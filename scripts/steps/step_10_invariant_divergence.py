#!/usr/bin/env python3
"""Step 10: Nonzero-Background Sensitivity of Proposition 1.

Proposition 1 (matter-frame curvature invariants vanish at the temporal
horizon) is proved on the static, conformally flat background R = 0.
Issue 27-10 asks the quantitative question the proof leaves open: under
the conformal transformation

    R_tilde = A^{-2} [ R - 6 Box(ln A) - 6 (nabla ln A)^2 ],

the gradient terms decay as eta^{2p-2} -> 0 for the horizon profile
A_clock(eta) = C eta^{-p} (0 < p < 1), but the residual-curvature term
A^{-2} R scales as eta^{2p} R and diverges for any fixed nonzero R.

This step computes, rather than asserts, the regularity condition:

  * Parametrise the residual background scalar as R(eta) = R0 eta^{-s}
    (s = 0 is a fixed offset, e.g. a cosmological-constant floor;
    s = 2 corresponds to curvature sourced by the scalar's own
    kinetic energy, since phi ~ ln eta gives phi'^2 ~ eta^{-2}).
  * A^{-2} R ~ R0 eta^{2p-s}: bounded iff s >= 2p, vanishing iff s > 2p.
  * The critical decay rate is therefore s_crit = 2p: background
    curvature must fall toward the horizon at least as fast as eta^{-2p}.

The step evaluates this boundary numerically: for each p it computes the
full invariant R_tilde(eta) under residual-curvature profiles of varying
s and reports where regularity holds, plus the analogous decomposition
for the Kretschmann scalar.  This converts the register's earlier
qualitative claim ("regularity enforces R -> 0") into the precise
condition actually derivable: R must decay faster than eta^{-2p}, i.e.
a fixed background offset is excluded but scalar-sourced curvature
(whose kinetic trace decays as eta^{-2}) satisfies it whenever p < 1.

This is a bounded sensitivity calculation on the proposition's stated
hypothesis space — not a derivation of R = 0 from the master action,
which remains an open item.
"""

from __future__ import annotations

import numpy as np

from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
)

STEP_ID = "step_10_invariant_divergence"

# Horizon profile: A_clock(eta) = C eta^{-p}.  The horizon A -> 0 is at
# eta -> infinity.  C is an overall normalisation (set to 1).
P_VALUES = [0.2, 0.3, 0.4, 0.45, 0.5, 0.75, 0.9]
S_VALUES = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
R0 = 1.0  # fiducial residual-curvature amplitude (units of the
          # background curvature scale; results are in units of R0)


def conformal_ricci_decomposed(eta: np.ndarray, p: float,
                               s: float, r0: float = R0):
    """Decompose the matter-frame Ricci scalar for A = eta^{-p}.

    R_tilde = A^{-2} R  +  R_grad,
    with R(eta) = r0 eta^{-s} the residual background scalar and

        R_grad = -6 A^{-2}[Box ln A + (nabla ln A)^2]
               = -6 p(p+1) C^{-2} eta^{2p-2}      (static, homogeneous)

    which is the term that vanishes as eta^{2p-2} -> 0 (p < 1).

    Returns (residual_term, gradient_term, total).
    """
    eta = np.asarray(eta, dtype=float)
    residual = r0 * eta ** (2.0 * p - s)          # A^{-2} R
    gradient = -6.0 * p * (p + 1.0) * eta ** (2.0 * p - 2.0)
    return residual, gradient, residual + gradient


def kretschmann_residual_scale(eta: np.ndarray, p: float,
                               s: float, r0: float = R0):
    """Leading residual contribution to the Kretschmann scalar.

    For a conformally flat background the Kretschmann scalar inherits
    K_tilde ~ A^{-4} K.  With K ~ R^2 (purely scalar-curvature residual),
    the residual piece scales as r0^2 eta^{4p-2s}, critical at s = 2p.
    """
    eta = np.asarray(eta, dtype=float)
    return r0 ** 2 * eta ** (4.0 * p - 2.0 * s)


def classify(p: float, s: float):
    """Asymptotic class of A^{-2} R ~ eta^{2p-s} as eta -> infinity."""
    exponent = 2.0 * p - s
    if exponent < 0:
        return "vanishes", exponent
    if exponent == 0:
        return "bounded_nonzero", exponent
    return "diverges", exponent


def horizon_crossing(p: float, s: float, r0: float = R0):
    """eta at which |residual| overtakes |gradient| term (if it does).

    |A^{-2}R| = r0 eta^{2p-s};  |R_grad| = 6p(p+1) eta^{2p-2}.
    Ratio = [r0 / (6p(p+1))] eta^{2-s}.
    Crossing eta* solves ratio = 1.
    """
    grad_amp = 6.0 * p * (p + 1.0)
    power = 2.0 - s
    if power == 0:
        return None if r0 <= grad_amp else 0.0
    # ratio = (r0/grad_amp) * eta^power ; crossing when equal to 1
    eta_star = (grad_amp / r0) ** (1.0 / power)
    if power < 0:
        # ratio -> 0: residual NEVER dominates (decays faster)
        return None
    return float(eta_star)


