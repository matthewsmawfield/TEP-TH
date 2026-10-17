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
    # With R = 0 (static background) and □A = -A'' (signature -+++; time derivatives only):
    # R̃ = +6 A^{-3} A''
    # For A(z) = (1+z)^{-1}: A' = -(1+z)^{-2}, A'' = 2(1+z)^{-3}
    # R̃ = +6 (1+z)^3 × 2(1+z)^{-3} = +12 (constant in z for p=1)
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

    In the static conformal background R = 0 and □A_clock = -A_clock''
    (time derivatives only).  For A_clock(η) = C η^{-p}:

        A_clock'' = p(p+1) C η^{-p-2}
        A_clock^{-3} = C^{-3} η^{3p}

        R̃ = +6 × C^{-3} η^{3p} × p(p+1) C η^{-p-2}
          = +6 p(p+1) C^{-2} η^{2p-2}

    which vanishes as η → ∞ for 0 < p < 1.

    The conformal time η is related to redshift by 1+z = C^{-1} η^{p}
    (Eq. 2.10), so η = C^{1/p} (1+z)^{1/p}.  Substituting:

        R̃(z) = +6 p(p+1) C^{-2} [C^{1/p} (1+z)^{1/p}]^{2p-2}
              = +6 p(p+1) C^{-2} C^{(2p-2)/p} (1+z)^{(2p-2)/p}
              = +6 p(p+1) C^{-2/p} (1+z)^{2 - 2/p}

    For p = 1: the conformal de Sitter branch has R̃ = +12/C².
    For p < 1: the exponent 2 - 2/p < 0, so R̃ → 0 as z → ∞.
    """
    z = np.asarray(z, dtype=float)
    # C is fixed by A_clock(z=0) = 1: C = η_0^{p}, and 1+z(η_0) = 1
    # so C = 1 (normalised).  The η-z relation gives η = (1+z)^{1/p}.
    # R̃ = +6 p(p+1) (1+z)^{2 - 2/p}
    exponent = 2.0 - 2.0 / p
    return 6.0 * p * (p + 1.0) * (1.0 + z) ** exponent


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
# Disformal compensation on ds^2=-N^2 deta^2+A^2 dx^2, B<0.
# The declared product is |B phi_prime^2|=A^(-2n), so
# N^2=A^2+A^(-2n) and det=-N^2 A^6 ~ -A^(6-2n).
# The finite determinant exponent is n=3. This does not by itself
# establish a smooth extension of all metric components at the boundary.
# ---------------------------------------------------------------------------

def disformal_determinant(z: np.ndarray, n_power: float) -> np.ndarray:
    """Exact determinant for the declared negative-B product ansatz."""
    A = clock_factor_A(np.asarray(z, dtype=float))
    return -(A**8 + A**(6.0-2.0*n_power))


def disformal_ricci_scalar(z: np.ndarray, n_power: float, p: float = DEFAULT_P) -> np.ndarray:
    """Exact -+++ Ricci scalar of the same A,N metric as the determinant.

    H=A'/(AN), R=6[(H'/N)+2H^2], N^2=A^2+A^(-2n).
    For A=eta^(-p), R scales as eta^(-2-2pn) at the horizon.
    Lapse derivatives alone are not the curvature of this metric.
    """
    z = np.asarray(z, dtype=float)
    A = clock_factor_A(z)
    eta = (1.0+z)**(1.0/p)
    temporal_extra = A**(-2.0*n_power)
    lapse2 = A*A+temporal_extra
    ratio = (A*A-n_power*temporal_extra)/lapse2
    return 6.0*(p+2.0*p*p-p*p*ratio)/(eta*eta*lapse2)


def test_pure_conformal_regularity(z_max: float = 1e6, n_points: int = 10000,
                                    p: float = DEFAULT_P) -> dict:
    """Test Proposition 1: curvature invariants vanish in pure conformal closure.

    Uses the observational clock map A_clock(z) = (1+z)^{-1}, which
    corresponds to A_clock(η) = C η^{-p} with the redshift relation
    1+z = C^{-1} η^{p} (Eq. 2.10 of the manuscript).
    """
    if not np.isfinite(p) or p <= 0:
        raise ValueError('The temporal-horizon family requires finite p>0')
    if not np.isfinite(z_max) or z_max <= 1 or n_points < 2:
        raise ValueError('Require z_max>1 and at least two samples')
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
    # A finite sample falling below a chosen number is not a limit test.
    # The exact positive-p formulas have eta exponents 2p-2 and 4p-4.
    R_vanishing = bool(p < 1.0)
    K_vanishing = bool(p < 1.0)
    endpoint_R_below_reference = bool(np.all(np.abs(R_high_z) < 1e-10)) if len(R_high_z) else None
    endpoint_K_below_reference = bool(np.all(np.abs(K_high_z) < 1e-10)) if len(K_high_z) else None

    # General timelike trajectories have the same bound as null rays.
    # Comoving observers (q=0) are the distinct, less restrictive special case.
    null_complete = p <= 0.5
    timelike_complete = p <= 0.5

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
            'limit_basis': 'Exact eta exponents 2p-2 and 4p-4; independent of finite sampling extent',
            'finite_endpoint_diagnostic': {'z_max': z_max, 'reference_threshold': 1e-10,
                'R_below_reference': endpoint_R_below_reference,
                'K_below_reference': endpoint_K_below_reference},
            'endpoint_values_are_finite_samples': True,
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
            'timelike_bound': 'p <= 1/2 for all conserved momenta',
            'comoving_timelike_complete': p <= 1.0,
            'comoving_timelike_bound': 'p <= 1 for q=0'
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
        'interpretation': ('Proposition 1 verified for this profile: both invariants vanish at the temporal horizon.'
                           if R_vanishing and K_vanishing else
                           'This profile is outside the curvature-vanishing branch: p=1 has constant curvature; p>1 diverges.')
    }

    return results


def test_disformal_compensation(z_max: float = 1e6, n_points: int = 10000,
                                 p: float = DEFAULT_P) -> dict:
    """Evaluate the declared product ansatz on its exact homogeneous metric.

    The determinant and curvature share N^2=A^2+A^(-2n) for B<0.
    Positive B instead has N^2=A^2-C A^(-2n), with a signature boundary.
    A finite coordinate determinant alone is not a smooth-extension theorem.
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
        # det(g̃) ~ A^{6-2n} as A → 0
        det_exponent = 6 - 2 * n_power
        if not det_finite:
            det_status = 'divergent'
        elif det_exponent > 0:
            det_status = f'degenerate (det ~ A^{{{det_exponent}}} → 0)'
        elif det_exponent == 0:
            det_status = 'finite coordinate determinant magnitude; boundary extension not inferred'
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

        # Critical power for a finite coordinate determinant is n=3.
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
            'det_scaling': f'det(g_tilde) ~ A^({6-2*n_power})'
        })

    # Signature analysis: for a homogeneous timelike gradient,
    # (∇φ)^2 = -(phi')^2 < 0, so the signed determinant factor is
    #   1 + B(∇φ)^2 / A^2 = 1 - B(phi')^2 / A^2.
    # Writing the compensation ansatz as |B (phi')^2| = C A^{-2n}:
    #   B > 0: factor = 1 - C A^{-2(n+1)} -> the effective lapse
    #          N~^2 = A^2 - C A^{-2n} vanishes at the surface
    #          A_x = C^{1/(2n+2)} — a signature-change surface at finite
    #          A (inside the domain for C <= 1), beyond which the metric
    #          loses its timelike direction. The growing-
    #          compensation branch with B > 0 terminates at signature
    #          change before any horizon regularization.
    #   B < 0: factor = 1 + C A^{-2(n+1)} > 0 and
    #          N~^2 = A^2 + C A^{-2n} stays positive at finite eta.
    signature_rows = []
    for n_power in power_tests:
        for coeff in (0.1, 1.0, 10.0):
            A_cross = coeff ** (1.0 / (2.0 * n_power + 2.0))
            signature_rows.append({
                'n_power': n_power,
                'coefficient_C': coeff,
                'B_positive_signature_change_at_A': float(A_cross),
                'A_cross_inside_domain': bool(A_cross < 1.0),
                'B_positive_lorentzian_at_A1': bool(coeff < 1.0),
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
                     'while the finite-eta metric remains Lorentzian; a divergent lapse '
                     'alone does not establish a physical pathology.'),
            'crossing_surface_A_x_for_B_positive': signature_rows,
        },
        'critical_power': {
            'n_critical': 3,
            'explanation': 'det(g_tilde) ~ A^{6-2n}; n=3 gives a finite coordinate determinant, not a smooth metric extension.',
            'det_formula': 'det(g_tilde) = -(A^2+A^{-2n}) A^6'
        },
        'power_results': power_results,
        'interpretation': (
            'For the existing negative-B product ansatz, the determinant has '
            'critical power n=3 and exact curvature vanishes as eta^(-2-2pn). '
            'This curvature scalar is invariant, not a coordinate artifact. '
            'The lapse stays positive at finite eta; the positive-B ansatz '
            'instead reaches its stated signature-change surface. '
            'These are metric-level tests of an assigned ansatz, not a derivation '
            'of B(phi), its observational viability, or a smooth extension '
            'of the boundary. The pure conformal completeness branch is unchanged.'
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
                'The pure conformal curvature-regularity certificate is retained. '
                'The negative-B product ansatz has exact positive lapse at finite '
                'eta and bounded curvature, with determinant critical power n=3; '
                'a divergent coordinate lapse is not itself an invariant exclusion. '
                'The positive-B growing ansatz has its stated signature-change '
                'surface. These disformal tests do not derive the coupling from '
                'the common action or establish observational closure.'
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
