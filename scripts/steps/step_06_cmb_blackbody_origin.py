#!/usr/bin/env python3
"""Step 06: CMB Blackbody Origin and Spectral Distortion.

Test whether the temporal-horizon thermal mapping preserves a Planckian
spectrum and does not generate forbidden μ or y spectral distortions.
"""

from __future__ import annotations

import sys
from pathlib import Path
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import zeta

from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
    conformal_factor_A,
)

STEP_ID = "step_06_cmb_blackbody_origin"
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Archived-run conventions: this step was originally executed under
# epsilon_t = 0.1 with epoch screening active (S_epoch suppresses the shear
# at recombination). These are retained as module defaults so the step
# reproduces its archived output.
DEFAULT_EPSILON_T_STEP = 0.1
DEFAULT_Z_T_STEP = 100.0
DEFAULT_N_T_STEP = 1.0
DEFAULT_T_LOCK_STEP = 30.0   # eV
DEFAULT_N_EPOCH_STEP = 2.0


def class_spectral_distortions() -> tuple | None:
    """Compute μ and y spectral distortions via CLASS's analytic module."""
    try:
        project_root = Path(__file__).resolve().parents[2]
        sys.path.insert(0, str(project_root / "external" / "class"))
        from classy import Class
        cosmo = Class()
        params = {
            'h': 0.674,
            'omega_b': 0.022383,
            'omega_cdm': 0.12011,
            'A_s': 2.1e-9,
            'n_s': 0.965,
            'tau_reio': 0.054,
            'N_ur': 2.0328,
            'N_ncdm': 1,
            'm_ncdm': 0.06,
            'output': 'tCl sd',
            'modes': 's',
            'l_max_scalars': 10,
        }
        cosmo.set(params)
        cosmo.compute()
        derived = cosmo.get_current_derived_parameters(['mu_sd', 'y_sd'])
        cosmo.struct_cleanup()
        cosmo.empty()
        return float(derived['mu_sd']), float(derived['y_sd'])
    except Exception:
        return None


def load_firas_data() -> tuple:
    """Load FIRAS CMB spectrum if available.

    Expects data/raw/firas_spectrum.dat with columns:
    frequency [Hz], intensity [W m^-2 Hz^-1 sr^-1], error [same units].
    Returns (freq, intensity, err, has_data).
    """
    firas_file = PROJECT_ROOT / "data" / "raw" / "firas_spectrum.dat"
    if firas_file.exists():
        data = np.loadtxt(firas_file)
        freq = data[:, 0]
        intensity = data[:, 1]
        err = data[:, 2]
        has_data = True
    else:
        # FIRAS frequency range: ~2 cm^-1 to ~20 cm^-1
        freq = np.linspace(2e10, 6e11, 43)
        intensity = np.zeros(43)
        err = np.ones(43) * 1e-22
        has_data = False
    return freq, intensity, err, has_data


def planck_spectrum(freq: np.ndarray, T: float) -> np.ndarray:
    """Planck blackbody spectrum B_ν(T) in W m^-2 Hz^-1 sr^-1."""
    h = 6.62607015e-34
    k = 1.380649e-23
    c = 299792458.0
    x = h * freq / (k * T)
    # exp(-x)/[1-exp(-x)] avoids both Rayleigh-Jeans cancellation
    # and Wien-tail exponential overflow.
    intensity = 2 * h * freq**3 / c**2 * np.exp(-x) / (-np.expm1(-x))
    return intensity


def mu_distortion_spectrum(freq: np.ndarray, T: float, mu: float) -> np.ndarray:
    """μ-distortion spectrum (chemical-potential template)."""
    B = planck_spectrum(freq, T)
    x = 6.62607015e-34 * freq / (1.380649e-23 * T)
    # Photon-number-conserving chemical-potential basis:
    # M = G [1/beta_mu - 1/x], beta_mu = 3 zeta(3)/zeta(2).
    # G is the fractional-temperature response of intensity.
    beta_mu = 3.0 * zeta(3.0, 1.0) / zeta(2.0, 1.0)
    G = x / (-np.expm1(-x)) * B
    correction = mu * G * (1.0 / beta_mu - 1.0 / x)
    return B + correction


def y_distortion_spectrum(freq: np.ndarray, T: float, y: float) -> np.ndarray:
    """y-distortion spectrum (Compton-y template)."""
    B = planck_spectrum(freq, T)
    x = 6.62607015e-34 * freq / (1.380649e-23 * T)
    # Y = G [x coth(x/2) - 4]; the temperature-response prefactor
    # is x exp(x)/(exp(x)-1), not x coth(x/2).
    G = x / (-np.expm1(-x)) * B
    correction = y * G * (x / np.tanh(x / 2.0) - 4.0)
    return B + correction


def tep_thermal_scaling(freq: np.ndarray, T0: float, z: float,
                        epsilon_t: float, z_t: float, n_t: float,
                        T_lock: float, n_epoch: float,
                        use_screening: bool) -> np.ndarray:
    """TEP thermal scaling: CMB spectrum at redshift z under conformal clock."""
    A_z = conformal_factor_A(z, epsilon_t, z_t, n_t, T_lock, n_epoch, use_screening)
    T_z = T0 / A_z  # Temperature rescales as T = T_0 / A
    return planck_spectrum(freq, T_z)