def run():
    logger = TEPLogger(STEP_ID, log_file_path=None)
    set_step_logger(logger)
    ensure_dirs()
    print_status("Step 10: Nonzero-background sensitivity of Proposition 1",
                 "INFO")

    eta_grid = np.logspace(2, 12, 400)   # horizon regime eta >> 1

    classification_grid = []
    csv_rows = []
    for p in P_VALUES:
        for s in S_VALUES:
            cls, exponent = classify(p, s)
            eta_star = horizon_crossing(p, s)
            # Numerical verification at the deep-horizon end
            res, grad, tot = conformal_ricci_decomposed(
                np.array([1e12]), p, s)
            res_at = float(abs(res[0]))
            grad_at = float(abs(grad[0]))
            kres = float(kretschmann_residual_scale(
                np.array([1e12]), p, s)[0])
            classification_grid.append({
                "p": p, "s": s,
                "residual_exponent": exponent,
                "asymptotic_class": cls,
                "horizon_crossing_eta": eta_star,
                "abs_residual_at_eta_1e12": res_at,
                "abs_gradient_at_eta_1e12": grad_at,
                "abs_kretschmann_residual_at_1e12": kres,
            })
        # CSV: invariant profile for representative s values at this p
        for s_probe in (0.0, 1.0, 2.0):
            res, grad, tot = conformal_ricci_decomposed(eta_grid, p, s_probe)
            for i in range(0, len(eta_grid), 40):
                csv_rows.append({
                    "p": p, "s_residual": s_probe,
                    "eta": rounded(float(eta_grid[i]), 4),
                    "residual_term": rounded(float(res[i]), 8),
                    "gradient_term": rounded(float(grad[i]), 8),
                    "R_tilde_total": rounded(float(tot[i]), 8),
                })

    # Critical decay rate summary per p
    critical = [{"p": p, "s_crit": 2.0 * p,
                 "scalar_kinetic_s": 2.0,
                 "kinetic_term_safe": 2.0 > 2.0 * p}
                for p in P_VALUES]

    # Where does a scalar-sourced background sit?  For a canonical scalar
    # phi(eta) = (p M_Pl / |beta_A|) ln eta (from A = exp(beta_A phi/M_pl)
    # = eta^{-p}), the kinetic trace phi'^2 ~ eta^{-2}: s = 2 exactly.
    # Potential-floor contributions (constant V0) would sit at s = 0 and
    # are excluded for every p > 0.
    scalar_sourced = {
        "phi_profile": "phi(eta) = (p M_Pl/|beta_A|) ln eta",
        "kinetic_curvature_decay": "R_kin ~ eta^{-2}  (s = 2)",
        "potential_floor_decay": "R_V ~ const        (s = 0, excluded)",
        "condition": "regularity requires s > 2p, i.e. R must decay "
                     "faster than eta^{-2p} toward the horizon",
    }

    n_div = sum(1 for c in classification_grid
                if c["asymptotic_class"] == "diverges")
    n_van = sum(1 for c in classification_grid
                if c["asymptotic_class"] == "vanishes")

    results = {
        "step": STEP_ID,
        "description": ("Nonzero-background sensitivity of Proposition 1: "
                        "bounded asymptotic classification of the "
                        "A^{-2} R term under R(eta) = R0 eta^{-s}"),
        "motivation_issue": "27-10",
        "model": {
            "horizon_profile": "A_clock(eta) = C eta^{-p} (C = 1)",
            "residual_curvature": "R(eta) = R0 eta^{-s}",
            "transformed_scalar": ("R_tilde = A^{-2}R + R_grad, "
                                   "R_grad = -6p(p+1) eta^{2p-2}"),
            "regularity_condition": "s > 2p for vanishing residual; "
                                    "s = 2p bounded; s < 2p divergent",
        },
        "classification_grid": classification_grid,
        "critical_decay_rates": critical,
        "scalar_sourced_background": scalar_sourced,
        "p_sensitivity_note": (
            "For every p < 1 the scalar's own kinetic-sourced curvature "
            "(s = 2) satisfies s > 2p and the residual vanishes. A fixed "
            "vacuum offset (s = 0) diverges for all p > 0 — the "
            "proposition's R = 0 hypothesis is therefore not merely a "
            "simplification: it is the requirement that the background "
            "carry no non-decaying curvature floor.  For the null-"
            "complete branch 0 < p <= 1/2 the condition is weakest "
            "(s_crit <= 1)."),
        "summary": {
            "n_grid_points": len(classification_grid),
            "n_divergent": n_div,
            "n_vanishing": n_van,
            "derived_condition": "R(eta) must decay faster than "
                                 "eta^{-2p}; equivalently A^{-2} R -> 0",
            "proposition_1_scope": ("holds iff the background Ricci "
                                    "scalar decays faster than "
                                    "eta^{-2p} toward the temporal "
                                    "horizon; a constant offset is "
                                    "excluded for all p > 0"),
        },
        "honesty_note": (
            "This is a bounded sensitivity calculation on the stated "
            "hypothesis space. It does NOT derive R = 0 from the master "
            "action; it converts the earlier qualitative 'regularity "
            "enforces R -> 0' claim into the precise quantitative "
            "condition R = o(eta^{-2p}), and shows scalar-kinetic "
            "curvature (s = 2) satisfies it while a constant floor "
            "(s = 0) does not. Whether the corpus's actual background "
            "solution carries a non-decaying curvature residual remains "
            "to be evaluated against the master-action constraint."),
    }

    write_csv(step_csv_path(STEP_ID), csv_rows)
    write_json(step_json_path(STEP_ID), results)
    print_status(
        f"Classification: {n_van} vanishing / {n_div} divergent of "
        f"{len(classification_grid)} (p, s) cells", "SUCCESS")
    print_status(
        "Critical decay rate s_crit = 2p; scalar-kinetic (s=2) safe for "
        "all p < 1", "INFO")
    return results


if __name__ == "__main__":
    run()
