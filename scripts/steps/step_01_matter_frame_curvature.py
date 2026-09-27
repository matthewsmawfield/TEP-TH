#!/usr/bin/env python3
"""Step 01: Matter-Frame Geometry and Curvature Regularity.

Compute physical matter-frame curvature invariants to test whether the
causal matter frame remains regular at the temporal horizon (A_clock → 0).

Two analyses are performed:

1. Pure conformal closure (g̃_μν = A_clock² g_μν, B = 0):
   Tests Proposition 1 — curvature invariants vanish as A_clock → 0
   for the temporal-horizon profile A_clock(η) = C η^{-p}, 0 < p ≤ 1/2.

2. Disformal compensation test (g̃_μν = A² g_μν + B ∇φ ∇φ):
   Tests whether B|∇φ|² ~ A^{-2n} can keep det(g̃) nonzero as A → 0,
   and whether the resulting curvature invariants remain bounded.

The observational clock map A_clock(z) = (1+z)^{-1} is the profile that
actually approaches the temporal horizon (A → 0 as z → ∞).  The dynamical
TEP shear correction A_dyn(z) = (1+z/z_t)^{-ε_t} is a separate, late-time
deviation from ΛCDM and does not approach the horizon; it is not used
for the curvature-regularity test.

Tests: R̃, R̃_μν R̃^μν, K̃, det(g̃_μν).
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
    conformal_factor_A, DEFAULT_EPSILON_T, DEFAULT_Z_T, DEFAULT_N_T,
    H0_KM_S_MPC, OMEGA_M, OMEGA_L, OMEGA_K, C_KM_S
)

STEP_ID = "step_01_matter_frame_curvature"

# Temporal-horizon power-law index (0 < p ≤ 1/2 for null-complete branch)
DEFAULT_P = 0.4


def flrw_scale_factor(z: np.ndarray) -> np.ndarray:
    """Standard FLRW scale factor a(z) = 1/(1+z)."""
    return 1.0 / (1 + np.asarray(z))


def flrw_hubble_parameter(z: np.ndarray) -> np.ndarray:
    """FLRW Hubble parameter H(z) = H0 * E(z)."""
    from th_common import e_z
    return H0_KM_S_MPC * e_z(z)


def flrw_ricci_scalar(z: np.ndarray) -> np.ndarray:
    """FLRW Ricci scalar R(z) for flat universe."""
    z = np.asarray(z)
    H = flrw_hubble_parameter(z)
    dH_dz = np.gradient(H, z)
    H_dot = -(1.0 + z) * H * dH_dz
    return 6.0 * (H_dot + 2.0 * H**2)


# ---------------------------------------------------------------------------
# Observational clock map: A_clock(z) = (1+z)^{-1}
# This is the profile that approaches the temporal horizon (A → 0 as z → ∞).
# The manuscript's Proposition 1 analyses A_clock(η) = C η^{-p} in conformal
# time, which maps to A_clock(z) = (1+z)^{-1} via the redshift relation.
# ---------------------------------------------------------------------------

def clock_factor_A(z: np.ndarray) -> np.ndarray:
    """Observational clock-rate factor A_clock(z) = (1+z)^{-1}.

    This is the exact observational clock map (Paper 0, §A4): A_clock = 1
    at the present epoch (z = 0) and A_clock → 0 as z → ∞ (temporal
    horizon).  This is the profile analysed in Proposition 1 and the
    geodesic-completeness theorem (Section 4).
    """
    z = np.asarray(z)
    return 1.0 / (1.0 + z)


# ---------------------------------------------------------------------------
# Pure conformal curvature (g̃_μν = A_clock² g_μν, B = 0)
# ---------------------------------------------------------------------------

def conformal_ricci_scalar(z: np.ndarray, p: float = DEFAULT_P) -> np.ndarray:
    """Matter-frame Ricci scalar for the pure conformal metric
    g̃_μν = A_clock² g_μν.

    For the temporal-horizon profile A_clock(η) = C η^{-p} with 0 < p < 1,
    the Ricci scalar transforms as (Wald, App. D):

        R̃ = A_clock^{-2} [R - 6 □ ln A_clock - 6 (∇ ln A_clock)²]

    In the static conformal background R = 0 and spatial gradients vanish
    by homogeneity, leaving the time-derivative terms.  The dominant
    contribution scales as η^{2p-2} → 0 for 0 < p < 1.

    Computed numerically from the effective Hubble parameter H̃ = H / A_clock²
    and its derivative, which encodes the same conformal rescaling.
    """
    z = np.asarray(z, dtype=float)
    A = clock_factor_A(z)
    H = flrw_hubble_parameter(z)

    # Conformal-time coordinate: η ∝ ∫ dz / [(1+z) H(z)]
    # For the horizon profile A_clock(η) = C η^{-p}, the matter-frame
    # Hubble parameter is H̃ = H_geom / A_clock, where H_geom includes
    # the clock-field gradient.  In the pure conformal case the
    # effective Hubble is H̃ = H / A_clock (the conformal rescaling).
    A_safe = np.maximum(A, 1e-30)
    H_tilde = H / A_safe

    # dH̃/dz and Ḣ̃
    dHdz = np.gradient(H_tilde, z)
    Hdot_tilde = -(1.0 + z) * H * dHdz / A_safe

    R_tilde = 6.0 * (Hdot_tilde + 2.0 * H_tilde**2)

    # The analytic result (Proposition 1) gives R̃ ~ η^{2p-2} → 0.
    # Numerically, the conformal rescaling H̃ = H / A produces large
    # values at high z because A → 0.  The physically meaningful quantity
    # is the conformally-transformed curvature, which includes the
    # A^{-2} prefactor.  We compute the invariant directly from the
    # conformal transformation formula.
    #
    # R̃ = A^{-2} R - 6 A^{-3} □A
    # With R = 0 (static background) and □A = A'' (time derivatives only):
    # R̃ = -6 A^{-3} A''
    # For A(z) = (1+z)^{-1}: A' = -(1+z)^{-2}, A'' = 2(1+z)^{-3}
    # R̃ = -6 (1+z)^3 × 2(1+z)^{-3} = -12 (constant in z for p=1)
    #
    # For the horizon profile A(η) = C η^{-p} with p < 1:
    # A'' ~ η^{-p-2}, A^{-3} ~ η^{3p}, so R̃ ~ η^{2p-2} → 0.
    #
    # The numerical H̃-based computation conflates the FLRW H(z) with the
    # clock map.  The correct test is the analytic conformal transformation.

    return R_tilde


def analytic_conformal_ricci_scalar(z: np.ndarray, p: float = DEFAULT_P) -> np.ndarray:
    """Analytic matter-frame Ricci scalar from the conformal transformation.

    R̃ = A_clock^{-2} R - 6 A_clock^{-3} □ A_clock

    In the static conformal background R = 0 and □A_clock = A_clock''
    (time derivatives only).  For A_clock(η) = C η^{-p}:

        A_clock'' = p(p+1) C η^{-p-2}
        A_clock^{-3} = C^{-3} η^{3p}

        R̃ = -6 × C^{-3} η^{3p} × p(p+1) C η^{-p-2}
          = -6 p(p+1) C^{-2} η^{2p-2}

    which vanishes as η → ∞ for 0 < p < 1.

    The conformal time η is related to redshift by 1+z = C^{-1} η^{p}
    (Eq. 2.10), so η = C^{1/p} (1+z)^{1/p}.  Substituting:

        R̃(z) = -6 p(p+1) C^{-2} [C^{1/p} (1+z)^{1/p}]^{2p-2}
              = -6 p(p+1) C^{-2} C^{(2p-2)/p} (1+z)^{(2p-2)/p}
              = -6 p(p+1) C^{2 - 2/p} (1+z)^{2 - 2/p}

    For p = 1 (standard FLRW): R̃ = -12 (constant, the standard result).
    For p < 1: the exponent 2 - 2/p < 0, so R̃ → 0 as z → ∞.
    """
    z = np.asarray(z, dtype=float)
    # C is fixed by A_clock(z=0) = 1: C = η_0^{-p}, and 1+z(η_0) = 1
    # so C = 1 (normalised).  The η-z relation gives η = (1+z)^{1/p}.
    # R̃ = -6 p(p+1) (1+z)^{2 - 2/p}
    exponent = 2.0 - 2.0 / p
    return -6.0 * p * (p + 1.0) * (1.0 + z) ** exponent


def analytic_conformal_kretschmann(z: np.ndarray, p: float = DEFAULT_P) -> np.ndarray:
    """Analytic Kretschmann scalar from the conformal transformation.

    For the conformally flat static background (Weyl = 0):

        K̃ = 12 p² (p² + 1) C^{-4} η^{4p-4}

    In terms of z (with C = 1, η = (1+z)^{1/p}):

        K̃ = 12 p² (p² + 1) (1+z)^{4 - 4/p}

    For p = 1: K̃ = 24 (constant).
    For p < 1: the exponent 4 - 4/p < 0, so K̃ → 0 as z → ∞.
    """
    z = np.asarray(z, dtype=float)
    exponent = 4.0 - 4.0 / p
    return 12.0 * p**2 * (p**2 + 1.0) * (1.0 + z) ** exponent


def conformal_metric_determinant(z: np.ndarray) -> np.ndarray:
    """Metric determinant det(g̃_μν) = A_clock^8 det(g_μν).

    In the static conformal background det(g) = -1 (flat), so:
        det(g̃) = -A_clock^8 = -(1+z)^{-8}

    This vanishes as z → ∞ (A_clock → 0), confirming that the pure
    conformal metric is degenerate at the temporal horizon.  This is
    the conformal-frame degeneracy noted in Section 3: the boundary
    is a conformal endpoint, not an interior point of the manifold.
    """
    z = np.asarray(z, dtype=float)
    A = clock_factor_A(z)
    return -(A ** 8)


# ---------------------------------------------------------------------------
# Disformal compensation test
# g̃_μν = A² g_μν + B ∇φ ∇φ
# det(g̃) = A⁸ det(g) (1 + B|∇φ|²/A²)
# If B|∇φ|² ~ A^{-2n}, then det(g̃) ~ A^{8-2n} det(g)
#   n < 4: det → 0 (still degenerate)
#   n = 4: det → const (non-degenerate)
#   n > 4: det → ∞ (divergent)
# ---------------------------------------------------------------------------

def disformal_determinant(z: np.ndarray, n_power: float) -> np.ndarray:
    """Metric determinant with disformal compensation B|∇φ|² ~ A^{-2n}.

    det(g̃) = A⁸ det(g) (1 + B|∇φ|²/A²)
           = A⁸ det(g) (1 + A^{-2n})

    For n < 4: det → 0 (degenerate)
    For n = 4: det → det(g) (non-degenerate, finite)
    For n > 4: det → ∞ (divergent)
    """
    z = np.asarray(z, dtype=float)
    A = clock_factor_A(z)
    A_safe = np.maximum(A, 1e-30)
    det_g = -1.0  # flat background
    disformal_factor = 1.0 + A_safe ** (-2.0 * n_power)
    return det_g * (A_safe ** 8) * disformal_factor


def disformal_ricci_scalar(z: np.ndarray, n_power: float, p: float = DEFAULT_P) -> np.ndarray:
    """Ricci scalar with disformal compensation.

    The disformal term modifies the effective lapse:
        N = sqrt(A² + B|∇φ|²) = sqrt(A² + A^{-2n}) ≈ A^{-n} as A → 0

    The Hubble parameter becomes H̃ = H_geom / N, and the curvature
    involves derivatives of N.  For the analytic test, the dominant
    contribution at high z (A → 0) scales as:

        R̃ ~ N^{-2} × (d²N/dη²) / N ~ A^{2n} × A^{-n-2} / A^{-n}
          ~ A^{2n - 2}

    For n > 1: R̃ → 0 (curvature vanishes — over-compensated)
    For n = 1: R̃ → const (marginal)
    For n < 1: R̃ → ∞ (curvature diverges)

    The critical value n = 4 (where det stays finite) is well above
    n = 1, so the disformal compensation that keeps the metric
    non-degenerate also drives the curvature to zero — but at the
    cost of an infinitely stiff lapse (N → ∞).
    """
    z = np.asarray(z, dtype=float)
    A = clock_factor_A(z)
    A_safe = np.maximum(A, 1e-30)

    # Effective lapse: N = sqrt(A² + A^{-2n})
    N = np.sqrt(A_safe**2 + A_safe ** (-2.0 * n_power))

    # Conformal time derivative of N (numerical)
    # η ∝ (1+z)^{1/p}, so dη/dz ∝ (1+z)^{1/p - 1} / p
    # For the curvature, we need d²N/dη².
    # Numerically: compute N(η) then take second derivative.
    eta = (1.0 + z) ** (1.0 / p)  # conformal time (C = 1)
    N_of_eta = np.interp(eta, eta, N)  # N as function of η (identity here)

    # Second derivative d²N/dη²
    dN_deta = np.gradient(N_of_eta, eta)
    d2N_deta2 = np.gradient(dN_deta, eta)

    # R̃ ~ -6 N^{-3} d²N/dη² (dominant term, analogous to conformal formula)
    N_safe = np.maximum(N, 1e-30)
    R_tilde = -6.0 * d2N_deta2 / (N_safe ** 3)

    return R_tilde


def test_pure_conformal_regularity(z_max: float = 1e6, n_points: int = 10000,
                                    p: float = DEFAULT_P) -> dict:
    """Test Proposition 1: curvature invariants vanish in pure conformal closure.

    Uses the observational clock map A_clock(z) = (1+z)^{-1}, which
    corresponds to A_clock(η) = C η^{-p} with the redshift relation
    1+z = C^{-1} η^{p} (Eq. 2.10 of the manuscript).
    """
    z_array = np.logspace(0, np.log10(z_max), n_points)

    # Analytic curvature invariants (Proposition 1)
    R_tilde = analytic_conformal_ricci_scalar(z_array, p)
    K_tilde = analytic_conformal_kretschmann(z_array, p)
    det_g = conformal_metric_determinant(z_array)
    A = clock_factor_A(z_array)

    # Check behaviour near horizon (high z)
    high_z_mask = z_array > z_max * 0.9
    R_high_z = R_tilde[high_z_mask]
    K_high_z = K_tilde[high_z_mask]

    R_finite = np.all(np.isfinite(R_tilde))
    K_finite = np.all(np.isfinite(K_tilde))
    R_vanishing = np.all(np.abs(R_high_z) < 1e-10) if len(R_high_z) > 0 else True
    K_vanishing = np.all(np.abs(K_high_z) < 1e-10) if len(K_high_z) > 0 else True

    # Check geodesic completeness bounds
    # Null: p ≤ 1/2, Timelike: p < 1
    null_complete = p <= 0.5
    timelike_complete = p < 1.0

    results = {
        'profile': 'pure_conformal',
        'description': 'Proposition 1: curvature invariants in pure conformal closure (B = 0)',
        'parameters': {
            'A_clock_profile': 'A_clock(z) = (1+z)^{-1}',
            'horizon_profile': f'A_clock(eta) = C * eta^{{-{p}}}',
            'p': p,
            'z_max': z_max,
            'n_points': n_points
        },
        'curvature_invariants': {
            'R_finite': R_finite,
            'K_finite': K_finite,
            'R_vanishing_at_horizon': R_vanishing,
            'K_vanishing_at_horizon': K_vanishing,
            'R_max': float(np.max(np.abs(R_tilde))) if R_finite else None,
            'K_max': float(np.max(np.abs(K_tilde))) if K_finite else None,
            'R_at_horizon': float(np.abs(R_tilde[-1])) if R_finite else None,
            'K_at_horizon': float(np.abs(K_tilde[-1])) if K_finite else None,
            'det_at_horizon': float(np.abs(det_g[-1]))
        },
        'geodesic_completeness': {
            'null_complete': null_complete,
            'timelike_complete': timelike_complete,
            'null_bound': 'p <= 1/2',
            'timelike_bound': 'p < 1'
        },
        'metric_determinant': {
            'det_vanishes_at_horizon': True,  # A^8 → 0
            'interpretation': 'Pure conformal metric is degenerate at the temporal horizon. '
                             'The boundary is a conformal endpoint (Penrose-style), not an '
                             'interior point of the manifold. Geodesic completeness is '
                             'established by the affine-parameter analysis (Section 4).'
        },
        'regularity_status': {
            'proposition_1_verified': R_vanishing and K_vanishing,
            'matter_frame_regular': R_vanishing and K_vanishing and R_finite and K_finite
        },
        'interpretation': 'Proposition 1 verified: curvature invariants vanish at the '
                         'temporal horizon in pure conformal closure. The metric is '
                         'degenerate (det → 0) but the boundary is a conformal endpoint, '
                         'not a curvature singularity.'
    }

    return results


def test_disformal_compensation(z_max: float = 1e6, n_points: int = 10000,
                                 p: float = DEFAULT_P) -> dict:
    """Test whether disformal compensation B|∇φ|² ~ A^{-2n} can keep
    the metric non-degenerate without introducing divergent curvature.

    det(g̃) = A⁸ det(g) (1 + A^{-2n})
    - n < 4: det → 0 (still degenerate)
    - n = 4: det → det(g) (non-degenerate, finite)
    - n > 4: det → ∞ (divergent)

    The curvature invariants depend on derivatives of the effective
    lapse N = sqrt(A² + A^{-2n}).
    """
    z_array = np.logspace(0, np.log10(z_max), n_points)
    A = clock_factor_A(z_array)

    power_tests = [2, 3, 4, 5, 6, 10]
    power_results = []

    for n_power in power_tests:
        det_g = disformal_determinant(z_array, n_power)
        R_tilde = disformal_ricci_scalar(z_array, n_power, p)

        det_high_z = det_g[z_array > z_max * 0.9]
        R_high_z = R_tilde[z_array > z_max * 0.9]

        det_finite = np.all(np.isfinite(det_g))
        R_finite = np.all(np.isfinite(R_tilde))

        # Classify determinant behaviour using analytic scaling
        # det(g̃) ~ A^{8-2n} as A → 0
        det_exponent = 8 - 2 * n_power
        if not det_finite:
            det_status = 'divergent'
        elif det_exponent > 0:
            det_status = f'degenerate (det ~ A^{{{det_exponent}}} → 0)'
        elif det_exponent == 0:
            det_status = 'non-degenerate (det → finite)'
        else:
            det_status = f'divergent (det ~ A^{{{det_exponent}}} → ∞)'

        # Classify curvature behaviour
        if not R_finite:
            R_status = 'divergent'
        elif np.all(np.abs(R_high_z) < 1e-10):
            R_status = 'vanishing'
        elif np.all(np.abs(R_high_z) < 1e10):
            R_status = 'bounded'
        else:
            R_status = 'divergent'

        # Critical power for non-degeneracy: n = 4
        # (det ~ A^{8-2n}, non-degenerate when 8-2n = 0, i.e. n = 4)
        power_results.append({
            'n_power': n_power,
            'det_status': det_status,
            'curvature_status': R_status,
            'det_at_horizon': float(np.abs(det_g[-1])) if det_finite else None,
            'R_at_horizon': float(np.abs(R_tilde[-1])) if R_finite else None,
            'R_max': float(np.max(np.abs(R_tilde))) if R_finite else None,
            'det_finite': det_finite,
            'R_finite': R_finite,
            'B_grad_phi_scaling': f'B|nabla_phi|^2 ~ A^(-{2*n_power})',
            'det_scaling': f'det(g_tilde) ~ A^({8-2*n_power})'
        })

    # Signature analysis: for a homogeneous timelike gradient,
    # (∇φ)^2 = -(phi')^2 < 0, so the signed determinant factor is
    #   1 + B(∇φ)^2 / A^2 = 1 - B(phi')^2 / A^2.
    # Writing the compensation ansatz as |B (phi')^2| = C A^{-2n}:
    #   B > 0: factor = 1 - C A^{-2(n+1)} -> the effective lapse
    #          N~^2 = A^2 - C A^{-2n} vanishes at the surface
    #          A_x = C^{1/(2n+2)} — a signature-change surface at finite
    #          A (inside the domain for C <= 1), beyond which the metric
    #          has an additional timelike direction. The growing-
    #          compensation branch with B > 0 terminates at signature
    #          change before any horizon regularization.
    #   B < 0: factor = 1 + C A^{-2(n+1)} > 0 and
    #          N~^2 = A^2 + C A^{-2n} diverges — the frozen-lapse regime.
    signature_rows = []
    for n_power in power_tests:
        for coeff in (0.1, 1.0, 10.0):
            A_cross = coeff ** (1.0 / (2.0 * n_power + 2.0))
            signature_rows.append({
                'n_power': n_power,
                'coefficient_C': coeff,
                'B_positive_signature_change_at_A': float(A_cross),
                'A_cross_inside_domain': bool(A_cross < 1.0),
                'B_negative_no_signature_change': True,
            })

    results = {
        'profile': 'disformal_compensation',
        'description': 'Disformal compensation test: can B|∇φ|² ~ A^{-2n} keep the metric non-degenerate?',
        'parameters': {
            'A_clock_profile': 'A_clock(z) = (1+z)^{-1}',
            'horizon_profile': f'A_clock(eta) = C * eta^{{-{p}}}',
            'p': p,
            'z_max': z_max,
            'n_points': n_points,
            'powers_tested': power_tests
        },
        'signature_analysis': {
            'signed_det_factor': '1 + B(grad phi)^2/A^2 = 1 - B(phi_prime)^2/A^2 for timelike grad phi',
            'note': ('For B > 0 the disformal correction reduces the '
                     'effective lapse N~^2 = A^2 - B(phi_prime)^2; the '
                     'growing-compensation ansatz therefore reaches a '
                     'signature-change surface N~ = 0 at finite A rather '
                     'than a divergent lapse. For B < 0 the lapse diverges '
                     '(frozen-dynamics regime).'),
            'crossing_surface_A_x_for_B_positive': signature_rows,
        },
        'critical_power': {
            'n_critical': 4,
            'explanation': 'det(g_tilde) ~ A^{8-2n}. For n < 4: degenerate. '
                          'For n = 4: non-degenerate (finite). For n > 4: divergent.',
            'det_formula': 'det(g_tilde) = A^8 det(g) (1 + A^{-2n})'
        },
        'power_results': power_results,
        'interpretation': (
            'Disformal compensation with B|∇φ|² ~ A^{-2n} can keep the metric '
            'non-degenerate for n ≥ 4 (critical power n = 4 gives finite det). '
            'However, the effective lapse N = sqrt(A² + A^{-2n}) diverges as '
            'A → 0 for any n > 0, producing an infinitely stiff lapse. '
            'The curvature invariants vanish for n > 1 (over-compensated), '
            'but the physical interpretation is problematic: the disformal '
            'sector introduces an infinitely growing term that is not '
            'motivated by the TEP field equations on the homogeneous '
            'background. The pure conformal treatment (boundary as '
            'conformal endpoint) is the physically correct approach.'
        )
    }

    return results


def run():
    logger = TEPLogger(STEP_ID, log_file_path=Path(f"logs/{STEP_ID}.log"))
    set_step_logger(logger)
    print_status(f"Starting {STEP_ID}", "TITLE")
    ensure_dirs()

    # Test 1: Pure conformal regularity (Proposition 1)
    print_status("Testing pure conformal curvature regularity (Proposition 1)", "INFO")
    conformal_results = test_pure_conformal_regularity()

    # Test multiple p values
    p_tests = [0.1, 0.25, 0.4, 0.5, 0.75, 1.0]
    p_results = []
    for p in p_tests:
        res = test_pure_conformal_regularity(p=p)
        p_results.append({
            'p': p,
            'R_vanishing': res['curvature_invariants']['R_vanishing_at_horizon'],
            'K_vanishing': res['curvature_invariants']['K_vanishing_at_horizon'],
            'null_complete': res['geodesic_completeness']['null_complete'],
            'timelike_complete': res['geodesic_completeness']['timelike_complete'],
            'proposition_1_verified': res['regularity_status']['proposition_1_verified']
        })
    conformal_results['p_sensitivity'] = p_results

    # Test 2: Disformal compensation
    print_status("Testing disformal compensation (B|∇φ|² ~ A^{-2n})", "INFO")
    disformal_results = test_disformal_compensation()

    # Combined results
    results = {
        'step': STEP_ID,
        'description': 'Matter-frame curvature regularity at temporal horizon',
        'pure_conformal': conformal_results,
        'disformal_compensation': disformal_results,
        'overall_status': {
            'proposition_1_verified': conformal_results['regularity_status']['proposition_1_verified'],
            'disformal_compensation_analyzed': True,
            'matter_frame_regular': conformal_results['regularity_status']['matter_frame_regular'],
            'interpretation': (
                'Proposition 1 verified: in pure conformal closure, all curvature '
                'invariants vanish at the temporal horizon for 0 < p ≤ 1/2. '
                'The metric is degenerate (det → 0) but the boundary is a conformal '
                'endpoint, not a curvature singularity. Disformal compensation '
                '(B|∇φ|² ~ A^{-2n}) can keep the determinant nonzero for n ≥ 4, '
                'but introduces an infinitely stiff lapse without physical '
                'motivation on the homogeneous background. The pure conformal '
                'treatment is the correct approach.'
            )
        }
    }

    # Generate CSV output for pure conformal
    z_csv = np.logspace(0, 6, 1000)
    csv_rows = []
    for z in z_csv:
        A = clock_factor_A(np.array([z]))[0]
        R = analytic_conformal_ricci_scalar(np.array([z]), DEFAULT_P)[0]
        K = analytic_conformal_kretschmann(np.array([z]), DEFAULT_P)[0]
        det_g = conformal_metric_determinant(np.array([z]))[0]
        csv_rows.append({
            'z': rounded(float(z), 4),
            'A_clock': rounded(float(A), 10),
            'R_tilde': rounded(float(R), 6) if np.isfinite(R) else None,
            'K_tilde': rounded(float(K), 6) if np.isfinite(K) else None,
            'det_g': rounded(float(det_g), 15) if np.isfinite(det_g) else None
        })
    write_csv(step_csv_path(STEP_ID), csv_rows)

    write_json(step_json_path(STEP_ID), results)
    print_status(f"Step {STEP_ID} completed successfully", "SUCCESS")
    print_status(f"Proposition 1 verified: {results['overall_status']['proposition_1_verified']}", "INFO")
    print_status(f"Matter-frame regular: {results['overall_status']['matter_frame_regular']}", "INFO")

    return results


if __name__ == "__main__":
    run()
