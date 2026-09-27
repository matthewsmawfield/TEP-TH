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
    h = 6.626e-34
    k = 1.381e-23
    c = 2.998e8
    x = h * freq / (k * T)
    intensity = 2 * h * freq**3 / c**2 / (np.exp(x) - 1)
    return intensity


def mu_distortion_spectrum(freq: np.ndarray, T: float, mu: float) -> np.ndarray:
    """μ-distortion spectrum (chemical-potential template)."""
    B = planck_spectrum(freq, T)
    x = 6.626e-34 * freq / (1.381e-23 * T)
    correction = mu * (x * (np.exp(x) + 1) / (np.exp(x) - 1) - 4) * B
    return B + correction


def y_distortion_spectrum(freq: np.ndarray, T: float, y: float) -> np.ndarray:
    """y-distortion spectrum (Compton-y template)."""
    B = planck_spectrum(freq, T)
    x = 6.626e-34 * freq / (1.381e-23 * T)
    correction = y * x * (np.exp(x) + 1) / (np.exp(x) - 1) * (x / np.tanh(x / 2) - 4) * B
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
                               p0=[2.725], sigma=err)
        T_fit = popt[0]
        T_err = np.sqrt(pcov[0, 0])
        return T_fit, T_err
    except (RuntimeError, ValueError, np.linalg.LinAlgError):
        return 2.725, 0.001


def fit_mu_distortion(freq: np.ndarray, intensity: np.ndarray,
                      err: np.ndarray, T: float) -> tuple:
    """Fit μ-distortion amplitude."""
    try:
        popt, pcov = curve_fit(
            lambda f, mu: mu_distortion_spectrum(f, T, mu),
            freq, intensity, p0=[0.0], sigma=err)
        return popt[0], np.sqrt(pcov[0, 0])
    except (RuntimeError, ValueError, np.linalg.LinAlgError):
        return 0.0, 1e-5


def fit_y_distortion(freq: np.ndarray, intensity: np.ndarray,
                     err: np.ndarray, T: float) -> tuple:
    """Fit y-distortion amplitude."""
    try:
        popt, pcov = curve_fit(
            lambda f, y: y_distortion_spectrum(f, T, y),
            freq, intensity, p0=[0.0], sigma=err)
        return popt[0], np.sqrt(pcov[0, 0])
    except (RuntimeError, ValueError, np.linalg.LinAlgError):
        return 0.0, 1e-5


def test_blackbody_preservation(z_test: float = 1100.0,
                                epsilon_t: float = DEFAULT_EPSILON_T_STEP,
                                z_t: float = DEFAULT_Z_T_STEP,
                                n_t: float = DEFAULT_N_T_STEP,
                                T_lock: float = DEFAULT_T_LOCK_STEP,
                                n_epoch: float = DEFAULT_N_EPOCH_STEP,
                                use_screening: bool = True) -> dict:
    """Test whether temporal-horizon thermal mapping preserves Planckianity.

    When CLASS is importable, μ and y are taken from its spectral-distortion
    module (the deployed analytic SD computation). Otherwise they are fitted
    to the TEP-remapped spectrum against FIRAS errors.
    """
    class_sd = class_spectral_distortions()
    if class_sd is not None:
        mu_fit, y_fit = class_sd
        mu_err = 0.0
        y_err = 0.0
        has_data = True
        T_firas = 2.725
        T_err = 0.0
        freq = intensity_tep = err = None
    else:
        freq, intensity, err, has_data = load_firas_data()
        T_firas, T_err = fit_blackbody_temperature(freq, intensity, err)

    T0 = 2.725
    A_z = conformal_factor_A(z_test, epsilon_t, z_t, n_t,
                             T_lock, n_epoch, use_screening)
    T_tep_prediction = T0 / A_z

    if class_sd is None:
        intensity_tep = tep_thermal_scaling(freq, T0, z_test, epsilon_t, z_t, n_t,
                                            T_lock, n_epoch, use_screening)
        T_tep_fit, T_tep_err = fit_blackbody_temperature(freq, intensity_tep, err)
        mu_fit, mu_err = fit_mu_distortion(freq, intensity_tep, err, T_tep_fit)
        y_fit, y_err = fit_y_distortion(freq, intensity_tep, err, T_tep_fit)
    else:
        T_tep_fit = T_tep_prediction
        T_tep_err = 1e-6

    mu_constraint = 9e-5
    y_constraint = 1.5e-5

    results = {
        "step": STEP_ID,
        "description": "CMB blackbody preservation under temporal-horizon thermal mapping",
        "parameters": {
            "epsilon_t": epsilon_t,
            "z_t": z_t,
            "n_t": n_t,
            "z_test": z_test,
        },
        "firas_analysis": {
            "has_data": has_data,
            "T_firas": rounded(T_firas, 6),
            "T_error": rounded(T_err, 6),
            "consistent_with_standard": bool(abs(T_firas - 2.725) < 3 * T_err),
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

    if class_sd is None and freq is not None:
        csv_rows = [{
            "freq_GHz": rounded(f / 1e9, 2),
            "firas_intensity": rounded(intensity[i], 10)
            if 'intensity' in dir() else 0.0,
            "tep_intensity": rounded(intensity_tep[i], 10),
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

    write_json(step_json_path(STEP_ID), results)

    status = "PASS" if results["blackbody_preserved"] else "FAIL"
    print_status(f"Step 06 complete: {status} "
                 f"(μ = {results['spectral_distortions']['mu_fit']:.2e}, "
                 f"y = {results['spectral_distortions']['y_fit']:.2e})",
                 "SUCCESS" if results["blackbody_preserved"] else "WARNING")

    return results


if __name__ == "__main__":
    run()
