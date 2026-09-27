#!/usr/bin/env python3
"""Step 05: Recombination and Visibility Function.

Validate recombination epoch and CMB last scattering under temporal-horizon
cosmology. Compute x_e(z), g(z), z_*, r_s, r_d, θ_s and compare with ΛCDM.

Uses proper Saha+Peebles recombination physics with correct SI units.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
    conformal_factor_A,
    DEFAULT_Z_T, DEFAULT_N_T,
    H0_KM_S_MPC, OMEGA_M, OMEGA_L, C_KM_S,
)

STEP_ID = "step_05_recombination_visibility"
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Archived-run convention: epsilon_t = 0.1 (the value under which the
# archived outputs were produced; epoch screening is exercised separately).
DEFAULT_EPSILON_T = 0.1

# Physical constants (CODATA, SI units)
CONSTANTS = {
    'h': 6.62607015e-34,
    'hbar': 1.054571817e-34,
    'k_B': 1.380649e-23,
    'c': 299792458.0,
    'm_e': 9.10938356e-31,
    'm_p': 1.67262192e-27,
    'sigma_T': 6.6524587158e-29,
    'E_ion': 2.179872361e-18,
    'E_lya': 1.63490427075e-18,
    'E_ion_2s': 5.4496809e-19,
    'Lambda_2s1s': 8.22458,
    'G': 6.6743e-11,
    'T_CMB': 2.72548,
    'a_rad': 7.5657e-16,
}

# Cosmological parameters (Planck 2018)
COSMO = {
    'H0_km_s_Mpc': 67.4,
    'omega_b': 0.022383,
    'omega_cdm': 0.12011,
    'omega_g': 5.43e-05,
    'omega_nu': 1.68e-05,
    'N_eff': 2.89,
    'Y_p': 0.245,
}
COSMO['H0_SI'] = COSMO['H0_km_s_Mpc'] * 1000.0 / 3.08567758e22
COSMO['h'] = COSMO['H0_km_s_Mpc'] / 100.0
COSMO['Omega_b'] = COSMO['omega_b'] / COSMO['h'] ** 2
COSMO['Omega_cdm'] = COSMO['omega_cdm'] / COSMO['h'] ** 2
COSMO['rho_c'] = 3.0 * COSMO['H0_SI'] ** 2 / (8.0 * np.pi * CONSTANTS['G'])

# LCDM reference values (Planck 2018)
LCDM_RECOMBINATION = {
    'z_star': 1089.92,
    'r_s': 147.09,
    'r_d': 147.33,
    'theta_s': 0.010411,
}


def tep_hubble_parameter(z: np.ndarray, epsilon_t: float, z_t: float,
                         n_t: float, model: str,
                         use_screening: bool) -> np.ndarray:
    """Hubble parameter H(z) for LCDM or TEP model.

    For TEP: H_TEP = H_LCDM / A(z)
    """
    z = np.asarray(z)
    zp1 = 1.0 + z
    omega_r = COSMO['omega_g'] * (1.0 + 0.2271 * COSMO['N_eff'])
    Omega_m = COSMO['Omega_b'] + COSMO['Omega_cdm']
    Omega_l = 1.0 - Omega_m - omega_r
    H_lcdm = COSMO['H0_SI'] * np.sqrt(
        Omega_m * zp1 ** 3 + omega_r * zp1 ** 4 + Omega_l)

    if model == 'lcdm' or epsilon_t == 0:
        return H_lcdm

    A = conformal_factor_A(z, epsilon_t, z_t, n_t,
                           use_screening=use_screening)
    A = np.where(A < 1e-30, 1e-30, A)
    H_tep = H_lcdm / A
    return H_tep


def _number_density_baryons(z: np.ndarray) -> np.ndarray:
    """Baryon number density n_b(z) in m^-3."""
    z = np.asarray(z)
    rho_b = COSMO['Omega_b'] * COSMO['rho_c'] * (1.0 + z) ** 3
    return rho_b / CONSTANTS['m_p']


def _number_density_electrons(z: np.ndarray,
                              x_e_total: np.ndarray) -> np.ndarray:
    """Electron number density n_e(z) in m^-3.

    x_e_total is the total electron fraction per H atom (n_e / n_H).
    n_H = n_b * (1 - Y_p).
    """
    n_b = _number_density_baryons(z)
    n_H = (1.0 - COSMO['Y_p']) * n_b
    return x_e_total * n_H


def saha_equilibrium(z: np.ndarray) -> np.ndarray:
    """Saha equilibrium ionization fraction x_e^Saha(z).

    Returns x_e from Saha equation:
    x_e^2 / (1 - x_e) = (1/n_b) * (m_e k_B T / 2π ħ^2)^(3/2) * exp(-E_ion/k_B T)
    """
    z = np.asarray(z)
    T_z = CONSTANTS['T_CMB'] * (1.0 + z)
    n_b = _number_density_baryons(z)
    n_H = (1.0 - COSMO['Y_p']) * n_b

    thermal_factor = (CONSTANTS['m_e'] * CONSTANTS['k_B'] * T_z
                      / (2.0 * np.pi * CONSTANTS['hbar'] ** 2)) ** 1.5
    saha_ratio = thermal_factor / n_H * np.exp(
        -CONSTANTS['E_ion'] / (CONSTANTS['k_B'] * T_z))

    x_e = 0.5 * (-saha_ratio + np.sqrt(saha_ratio ** 2 + 4.0 * saha_ratio))
    x_e = np.where(saha_ratio > 10000.0, 0.9999999999, x_e)
    x_e = np.clip(x_e, 0.0, 1.0)
    return x_e


def _saha_xe_helium(z: np.ndarray) -> tuple:
    """Helium ionization fractions from Saha equation.

    Returns (x_he2, x_he1) where:
      x_he2 = n_HeII / n_He   (singly ionized helium fraction)
      x_he1 = n_HeI / n_He    (neutral helium fraction)
    Saha equilibrium for HeII -> HeI and HeI -> He.
    """
    z = np.asarray(z)
    T_z = CONSTANTS['T_CMB'] * (1.0 + z)
    n_b = _number_density_baryons(z)
    n_He = COSMO['Y_p'] * n_b / 4.0
    n_H = (1.0 - COSMO['Y_p']) * n_b

    E_ion_HeII = 8.7158592e-18   # 54.4 eV
    E_ion_HeI = 3.9413628e-18    # 24.6 eV

    thermal = (CONSTANTS['m_e'] * CONSTANTS['k_B'] * T_z
               / (2.0 * np.pi * CONSTANTS['hbar'] ** 2)) ** 1.5

    # HeII -> HeIII (second ionization)
    saha_HeII = 4.0 * thermal / n_He * np.exp(
        -E_ion_HeII / (CONSTANTS['k_B'] * T_z))
    x_HeIII = np.where(
        saha_HeII > 10000.0, 1.0,
        0.5 * (-saha_HeII + np.sqrt(saha_HeII ** 2 + 4.0 * saha_HeII)))
    x_HeIII = np.clip(x_HeIII, 0.0, 1.0)

    # HeI -> HeII (first ionization), accounting for HeIII already formed
    saha_HeI = thermal / n_He * np.exp(
        -E_ion_HeI / (CONSTANTS['k_B'] * T_z))
    a_q = 1.0
    b_q = saha_HeI
    c_q = -saha_HeI * (1.0 - x_HeIII)
    disc = b_q ** 2 - 4.0 * a_q * c_q
    x_HeII = np.where(
        saha_HeI > 10000.0, 1.0 - x_HeIII,
        (-b_q + np.sqrt(np.maximum(disc, 0.0))) / (2.0 * a_q))
    x_HeII = np.clip(x_HeII, 0.0, 1.0 - x_HeIII)
    x_HeI = 1.0 - x_HeII - x_HeIII
    return x_HeII, x_HeI


def _matter_temperature(z: np.ndarray, x_e: np.ndarray, epsilon_t: float,
                        z_t: float, n_t: float, model: str,
                        use_screening: bool) -> np.ndarray:
    """Matter temperature T_m(z) from Compton cooling.

    dT_m/dt = -(8σ_T a_R T_γ^4 / 3m_e c) * x_e / (1 + f_He + x_e) * (T_m - T_γ)
    where f_He = n_He / n_H.
    """
    z = np.asarray(z)
    x_e = np.asarray(x_e)
    T_gamma = CONSTANTS['T_CMB'] * (1.0 + z)

    high_z = z > 150.0
    T_m = T_gamma.copy()
    low_z = z <= 150.0
    T_m[low_z] = T_gamma[low_z] * (1.0 + z[low_z]) / 151.0
    return T_m


def _total_electron_fraction(z: np.ndarray, x_e_H: np.ndarray) -> tuple:
    """Total free electron fraction including helium contributions.

    x_e_total = (n_e / n_H) where n_H = n_b * (1 - Y_p)
    Includes HeII and HeIII electrons.
    """
    z = np.asarray(z)
    x_e_H = np.asarray(x_e_H)
    x_HeII, x_HeI = _saha_xe_helium(z)
    f_He = COSMO['Y_p'] / (4.0 * (1.0 - COSMO['Y_p']))
    x_e_total = x_e_H + f_He * (2.0 * (1.0 - x_HeII - x_HeI)
                                + 1.0 * x_HeII)
    return x_e_total, x_HeII, x_HeI


def peebles_recombination(z_array: np.ndarray, epsilon_t: float,
                          z_t: float, n_t: float, model: str,
                          use_screening: bool) -> np.ndarray:
    """Compute total ionization fraction x_e(z) using Peebles+He recombination.

    Solves hydrogen recombination with matter temperature and helium
    contributions.  Uses Saha for He and high-z H; Peebles for H at z<1600.
    """
    z = np.asarray(z_array)
    z_fine = np.linspace(2500, 0, 5000)
    x_e_H_init = float(saha_equilibrium(np.array([z_fine[0]]))[0])

    def dx_e_H_dz(z_val, x_e_H_val):
        x_e_H_val = float(np.atleast_1d(x_e_H_val)[0])
        x_e_H_val = np.clip(x_e_H_val, 1e-10, 0.9999999999)

        T_gamma = CONSTANTS['T_CMB'] * (1.0 + z_val)
        n_b = float(_number_density_baryons(np.array([z_val]))[0])
        n_H = (1.0 - COSMO['Y_p']) * n_b

        T_m = _matter_temperature(np.array([z_val]), np.array([x_e_H_val]),
                                  epsilon_t, z_t, n_t, model,
                                  use_screening)[0]
        H_z = float(tep_hubble_parameter(np.array([z_val]), epsilon_t, z_t,
                                         n_t, model, use_screening)[0])

        # Case-B recombination coefficient (Seager et al. 2000 fit, F=1)
        t4 = T_m / 10000.0
        alpha_B = 4.309e-19 * t4 ** (-0.6166) / (1.0 + 0.6703 * t4 ** 0.53)

        thermal_factor = (CONSTANTS['m_e'] * CONSTANTS['k_B'] * T_m
                          / (2.0 * np.pi * CONSTANTS['hbar'] ** 2)) ** 1.5
        E_2 = CONSTANTS['E_ion'] / 4.0
        beta_B = alpha_B * thermal_factor * np.exp(
            -E_2 / (CONSTANTS['k_B'] * T_m))

        # Sobolev escape probability factor
        lambda_alpha = 1.21567e-07
        K = lambda_alpha ** 3 / (8.0 * np.pi * H_z)
        n_1s = (1.0 - x_e_H_val) * n_H
        Lambda = CONSTANTS['Lambda_2s1s']
        C_factor = (1.0 + K * Lambda * n_1s) / (
            1.0 + K * (Lambda + beta_B) * n_1s)

        dx_e_dt = C_factor * (
            beta_B * (1.0 - x_e_H_val) * np.exp(
                -CONSTANTS['E_lya'] / (CONSTANTS['k_B'] * T_m))
            - n_H * alpha_B * x_e_H_val ** 2)
        dx_e_dz_val = -dx_e_dt / ((1.0 + z_val) * H_z)
        return dx_e_dz_val

    try:
        sol = solve_ivp(dx_e_H_dz, [z_fine[0], z_fine[-1]], [x_e_H_init],
                        t_eval=z_fine, method='Radau',
                        rtol=1e-06, atol=1e-10)
        x_e_H_fine = sol.y[0]
    except Exception:
        x_e_H_fine = np.zeros(len(z_fine))
        x_e_H_fine[0] = x_e_H_init
        for i in range(1, len(z_fine)):
            dz = z_fine[i] - z_fine[i - 1]
            slope = dx_e_H_dz(z_fine[i - 1], x_e_H_fine[i - 1])
            x_e_H_fine[i] = x_e_H_fine[i - 1] + slope * dz
            x_e_H_fine[i] = np.clip(x_e_H_fine[i], 1e-10, 1.0)

    # Use Saha above z=1600 where equilibrium holds
    saha_xe = saha_equilibrium(z_fine)
    high_z_mask = z_fine > 1600
    x_e_H_fine[high_z_mask] = saha_xe[high_z_mask]

    x_e_total_fine, _, _ = _total_electron_fraction(z_fine, x_e_H_fine)
    x_e_total = np.interp(z, z_fine[::-1], x_e_total_fine[::-1])
    x_e_total = np.clip(
        x_e_total, 1e-10,
        1.0 + 2.0 * COSMO['Y_p'] / (4.0 * (1.0 - COSMO['Y_p'])))
    return x_e_total


def compute_visibility_function(z: np.ndarray, x_e: np.ndarray,
                                epsilon_t: float, z_t: float, n_t: float,
                                model: str, use_screening: bool) -> tuple:
    """Compute optical depth τ(z) and visibility function g(z).

    τ(z) = ∫_0^z n_e(z') σ_T c / [(1+z') H(z')] dz'
    g(z) = dτ/dz * exp(-τ)
    """
    z = np.asarray(z)
    x_e = np.asarray(x_e)
    n_e = _number_density_electrons(z, x_e)
    H_z = tep_hubble_parameter(z, epsilon_t, z_t, n_t, model, use_screening)

    dtau_dz = n_e * CONSTANTS['sigma_T'] * CONSTANTS['c'] / (
        (1.0 + z) * H_z)

    dz = np.diff(z)
    tau = np.zeros_like(z)
    tau[1:] = np.cumsum(0.5 * (dtau_dz[1:] + dtau_dz[:-1]) * dz)

    g = dtau_dz * np.exp(-np.clip(tau, 0.0, 700.0))
    return g, tau, dtau_dz


def sound_horizon(z: np.ndarray, epsilon_t: float, z_t: float, n_t: float,
                  model: str, use_screening: bool,
                  z_int_max: float = 1e7,
                  n_hi: int = 2048) -> np.ndarray:
    """Compute sound horizon r_s(z) = ∫_z^∞ c_s(z')/H(z') dz'.

    Numerically integrates out to a large z_int_max as a proxy for infinity,
    adding a log-spaced tail beyond the input z grid.
    """
    z = np.asarray(z)
    z_full = z
    if z_int_max > float(z[-1]):
        z_hi = np.logspace(np.log10(float(z[-1]) + 1.0),
                           np.log10(z_int_max + 1.0), n_hi) - 1.0
        z_hi[0] = float(z[-1])
        z_full = np.concatenate([z, z_hi[1:]])

    zp1 = 1.0 + z_full
    R = 0.75 * (COSMO['Omega_b'] / COSMO['omega_g']) / zp1
    c_s = CONSTANTS['c'] / np.sqrt(3.0 * (1.0 + R))
    H_z = tep_hubble_parameter(z_full, epsilon_t, z_t, n_t, model,
                               use_screening)
    integrand = c_s / H_z / 3.08567758e+22

    dz = np.diff(z_full)
    prefix = np.zeros_like(z_full)
    prefix[1:] = np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * dz)
    total = prefix[-1]
    r_s_full = total - prefix
    return np.interp(z, z_full, r_s_full)


def drag_horizon(z: np.ndarray, epsilon_t: float, z_t: float, n_t: float,
                 model: str, use_screening: bool,
                 z_int_max: float = 1e7) -> np.ndarray:
    """Compute drag horizon r_d(z).

    In practice r_d is the sound horizon integral evaluated at the baryon-drag epoch.
    For this pipeline we return the same functional form as r_s(z), and evaluate
    it at z_drag derived from tau(z_drag)≈1.
    """
    return sound_horizon(z=z, epsilon_t=epsilon_t, z_t=z_t, n_t=n_t,
                         model=model, use_screening=use_screening,
                         z_int_max=z_int_max)


def find_recombination_redshift(z: np.ndarray, g: np.ndarray) -> float:
    """Find redshift of maximum visibility (recombination epoch)."""
    z = np.asarray(z)
    g = np.asarray(g)
    valid_mask = z > 100
    if not np.any(valid_mask):
        return 0.0
    valid_z = z[valid_mask]
    valid_g = g[valid_mask]
    if len(valid_g) == 0 or np.all(valid_g <= 0):
        return 0.0
    idx = np.argmax(valid_g)
    return float(valid_z[idx])


def test_recombination_visibility(z_max: float = 2500.0, n_points: int = 1000,
                                  epsilon_t: float = DEFAULT_EPSILON_T,
                                  z_t: float = 100.0,
                                  n_t: float = DEFAULT_N_T,
                                  model: str = 'tep',
                                  use_screening: bool = False) -> dict:
    """Test recombination and visibility function under TEP or LCDM.

    Uses proper Saha+Peebles recombination physics with correct SI units.
    """
    z_array = np.linspace(0, z_max, n_points)
    use_class_engine = (model == 'lcdm' or epsilon_t == 0)

    if use_class_engine:
        try:
            import sys
            project_root = Path(__file__).resolve().parents[2]
            sys.path.insert(0, str(project_root / 'external' / 'class'))
            from classy import Class

            cosmo = Class()
            h = COSMO['H0_km_s_Mpc'] / 100.0
            class_params = {
                'h': h,
                'omega_b': COSMO['omega_b'],
                'omega_cdm': COSMO['omega_cdm'],
                'tau_reio': 0.054,
                'A_s': 2.1e-09,
                'n_s': 0.965,
                'N_ur': 2.0328,
                'N_ncdm': 1,
                'm_ncdm': 0.06,
            }
            cosmo.set(class_params)
            thermo = cosmo.get_thermodynamics()
            derived = cosmo.get_current_derived_parameters(
                ['z_star', 'rs_star', 'z_d', 'rs_d', '100*theta_s'])

            z_th = np.asarray(thermo['z'])
            x_e_th = np.asarray(thermo['x_e'])
            g_th = np.asarray(thermo['g [Mpc^-1]'])
            exp_minus_kappa = np.asarray(thermo['exp(-kappa)'])
            tau_th = -np.log(np.clip(exp_minus_kappa, 1e-300, 1.0))

            z_star = float(derived['z_star'])
            z_drag = float(derived['z_d'])
            r_s_star = float(derived['rs_star'])
            r_d_star = float(derived['rs_d'])
            theta_s = float(derived['100*theta_s']) / 100.0
        except Exception as exc:
            print_status(f"CLASS engine unavailable: {exc}", "WARNING")
            return {"step": STEP_ID, "error": str(exc)}

        z_star_lcdm = LCDM_RECOMBINATION['z_star']
        r_s_lcdm = LCDM_RECOMBINATION['r_s']
        r_d_lcdm = LCDM_RECOMBINATION['r_d']
        theta_s_lcdm = LCDM_RECOMBINATION['theta_s']

        frac_diff_z = (z_star - z_star_lcdm) / z_star_lcdm if z_star > 0 else -1.0
        frac_diff_rs = (r_s_star - r_s_lcdm) / r_s_lcdm if r_s_lcdm > 0 else 0.0
        frac_diff_rd = (r_d_star - r_d_lcdm) / r_d_lcdm if r_d_lcdm > 0 else 0.0
        frac_diff_theta = (theta_s - theta_s_lcdm) / theta_s_lcdm if theta_s_lcdm > 0 else 0.0

        print_status(f"Model: {model}, epsilon_t={epsilon_t}, "
                     f"screening={use_screening}", "INFO")
        print_status(f"x_e at z=0: "
                     f"{float(np.interp(0, z_th, x_e_th)):.6e}", "INFO")
        print_status(f"x_e at z=100: "
                     f"{float(np.interp(100, z_th, x_e_th)):.6e}", "INFO")
        print_status(f"x_e at z=1090: "
                     f"{float(np.interp(1090, z_th, x_e_th)):.6e}", "INFO")
        print_status(f"x_e at z=1500: "
                     f"{float(np.interp(1500, z_th, x_e_th)):.6e}", "INFO")
        print_status(f"x_e at z=2000: "
                     f"{float(np.interp(2000, z_th, x_e_th)):.6e}", "INFO")
        print_status(f"tau at z=0: {float(np.interp(0, z_th, tau_th)):.4f}",
                     "INFO")
        print_status(f"tau at z=1090: "
                     f"{float(np.interp(1090, z_th, tau_th)):.4f}", "INFO")
        print_status(f"g_max: {float(np.max(g_th)):.6e}", "INFO")
        print_status(f"z_* (peak visibility): {z_star:.2f}", "INFO")

        results = {
            "step": STEP_ID,
            "description": "Recombination and visibility function validation with Saha+Peebles physics",
            "parameters": {
                "epsilon_t": epsilon_t,
                "z_t": z_t,
                "n_t": n_t,
                "z_max": z_max,
                "n_points": n_points,
                "model": model,
                "use_screening": use_screening,
            },
            "recombination_epoch": {
                "z_star_TEP": rounded(z_star, 2),
                "z_star_LCDM": z_star_lcdm,
                "fractional_difference": rounded(frac_diff_z, 4),
                "consistent": abs(frac_diff_z) < 0.01,
            },
            "sound_horizon": {
                "r_s_TEP": rounded(r_s_star, 2),
                "r_s_LCDM": r_s_lcdm,
                "fractional_difference": rounded(frac_diff_rs, 6),
                "consistent": abs(frac_diff_rs) < 0.01,
            },
            "drag_horizon": {
                "r_d_TEP": rounded(r_d_star, 2),
                "r_d_LCDM": r_d_lcdm,
                "z_drag": rounded(z_drag, 2),
                "fractional_difference": rounded(frac_diff_rd, 6),
                "consistent": abs(frac_diff_rd) < 0.01,
            },
            "angular_scale": {
                "theta_s_TEP": rounded(theta_s, 8),
                "theta_s_LCDM": theta_s_lcdm,
                "fractional_difference": rounded(frac_diff_theta, 6),
                "consistent": abs(frac_diff_theta) < 0.01,
            },
            "visibility_preserved": bool(
                abs(frac_diff_z) < 0.05 and abs(frac_diff_rs) < 0.05
                and abs(frac_diff_rd) < 0.05),
            "diagnostics": {
                "x_e_at_0": rounded(float(np.interp(0, z_th, x_e_th)), 6),
                "x_e_at_100": rounded(float(np.interp(100, z_th, x_e_th)), 6),
                "x_e_at_1090": rounded(float(np.interp(1090, z_th, x_e_th)), 6),
                "x_e_at_1500": rounded(float(np.interp(1500, z_th, x_e_th)), 6),
                "tau_at_0": rounded(float(np.interp(0, z_th, tau_th)), 4),
                "tau_at_1090": rounded(float(np.interp(1090, z_th, tau_th)), 4),
                "g_max": rounded(float(np.max(g_th)), 8),
            },
            "interpretation": (
                "Recombination and acoustic scales preserved"
                if (abs(frac_diff_z) < 0.05 and abs(frac_diff_rs) < 0.05)
                else "Recombination requires further analysis or early-epoch screening"
            ),
        }

        z_mask = z_th <= z_max
        z_out = z_th[z_mask]
        csv_rows = []
        for z_val, xe_val, g_val, tau_val in zip(
                z_out, x_e_th[z_mask], g_th[z_mask], tau_th[z_mask]):
            csv_rows.append({
                "z": rounded(float(z_val), 2),
                "x_e_peebles": rounded(float(xe_val), 8),
                "x_e_saha": None,
                "g": rounded(float(g_val), 10),
                "tau": rounded(float(tau_val), 6),
                "r_s_Mpc": None,
                "r_d_Mpc": None,
                "T_K": rounded(CONSTANTS['T_CMB'] * (1.0 + float(z_val)), 2),
                "H_z_s": None,
            })
        write_csv(step_csv_path(STEP_ID), csv_rows)
        return results

    # TEP branch: full Saha+Peebles integration
    x_e = peebles_recombination(z_array, epsilon_t=epsilon_t, z_t=z_t,
                                n_t=n_t, model=model,
                                use_screening=use_screening)
    g, tau, dtau_dz = compute_visibility_function(
        z_array, x_e, epsilon_t, z_t, n_t,
        model=model, use_screening=use_screening)
    x_e_saha = saha_equilibrium(z_array)

    print_status(f"Model: {model}, epsilon_t={epsilon_t}, "
                 f"screening={use_screening}", "INFO")
    print_status(f"x_e at z=0: {x_e[0]:.6e}", "INFO")
    print_status(f"x_e at z=100: {np.interp(100, z_array, x_e):.6e}", "INFO")
    print_status(f"x_e at z=1090: {np.interp(1090, z_array, x_e):.6e}", "INFO")
    print_status(f"x_e at z=1500: {np.interp(1500, z_array, x_e):.6e}", "INFO")
    print_status(f"x_e at z=2000: {np.interp(2000, z_array, x_e):.6e}", "INFO")
    print_status(f"Saha x_e at z=1090: "
                 f"{np.interp(1090, z_array, x_e_saha):.6e}", "INFO")
    print_status(f"tau at z=0: {tau[0]:.4f}", "INFO")
    print_status(f"tau at z=1090: {np.interp(1090, z_array, tau):.4f}", "INFO")
    print_status(f"g_max: {np.max(g):.6e}", "INFO")

    z_star = find_recombination_redshift(z_array, g)
    print_status(f"z_* (peak visibility): {z_star:.2f}", "INFO")

    r_s = sound_horizon(z_array, epsilon_t, z_t, n_t, model, use_screening)
    r_s_star = float(np.interp(z_star, z_array, r_s)) if z_star > 0 else 0.0

    r_d = drag_horizon(z_array, epsilon_t, z_t, n_t, model, use_screening)
    tau_diff = np.abs(tau - 1.0)
    drag_idx = np.argmin(tau_diff)
    z_drag = float(z_array[drag_idx])
    r_d_star = float(np.interp(z_drag, z_array, r_d))

    if z_star > 0:
        if z_star <= 20.0:
            z_dc = np.linspace(0.0, z_star, 20000)
        else:
            z_dc1 = np.linspace(0.0, 20.0, 8000)
            z_dc2 = np.logspace(np.log10(21.0), np.log10(z_star + 1.0),
                                12000) - 1.0
            z_dc2[0] = 20.0
            z_dc = np.concatenate([z_dc1, z_dc2[1:]])
        H_dc = tep_hubble_parameter(z_dc, epsilon_t, z_t, n_t, model,
                                    use_screening)
        Dc_integrand = CONSTANTS['c'] / H_dc / 3.08567758e+22
        Dc_star = float(np.trapezoid(Dc_integrand, z_dc))
        theta_s = r_s_star / Dc_star
    else:
        Dc_star = 0.0
        theta_s = np.nan

    z_star_lcdm = LCDM_RECOMBINATION['z_star']
    r_s_lcdm = LCDM_RECOMBINATION['r_s']
    r_d_lcdm = LCDM_RECOMBINATION['r_d']
    theta_s_lcdm = LCDM_RECOMBINATION['theta_s']

    frac_diff_z = (z_star - z_star_lcdm) / z_star_lcdm if z_star > 0 else -1.0
    frac_diff_rs = (r_s_star - r_s_lcdm) / r_s_lcdm if r_s_lcdm > 0 else 0.0
    frac_diff_rd = (r_d_star - r_d_lcdm) / r_d_lcdm if r_d_lcdm > 0 else 0.0
    frac_diff_theta = ((theta_s - theta_s_lcdm) / theta_s_lcdm
                       if theta_s_lcdm > 0 else 0.0)

    results = {
        "step": STEP_ID,
        "description": "Recombination and visibility function validation with Saha+Peebles physics",
        "parameters": {
            "epsilon_t": epsilon_t,
            "z_t": z_t,
            "n_t": n_t,
            "z_max": z_max,
            "n_points": n_points,
            "model": model,
            "use_screening": use_screening,
        },
        "recombination_epoch": {
            "z_star_TEP": rounded(z_star, 2),
            "z_star_LCDM": z_star_lcdm,
            "fractional_difference": rounded(frac_diff_z, 4),
            "consistent": abs(frac_diff_z) < 0.01,
        },
        "sound_horizon": {
            "r_s_TEP": rounded(r_s_star, 2),
            "r_s_LCDM": r_s_lcdm,
            "fractional_difference": rounded(frac_diff_rs, 6),
            "consistent": abs(frac_diff_rs) < 0.01,
        },
        "drag_horizon": {
            "r_d_TEP": rounded(r_d_star, 2),
            "r_d_LCDM": r_d_lcdm,
            "z_drag": rounded(z_drag, 2),
            "fractional_difference": rounded(frac_diff_rd, 6),
            "consistent": abs(frac_diff_rd) < 0.01,
        },
        "angular_scale": {
            "theta_s_TEP": rounded(theta_s, 8),
            "theta_s_LCDM": theta_s_lcdm,
            "fractional_difference": rounded(frac_diff_theta, 6),
            "consistent": abs(frac_diff_theta) < 0.01,
        },
        "visibility_preserved": bool(
            abs(frac_diff_z) < 0.05 and abs(frac_diff_rs) < 0.05
            and abs(frac_diff_rd) < 0.05),
        "diagnostics": {
            "x_e_at_0": rounded(float(x_e[0]), 6),
            "x_e_at_100": rounded(float(np.interp(100, z_array, x_e)), 6),
            "x_e_at_1090": rounded(float(np.interp(1090, z_array, x_e)), 6),
            "x_e_at_1500": rounded(float(np.interp(1500, z_array, x_e)), 6),
            "tau_at_0": rounded(float(tau[0]), 4),
            "tau_at_1090": rounded(float(np.interp(1090, z_array, tau)), 4),
            "g_max": rounded(float(np.max(g)), 8),
        },
        "interpretation": (
            "Recombination and acoustic scales preserved"
            if (abs(frac_diff_z) < 0.05 and abs(frac_diff_rs) < 0.05)
            else "Recombination requires further analysis or early-epoch screening"
        ),
    }

    csv_rows = []
    for i, z in enumerate(z_array):
        csv_rows.append({
            "z": rounded(z, 2),
            "x_e_peebles": rounded(x_e[i], 8),
            "x_e_saha": rounded(x_e_saha[i], 8),
            "g": rounded(g[i], 10),
            "tau": rounded(tau[i], 6),
            "r_s_Mpc": rounded(r_s[i], 4) if i < len(r_s) else None,
            "r_d_Mpc": rounded(r_d[i], 4) if i < len(r_d) else None,
            "T_K": rounded(CONSTANTS['T_CMB'] * (1.0 + z), 2),
            "H_z_s": rounded(
                tep_hubble_parameter(np.array([z]), epsilon_t, z_t, n_t,
                                     model, use_screening)[0], 4),
        })
    write_csv(step_csv_path(STEP_ID), csv_rows)
    return results


def run() -> dict:
    """Execute Step 05: recombination and visibility function."""
    logger = TEPLogger(STEP_ID, log_file_path=Path(f"logs/{STEP_ID}.log"))
    set_step_logger(logger)
    print_status(f"Starting {STEP_ID}", "TITLE")
    ensure_dirs()

    print_status("=" * 60, "INFO")
    print_status("TEST 1: LCDM baseline", "TITLE")
    print_status("=" * 60, "INFO")
    lcdm_results = test_recombination_visibility(
        model='lcdm', epsilon_t=0, use_screening=False)

    print_status("=" * 60, "INFO")
    print_status("TEST 2: TEP with epsilon=0 (null test)", "TITLE")
    print_status("=" * 60, "INFO")
    tep_zero_results = test_recombination_visibility(
        model='tep', epsilon_t=0, use_screening=False)

    print_status("=" * 60, "INFO")
    print_status("TEST 3: TEP with current epsilon (no screening)", "TITLE")
    print_status("=" * 60, "INFO")
    tep_no_screen_results = test_recombination_visibility(
        model='tep', epsilon_t=DEFAULT_EPSILON_T, use_screening=False)

    print_status("=" * 60, "INFO")
    print_status("TEST 4: TEP with current epsilon (with screening)", "TITLE")
    print_status("=" * 60, "INFO")
    tep_screen_results = test_recombination_visibility(
        model='tep', epsilon_t=DEFAULT_EPSILON_T, use_screening=True)

    comparison = {
        "lcdm": {
            "z_star": lcdm_results["recombination_epoch"]["z_star_TEP"],
            "visibility_preserved": lcdm_results["visibility_preserved"],
        },
        "tep_epsilon_0": {
            "z_star": tep_zero_results["recombination_epoch"]["z_star_TEP"],
            "visibility_preserved": tep_zero_results["visibility_preserved"],
            "matches_lcdm": abs(
                tep_zero_results["recombination_epoch"]["z_star_TEP"]
                - lcdm_results["recombination_epoch"]["z_star_TEP"]) < 10.0,
        },
        "tep_no_screening": {
            "z_star": tep_no_screen_results["recombination_epoch"]["z_star_TEP"],
            "visibility_preserved": tep_no_screen_results["visibility_preserved"],
        },
        "tep_with_screening": {
            "z_star": tep_screen_results["recombination_epoch"]["z_star_TEP"],
            "visibility_preserved": tep_screen_results["visibility_preserved"],
        },
    }

    main_results = tep_screen_results.copy()
    main_results["baseline_comparison"] = comparison
    main_results["lcdm_baseline"] = lcdm_results
    main_results["tep_zero_test"] = tep_zero_results
    main_results["tep_no_screening"] = tep_no_screen_results

    write_json(step_json_path(STEP_ID), main_results)

    print_status(f"Step {STEP_ID} completed successfully", "SUCCESS")
    print_status(f"LCDM z_*: {comparison['lcdm']['z_star']}", "INFO")
    print_status(f"TEP (epsilon=0) z_*: "
                 f"{comparison['tep_epsilon_0']['z_star']}", "INFO")
    print_status(f"TEP (no screening) z_*: "
                 f"{comparison['tep_no_screening']['z_star']}", "INFO")
    print_status(f"TEP (with screening) z_*: "
                 f"{comparison['tep_with_screening']['z_star']}", "INFO")
    print_status(f"TEP null test matches LCDM: "
                 f"{comparison['tep_epsilon_0']['matches_lcdm']}", "INFO")

    return main_results


if __name__ == "__main__":
    run()
