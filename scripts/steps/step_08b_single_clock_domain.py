#!/usr/bin/env python3
"""Step 08b: Single-clock perturbative domain of control.

Quantifies the domain in which the reconstructed single-clock sector of
Section 10 remains perturbatively controlled.  The pump field

    z_A(eta) = z_* (eta/eta_*)^{-(1+epsilon_field)}

vanishes only asymptotically (eta -> infinity, A_clock -> 0), i.e. at the
temporal horizon itself.  A mode k exits its sound horizon at

    eta_k = sqrt(nu_A^2 - 1/4) / k ,   nu_A = 3/2 + epsilon_field ,

and the per-decade variance of the field fluctuation in the oscillatory
(WKB) regime is

    P_dchi(k, eta) = k^2 / (4 pi^2 z_A^2(eta)) ,

which grows toward the frontier as (eta/eta_k)^{2+2epsilon_field} and
reaches order unity at the strong-coupling surface eta_sc(k).  The step
computes eta_k, z_A at freeze-out, P_dchi at freeze-out, eta_sc, and the
margin eta_sc/eta_k across the CMB wavenumber band, establishing that
freeze-out occurs deep inside the controlled window while the
strong-coupling frontier remains asymptotically separated.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
from scipy.special import gamma as gamma_fn
from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
)

STEP_ID = "step_08b_single_clock_domain"

# Fiducial single-clock parameters (Section 10.6)
N_S = 0.9649            # scalar spectral index
A_S = 2.10e-9           # scalar amplitude at pivot
K_PIVOT = 0.05          # Mpc^-1
ETA_STAR = 6000.0       # Mpc, reference epoch eta_* = eta_0
P_POWER = 0.1           # conformal-time exponent, A_clock = C eta^{-p}

# Field-map to canonical scalar sector (universal coupling, Rule 3)
BETA_A = -1.0           # chi = beta_A phi / M_Pl


def epsilon_field(n_s: float = N_S) -> float:
    return (1.0 - n_s) / 2.0


def nu_A(eps: float) -> float:
    return 1.5 + eps


def z_star_sq(eps: float, n_s: float = N_S, a_s: float = A_S,
              k_pivot: float = K_PIVOT, eta_star: float = ETA_STAR) -> float:
    """Pump-field normalization from the manuscript's A_s-matching formula:

        z_*^2 = [2^{2 nu_A - 3} Gamma(nu_A)^2 / (pi^3 A_s)]
                k_*^{3 - 2 nu_A} eta_*^{1 - 2 nu_A}
    """
    nu = nu_A(eps)
    pref = (2.0 ** (2.0 * nu - 3.0)) * gamma_fn(nu) ** 2 / (np.pi ** 3 * a_s)
    return pref * (k_pivot ** (3.0 - 2.0 * nu)) * (eta_star ** (1.0 - 2.0 * nu))


def z_A(eta: np.ndarray, z_st: float, eps: float, eta_star: float = ETA_STAR) -> np.ndarray:
    return z_st * (eta / eta_star) ** (-(1.0 + eps))


def eta_freeze(k: np.ndarray, eps: float) -> np.ndarray:
    """Sound-horizon crossing k^2 eta^2 = nu_A^2 - 1/4."""
    nu = nu_A(eps)
    return np.sqrt(nu * nu - 0.25) / k


def eta_strong_coupling(k: np.ndarray, z_st: float, eps: float,
                        eta_star: float = ETA_STAR) -> np.ndarray:
    """Surface where P_dchi(k, eta) = k^2/(4 pi^2 z_A^2) reaches unity."""
    return eta_star * (2.0 * np.pi * z_st / k) ** (1.0 / (1.0 + eps))


def analyze_domain(eps: float, k_array: np.ndarray) -> dict:
    nu = nu_A(eps)
    z2 = z_star_sq(eps)
    z_st = np.sqrt(z2)

    eta_k = eta_freeze(k_array, eps)
    z_at_k = z_A(eta_k, z_st, eps)
    # Per-decade variance of delta chi evaluated at freeze-out
    P_dchi_k = k_array ** 2 / (4.0 * np.pi ** 2 * z_at_k ** 2)
    # Asymptotic growth exponent toward the frontier (oscillatory regime)
    growth_exp = 2.0 + 2.0 * eps
    eta_sc = eta_strong_coupling(k_array, z_st, eps)
    margin = eta_sc / eta_k

    ipiv = int(np.argmin(np.abs(k_array - K_PIVOT)))

    per_mode = [{
        'k_Mpc': rounded(k, 6),
        'eta_freeze_Mpc': rounded(eta_k[i], 4),
        'z_A_at_freeze': rounded(z_at_k[i], 4),
        'P_dchi_at_freeze': float(f"{P_dchi_k[i]:.4e}"),
        'eta_strong_coupling_Mpc': rounded(eta_sc[i], 1),
        'controlled_window_eta_sc_over_eta_k': rounded(margin[i], 2),
    } for i, k in enumerate(k_array)]

    return {
        'field_map': {
            'chi_definition': 'chi = ln A_clock',
            'canonical_scalar_map': 'chi = beta_A * phi / M_Pl',
            'beta_A': BETA_A,
            'phi_of_chi': 'phi = -M_Pl * chi = M_Pl * ln(1+z)',
            'canonical_limit': 'Z = 1 (constant kinetic function)',
            'completion_generator': (
                'Within the master action the only single-scalar sector capable of '
                'generating a field-dependent homogeneous kinetic normalization is the '
                'disformal channel B(phi) nabla phi nabla phi on the time-dependent '
                'background; the conformal sector is already absorbed into chi and the '
                'potential enters U separately.'
            ),
            'ambient_limit': 'Z(chi=0) = Z_* finite at the present epoch (phi = 0 ambient)',
        },
        'pump_field': {
            'form': 'z_A(eta) = z_* (eta/eta_*)^{-(1+epsilon_field)}',
            'z_star': rounded(z_st, 4),
            'epsilon_field': rounded(eps, 6),
            'nu_A': rounded(nu, 6),
            'frontier': 'z_A -> 0 only as eta -> infinity (A_clock -> 0, temporal horizon)',
        },
        'variance_growth': {
            'regime': 'oscillatory (k eta >> 1), WKB branch |v_k| ~ (2k)^{-1/2}',
            'law': 'P_dchi(k,eta) ~ A_s(k) (eta/eta_k)^{2+2 epsilon_field}',
            'exponent': rounded(growth_exp, 4),
        },
        'per_mode': per_mode,
        'pivot_mode': {
            'k_Mpc': K_PIVOT,
            'eta_freeze_Mpc': rounded(eta_k[ipiv], 4),
            'z_A_at_freeze': rounded(z_at_k[ipiv], 4),
            'P_dchi_at_freeze': float(f"{P_dchi_k[ipiv]:.4e}"),
            'delta_chi_rms_at_freeze': float(f"{np.sqrt(P_dchi_k[ipiv]):.4e}"),
            'eta_strong_coupling_Mpc': rounded(eta_sc[ipiv], 1),
            'controlled_window_decades': rounded(np.log10(margin[ipiv]), 3),
        },
        'min_controlled_window': rounded(float(np.min(margin)), 2),
        'min_controlled_window_decades': rounded(float(np.log10(np.min(margin))), 3),
    }


def run():
    logger = TEPLogger(STEP_ID, log_file_path=Path(f"logs/{STEP_ID}.log"))
    set_step_logger(logger)
    print_status(f"Starting {STEP_ID}", "TITLE")
    ensure_dirs()

    eps = epsilon_field()
    k_array = np.logspace(-4, 0, 13)
    analysis = analyze_domain(eps, k_array)

    min_margin = analysis['min_controlled_window']
    controlled = min_margin > 100.0

    results = {
        'step': STEP_ID,
        'description': 'Domain of perturbative control for the reconstructed single-clock sector',
        'parameters': {
            'n_s': N_S,
            'A_s': A_S,
            'k_pivot': K_PIVOT,
            'eta_star_Mpc': ETA_STAR,
            'p': P_POWER,
            'beta_A': BETA_A,
        },
        'analysis': analysis,
        'freeze_out_controlled': bool(controlled),
        'frontier_asymptotic': True,
        'interpretation': (
            'Freeze-out occurs ~%.1f decades inside the strong-coupling surface for all CMB '
            'modes; P_dchi at freeze-out is of order A_s (~1e-9). The pump-field zero at '
            'eta -> infinity bounds the effective description at the temporal horizon rather '
            'than invalidating the freeze-out computation.'
        ) % np.log10(min_margin),
    }

    write_csv(step_csv_path(STEP_ID), analysis['per_mode'])
    write_json(step_json_path(STEP_ID), results)

    print_status(f"Step {STEP_ID} completed successfully", "SUCCESS")
    print_status(f"Freeze-out controlled: {controlled}", "INFO")
    print_status(
        f"Min controlled window: {analysis['min_controlled_window_decades']} decades in eta",
        "INFO",
    )
    print_status(
        f"Pivot P_dchi at freeze-out: {analysis['pivot_mode']['P_dchi_at_freeze']}",
        "INFO",
    )

    return results


if __name__ == "__main__":
    run()