def fit_blackbody_temperature(freq: np.ndarray, intensity: np.ndarray,
                              err: np.ndarray) -> tuple:
    """Fit temperature to spectrum, return (T, sigma_T)."""
    try:
        popt, pcov = curve_fit(planck_spectrum, freq, intensity,
                               p0=[2.725], sigma=err, absolute_sigma=True)
        T_fit = popt[0]
        T_err = np.sqrt(pcov[0, 0])
        return T_fit, T_err
    except (RuntimeError, ValueError, np.linalg.LinAlgError):
        raise RuntimeError("Blackbody-temperature fit failed; no substitute result is valid")


def _fit_linear_distortion(freq, intensity, err, T, spectrum):
    """Exact weighted fit for a linear spectral template; absolute errors."""
    err = np.asarray(err, dtype=float)
    if np.any(~np.isfinite(err)) or np.any(err <= 0):
        raise ValueError("Spectral errors must be finite and positive")
    B = planck_spectrum(freq, T)
    template = spectrum(freq, T, 1.0) - B
    weighted = template / err
    information = float(np.dot(weighted, weighted))
    if not np.isfinite(information) or information <= 0:
        raise ValueError("Spectral template has no finite information")
    amplitude = float(np.dot(weighted, (np.asarray(intensity) - B) / err)
                      / information)
    return amplitude, 1.0 / np.sqrt(information)


def fit_mu_distortion(freq: np.ndarray, intensity: np.ndarray,
                      err: np.ndarray, T: float) -> tuple:
    """Fit the linear photon-number-conserving μ template."""
    return _fit_linear_distortion(freq, intensity, err, T, mu_distortion_spectrum)


def fit_y_distortion(freq: np.ndarray, intensity: np.ndarray,
                     err: np.ndarray, T: float) -> tuple:
    """Fit the linear Compton-y template."""
    return _fit_linear_distortion(freq, intensity, err, T, y_distortion_spectrum)


def test_blackbody_preservation(z_test: float = 1100.0,
                                epsilon_t: float = DEFAULT_EPSILON_T_STEP,
                                z_t: float = DEFAULT_Z_T_STEP,
                                n_t: float = DEFAULT_N_T_STEP,
                                T_lock: float = DEFAULT_T_LOCK_STEP,
                                n_epoch: float = DEFAULT_N_EPOCH_STEP,
                                use_screening: bool = True) -> dict:
    """Test whether temporal-horizon thermal mapping preserves Planckianity.

    The TEP-remapped Planck spectrum is tested directly. CLASS values are
    reported separately as an LCDM reference. Missing FIRAS data are not
    represented as observations; synthetic fits check transport/templates.
    """
    # CLASS receives LCDM parameters here: it is a reference, not the
    # TEP transport calculation and not a FIRAS observation.
    class_sd = class_spectral_distortions()
    freq, intensity, err, has_data = load_firas_data()
    if has_data:
        T_firas, T_err_stat = fit_blackbody_temperature(freq, intensity, err)
        # Include FIRAS absolute thermometer calibration uncertainty (0.6 mK, Fixsen 2009)
        T_err = float(np.sqrt(T_err_stat**2 + 0.0006**2))
    else:
        T_firas = T_err = None

    T0 = 2.725
    A_z = conformal_factor_A(z_test, epsilon_t, z_t, n_t,
                             T_lock, n_epoch, use_screening)
    T_tep_prediction = T0 / A_z

    intensity_tep = tep_thermal_scaling(freq, T0, z_test, epsilon_t, z_t, n_t,
                                        T_lock, n_epoch, use_screening)
    T_tep_fit, T_tep_err = fit_blackbody_temperature(freq, intensity_tep, err)
    mu_fit, mu_err = fit_mu_distortion(freq, intensity_tep, err, T_tep_fit)
    y_fit, y_err = fit_y_distortion(freq, intensity_tep, err, T_tep_fit)

    mu_constraint = 9e-5
    y_constraint = 1.5e-5

    results = {
        "step": STEP_ID,
        "description": "CMB blackbody preservation under temporal-horizon thermal mapping",
        "test_kind": "Analytic homogeneous transport and template-recovery check; not an independently derived thermalization history",
        "class_lcdm_reference": {"available": class_sd is not None,
                                 "mu": class_sd[0] if class_sd is not None else None,
                                 "y": class_sd[1] if class_sd is not None else None},
        "parameters": {
            "epsilon_t": epsilon_t,
            "z_t": z_t,
            "n_t": n_t,
            "z_test": z_test,
        },
        "firas_analysis": {
            "has_data": has_data,
            "T_firas": rounded(T_firas, 6) if has_data else None,
            "T_error": rounded(T_err, 6) if has_data else None,
            "consistent_with_standard": bool(abs(T_firas - 2.725) < 3 * T_err) if has_data else None,
        },
        "tep_thermal_mapping": {
            "A_at_z_test": rounded(A_z, 10),
            "T_tep_prediction": rounded(T_tep_prediction, 6),
            "T_tep_fit": rounded(T_tep_fit, 6),
            "T_tep_error": rounded(T_tep_err, 6),
            "thermal_scaling_preserves_blackbody": bool(
                abs(T_tep_fit - T_tep_prediction) < max(3 * T_tep_err, 1e-6)),
        },
        "spectral_distortions": {
            "mu_fit": rounded(mu_fit, 8),
            "mu_error": rounded(mu_err, 8),
            "mu_constraint": mu_constraint,
            "mu_violates_firas": bool(abs(mu_fit) > mu_constraint),
            "y_fit": rounded(y_fit, 8),
            "y_error": rounded(y_err, 8),
            "y_constraint": y_constraint,
            "y_violates_firas": bool(abs(y_fit) > y_constraint),
        },
        "blackbody_preserved": bool(abs(mu_fit) < mu_constraint
                                    and abs(y_fit) < y_constraint),
        "interpretation": (
            "Temporal-horizon thermal mapping preserves blackbody spectrum "
            "without forbidden distortions"
            if (abs(mu_fit) < mu_constraint and abs(y_fit) < y_constraint)
            else "Temporal-horizon mapping generates forbidden spectral "
                 "distortions"
        ),
    }

    if freq is not None:
        csv_rows = [{
            "freq_GHz": rounded(f / 1e9, 2),
            "firas_intensity": float(intensity[i]) if has_data else None,
            "tep_intensity": float(intensity_tep[i]),
        } for i, f in enumerate(freq)]
        write_csv(step_csv_path(STEP_ID), csv_rows)

    return results


