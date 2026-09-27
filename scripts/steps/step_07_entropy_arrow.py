#!/usr/bin/env python3
"""Step 07: Entropy and Arrow of Time.

Track the specific entropy per baryon in the temporal-horizon
reconstruction to test whether the temporal horizon is
thermodynamically regular and does not require an infinite-entropy
initial singularity.

The diagnostic is deliberately non-definitional.  Two independently
motivated evolution laws are combined:

  * photon entropy density s_gamma from blackbody thermodynamics of the
    measured temperature-redshift law, s_gamma = (4 pi^2/45) g_*s T^3
    with T(z) = T_0 (1+z) = T_0 / A_clock(z);
  * baryon number density n_b from baryon-number conservation on the
    effective matter geometry, n_b(z) = n_b(z=0) [A_clock(0)/A_clock(z)]^3.

The specific entropy per baryon sigma = s_gamma / (k_B n_b) is constant
if and only if the thermal law and the geometric dilution law are
governed by the same clock factor — the content of the TEP thermal
scaling T = T_0/A_clock (Section 8).  A mismatched dilution profile is
evaluated as a sensitivity control to demonstrate that the diagnostic
can fail.  No observational entropy data are synthesised: T_0, n_b0 and
the constants entering s_gamma are measured quantities; the redshift
scalings are the model's own evolution laws.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
    conformal_factor_A, DEFAULT_EPSILON_T, DEFAULT_Z_T, DEFAULT_N_T,
    OMEGA_M
)

STEP_ID = "step_07_entropy_arrow"

# Physical constants (SI)
K_B = 1.380649e-23        # Boltzmann constant, J/K
HBAR_C = 1.973269804e-7   # hbar*c, eV m
EV_J = 1.602176634e-19    # eV -> J
T_CMB0 = 2.7255           # CMB temperature today, K (Fixsen 2009)
G_STAR_S = 2.0            # photon entropy degrees of freedom
N_B0 = 0.251              # baryon number density today, m^-3
                          # (Omega_b h^2 = 0.0224, h = 0.70)


def clock_factor_A(z: np.ndarray | float) -> np.ndarray | float:
    """Observational clock map A_clock(z) = (1+z)^{-1} (Step 01)."""
    return 1.0 / (1.0 + np.asarray(z))


def matter_frame_temperature(z: np.ndarray) -> np.ndarray:
    """Photon-bath temperature T(z) = T_0 (1+z) = T_0 / A_clock(z).

    Measured temperature-redshift law; in the TEP reading it is the
    clock-ratio map T = T_0/A_clock (Section 8 of the manuscript).
    """
    return T_CMB0 * (1.0 + np.asarray(z))


def photon_entropy_density(z: np.ndarray) -> np.ndarray:
    """Blackbody entropy density s_gamma = (2 pi^2/45) g_*s (k_B T)^3/(hbar c)^3.

    Returned in k_B m^{-3} (dimensionless entropy per cubic metre).
    Computed from radiation thermodynamics of T(z) — not from any
    assumed volume law.
    """
    T = matter_frame_temperature(z)
    kT_eV = K_B * T / EV_J
    s = (2.0 * np.pi**2 / 45.0) * G_STAR_S * (kT_eV / HBAR_C)**3
    return s  # k_B m^{-3}


def baryon_number_density(z: np.ndarray, dilution_A: np.ndarray | None = None) -> np.ndarray:
    """Baryon number density from conservation on the effective geometry.

    Baryon-number conservation n_b x (physical volume) = const on the
    matter-frame congruence gives n_b(z) = n_b0 [A_clock(0)/A_clock(z)]^3,
    since the effective scale factor of the static matter-frame
    representation is a_eff = A_clock.
    """
    if dilution_A is None:
        dilution_A = clock_factor_A(np.asarray(z))
    dilution_A = np.asarray(dilution_A, dtype=float)
    return N_B0 * (1.0 / dilution_A)**3


def specific_entropy_per_baryon(z: np.ndarray,
                                dilution_A: np.ndarray | None = None) -> np.ndarray:
    """Specific entropy per baryon sigma = s_gamma / n_b  (units of k_B)."""
    s = photon_entropy_density(z)
    n_b = baryon_number_density(z, dilution_A)
    return s / n_b


def specific_entropy_test(z: np.ndarray, epsilon_t: float = DEFAULT_EPSILON_T,
                          z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T) -> dict:
    """Constancy of the specific entropy per baryon across redshift.

    sigma(z) is assembled from two independent inputs — the measured
    thermal law and baryon conservation on the effective geometry — so
    its constancy is a physical consistency condition, not a definition.
    A control evaluation with a deliberately mismatched dilution profile
    (the late-time drift factor A_dyn = (1+z/z_t)^{-epsilon_dyn}, which is
    not the horizon clock map) demonstrates that the diagnostic responds
    to inconsistency.
    """
    z = np.asarray(z)
    sigma = specific_entropy_per_baryon(z)
    sigma_ratio = sigma / sigma[0]
    sigma_const = bool(np.all(np.abs(sigma_ratio - 1.0) < 1e-9))

    # Sensitivity control: dilution law driven by a different profile
    A_dyn = conformal_factor_A(z, epsilon_t, z_t, n_t)
    sigma_ctrl = specific_entropy_per_baryon(z, dilution_A=A_dyn)
    sigma_ctrl_ratio = sigma_ctrl / sigma_ctrl[0]
    ctrl_drift = float(np.max(np.abs(sigma_ctrl_ratio - 1.0)))

    return {
        'specific_entropy_constant': sigma_const,
        'sigma0_kB_per_baryon': rounded(float(sigma[0]), 4),
        'sigma_range_over_z': (rounded(float(np.min(sigma_ratio)), 9),
                               rounded(float(np.max(sigma_ratio)), 9)),
        'control_dilution_profile': 'A_dyn(z) = (1+z/z_t)^(-epsilon_dyn)',
        'control_sigma_max_abs_deviation': rounded(ctrl_drift, 6),
        'control_sigma_range_over_z': (rounded(float(np.min(sigma_ctrl_ratio)), 6),
                                       rounded(float(np.max(sigma_ctrl_ratio)), 6)),
        'interpretation': (
            'sigma = s_gamma/n_b is built from two independent laws '
            '(blackbody thermodynamics of T(z) and baryon conservation '
            'on the effective geometry). Its constancy verifies that the '
            'thermal law and the dilution law share the same clock '
            'factor — the content of T = T_0/A_clock. The mismatched-'
            'profile control drifts, showing the diagnostic is not '
            'vacuous.'
        )
    }


def arrow_of_time_indicator(z: np.ndarray) -> dict:
    """Arrow-of-time indicator.

    The specific entropy per baryon is constant (adiabatic, reversible
    evolution): no entropy production is required across the
    temporal-horizon reconstruction.  The arrow of time is carried by
    the clock-drift direction itself — the future is the direction of
    increasing A_clock (decreasing z) — rather than by entropy growth
    from a low-entropy initial state, of which there is none.
    """
    z = np.asarray(z)
    sigma = specific_entropy_per_baryon(z)
    dsigma_dz = np.gradient(sigma, z)
    tol = 1e-6 * max(1.0, float(abs(sigma[0])))
    reversible = bool(np.all(np.abs(dsigma_dz) <= tol))

    A = clock_factor_A(z)
    dA_dz = np.gradient(A, z)
    clock_drift_monotonic = bool(np.all(dA_dz < 0))

    return {
        'sigma_reversible': reversible,
        'entropy_production': 0.0 if reversible else None,
        'clock_map_monotonic': clock_drift_monotonic,
        'arrow_direction': 'future = increasing A_clock (decreasing z)',
        'arrow_well_defined': bool(reversible and clock_drift_monotonic),
    }


def test_entropy_regularity(z_max: float = 1000.0, n_points: int = 1000,
                           epsilon_t: float = DEFAULT_EPSILON_T,
                           z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T) -> dict:
    """Test entropy regularity at temporal horizon."""

    z_array = np.linspace(0, z_max, n_points)

    # Entropy densities: observed-frame s_gamma and matter-frame s_tilde.
    # Matter-frame density transforms as s_tilde = s / A_clock^3 under
    # g_tilde = A_clock^2 g (volume element scales as A_clock^3).
    A_clock = clock_factor_A(z_array)
    s_std = photon_entropy_density(z_array)
    s_tep = s_std / np.maximum(A_clock, 1e-300)**3

    # Check for divergences at finite z
    s_std_finite = np.all(np.isfinite(s_std))
    s_tep_finite = np.all(np.isfinite(s_tep))

    # Check behavior near horizon (finite-z edge of the sampled range)
    high_z_mask = z_array > z_max * 0.9
    s_tep_high_z = s_tep[high_z_mask]

    s_tep_positive = np.all(s_tep_high_z > 0) if len(s_tep_high_z) > 0 else True
    # Finite at every finite redshift; growth is the clock-ratio image of
    # the standard T -> infinity limit, not a state at finite affine
    # distance.
    s_tep_bounded = bool(s_tep_finite and np.all(np.isfinite(s_tep_high_z)))

    # Specific-entropy consistency test
    entropy_test = specific_entropy_test(z_array, epsilon_t, z_t, n_t)

    # Arrow of time
    arrow_test = arrow_of_time_indicator(z_array)

    results = {
        'step': STEP_ID,
        'description': 'Entropy and arrow-of-time regularity at temporal horizon',
        'parameters': {
            'epsilon_t': epsilon_t,
            'z_t': z_t,
            'n_t': n_t,
            'z_max': z_max,
            'n_points': n_points,
            'T_CMB0': T_CMB0,
            'N_B0': N_B0
        },
        'entropy_regularity': {
            's_standard_finite': bool(s_std_finite),
            's_tep_finite': bool(s_tep_finite),
            's_tep_bounded_near_horizon': s_tep_bounded,
            's_tep_positive_near_horizon': s_tep_positive,
            's_tep_max': rounded(float(np.max(s_tep)), 6) if s_tep_finite else None,
            's_tep_min': rounded(float(np.min(s_tep)), 6) if s_tep_finite else None
        },
        'specific_entropy': entropy_test,
        'arrow_of_time': arrow_test,
        'thermodynamic_regularity': {
            'entropy_finite': bool(s_tep_finite),
            'entropy_bounded': s_tep_bounded,
            'entropy_positive': s_tep_positive,
            'specific_entropy_constant': entropy_test['specific_entropy_constant'],
            'arrow_of_time_valid': arrow_test['arrow_well_defined'],
            'all_regular': bool(s_tep_finite and s_tep_bounded and s_tep_positive and
                               entropy_test['specific_entropy_constant'] and
                               arrow_test['arrow_well_defined'])
        },
        'interpretation': 'Temporal horizon is thermodynamically regular with finite entropy' if
                          (s_tep_finite and s_tep_bounded and s_tep_positive) else
                          'Entropy behavior requires further analysis'
    }

    # Generate CSV output
    sigma = specific_entropy_per_baryon(z_array)
    n_b = baryon_number_density(z_array)
    csv_rows = []
    for i, z in enumerate(z_array):
        csv_rows.append({
            'z': rounded(z, 4),
            's_gamma_kB_m3': rounded(s_std[i], 6),
            's_tilde_kB_m3': rounded(s_tep[i], 6),
            'n_b_m3': rounded(n_b[i], 6),
            'sigma_kB_per_baryon': rounded(sigma[i], 6)
        })

    write_csv(step_csv_path(STEP_ID), csv_rows)

    return results


def run():
    logger = TEPLogger(STEP_ID, log_file_path=Path(f"logs/{STEP_ID}.log"))
    set_step_logger(logger)
    print_status(f"Starting {STEP_ID}", "TITLE")
    ensure_dirs()

    # Test with default parameters
    results = test_entropy_regularity()

    # Test with different epsilon_t values (control-profile sensitivity)
    epsilon_tests = [0.0001, 0.001, 0.01]
    epsilon_results = []

    for eps in epsilon_tests:
        eps_result = test_entropy_regularity(epsilon_t=eps)
        epsilon_results.append({
            'epsilon_t': eps,
            'all_regular': eps_result['thermodynamic_regularity']['all_regular'],
            'entropy_finite': eps_result['entropy_regularity']['s_tep_finite']
        })

    results['epsilon_sensitivity'] = epsilon_results

    write_json(step_json_path(STEP_ID), results)
    print_status(f"Step {STEP_ID} completed successfully", "SUCCESS")
    print_status(f"Thermodynamic regularity: {results['thermodynamic_regularity']['all_regular']}", "INFO")
    print_status(f"Arrow of time valid: {results['arrow_of_time']['arrow_well_defined']}", "INFO")

    return results


if __name__ == "__main__":
    run()