def run() -> dict:
    """Execute Step 06: CMB blackbody origin and spectral distortions."""
    logger = TEPLogger(STEP_ID, log_file_path=PROJECT_ROOT / "logs" / f"{STEP_ID}.log")
    set_step_logger(logger)
    ensure_dirs()

    print_status("Testing CMB blackbody preservation under TEP thermal mapping...")

    results = test_blackbody_preservation(z_test=1100.0)

    z_tests = np.array([100, 500, 1100, 2000])
    distortion_evolution = []
    for z in z_tests:
        r = test_blackbody_preservation(z_test=float(z))
        distortion_evolution.append({
            "z": float(z),
            "mu_fit": r["spectral_distortions"]["mu_fit"],
            "y_fit": r["spectral_distortions"]["y_fit"],
            "blackbody_preserved": r["blackbody_preserved"],
        })
    results["redshift_evolution"] = distortion_evolution

    # Forward-integrated homogeneous Saha+Peebles electron-density and
    # Thomson optical-depth profile across the dust-to-plasma transition
    # (z = 130 to 2000), using Step 05's recombination solver.
    import step_05_recombination_visibility as s5
    z_grid = np.linspace(0.0, 2000.0, 2001)
    xe_grid = s5.peebles_recombination(
        z_grid, epsilon_t=DEFAULT_EPSILON_T_STEP, z_t=DEFAULT_Z_T_STEP,
        n_t=DEFAULT_N_T_STEP, model="tep", use_screening=True,
    )
    _, tau_grid, _ = s5.compute_visibility_function(
        z_grid, xe_grid, epsilon_t=DEFAULT_EPSILON_T_STEP, z_t=DEFAULT_Z_T_STEP,
        n_t=DEFAULT_N_T_STEP, model="tep", use_screening=True,
    )
    ne_grid_cm3 = s5._number_density_electrons(z_grid, xe_grid) * 1e-6
    t_grid_k = s5.CONSTANTS["T_CMB"] * (1.0 + z_grid)
    profile_rows = []
    for z_probe in [0.0, 10.0, 100.0, 130.0, 500.0, 1079.0, 1100.0, 1500.0, 2000.0]:
        idx = int(np.argmin(np.abs(z_grid - z_probe)))
        profile_rows.append({
            "z": float(z_grid[idx]),
            "T_loc_K": rounded(float(t_grid_k[idx]), 2),
            "x_e": rounded(float(xe_grid[idx]), 6),
            "n_e_cm3": rounded(float(ne_grid_cm3[idx]), 6),
            "tau_es": rounded(float(tau_grid[idx]), 5),
        })
    z_tau_unity = float(np.interp(1.0, tau_grid, z_grid))
    results["forward_optical_depth_profile"] = {
        "scope": (
            "Homogeneous Saha+Peebles recombination and Thomson optical-depth "
            "profile across the dust-to-plasma transition (Step 05 solver); "
            "inhomogeneous absorber-clumping inversion remains separate."
        ),
        "z_tau_es_unity": rounded(z_tau_unity, 2),
        "profile": profile_rows,
    }

    write_json(step_json_path(STEP_ID), results)

    status = "PASS" if results["blackbody_preserved"] else "FAIL"
    print_status(f"Step 06 complete: {status} "
                 f"(μ = {results['spectral_distortions']['mu_fit']:.2e}, "
                 f"y = {results['spectral_distortions']['y_fit']:.2e})",
                 "SUCCESS" if results["blackbody_preserved"] else "WARNING")

    return results


if __name__ == "__main__":
    run()
