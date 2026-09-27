#!/usr/bin/env python3
"""Matter-frame curvature on the temporal-horizon profile.

Issue 27-10. The conformal transformation g̃ = A² g gives

    R̃ = A^{-2} R - 6 A^{-3} □A .

A nonzero frozen gravitational-frame Ricci scalar would make R̃ diverge
as A^{-2} wherever A → 0. That is not the horizon solution. The tensor
sector of this paper is the profile whose gravitational metric approaches
the Minkowski vacuum (A''/A → 0 is not assumed; the wave operator
approaches □_η). On that branch R = 0 and

    R̃ = 6 A^{-3} A'' .

For A(η) = [1 + (η/η0)^n ]^{-p/n} this is finite at every finite η, and
for 0 < p ≤ 1/2 it decays as η^{2p-2} at the temporal boundary. The
boundary is therefore regular. A constant nonzero R is computed alongside
as the divergent counterexample the proposition excludes.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from step_09b_native_tensor_integration import (  # noqa: E402
    A_double_prime_over_A,
    A_profile,
)

ETA0 = 6000.0
N_PROF = 2.0


def matter_ricci(eta, p, R_g=0.0):
    """R̃ η0², so the result is dimensionless."""
    A = A_profile(eta, p=p, eta_0=ETA0, n=N_PROF)
    App_over_A = A_double_prime_over_A(eta, p=p, eta_0=ETA0, n=N_PROF)
    # □A = -A'' on the Minkowski gravitational frame in conformal time,
    # so -6 A^{-3} □A = 6 (A''/A) / A².
    conformal = 6.0 * App_over_A / A**2
    frozen = R_g / A**2
    return conformal * ETA0**2, frozen * ETA0**2


def main():
    eta = np.geomspace(1e-3 * ETA0, 1e6 * ETA0, 20000)
    rows = []
    for p in (0.05, 0.1, 0.25, 0.5):
        conf, frozen = matter_ricci(eta, p, R_g=1.0 / ETA0**2)
        # Asymptotic index from the outer decade.
        outer = eta > 1e4 * ETA0
        # |R̃| ~ η^{2p-2}; measure the local slope.
        x = np.log(eta[outer])
        y = np.log(np.maximum(np.abs(conf[outer]), 1e-300))
        slope = float(np.polyfit(x, y, 1)[0])
        rows.append({
            "p": p,
            "Rtilde_eta0sq_max": float(np.max(np.abs(conf))),
            "Rtilde_eta0sq_at_outer_edge": float(conf[-1]),
            "asymptotic_log_slope": slope,
            "expected_slope_2p_minus_2": 2 * p - 2,
            "finite_on_profile": bool(np.all(np.isfinite(conf))),
            "decays_at_boundary": bool(abs(conf[-1]) < abs(conf[np.argmax(np.abs(conf))]) ),
            "frozen_R_over_regular_at_outer_edge": float(abs(frozen[-1]) / max(abs(conf[-1]), 1e-300)),
        })
        if not rows[-1]["finite_on_profile"]:
            raise SystemExit(f"curvature not finite at p={p}")
        if abs(slope - (2 * p - 2)) > 0.05:
            raise SystemExit(f"asymptotic slope {slope} != {2*p-2} at p={p}")
    out = {
        "step": "step_27_10_invariant_divergence",
        "formula": "R~ = A^{-2} R - 6 A^{-3} Box A; horizon branch R=0",
        "profile": "A=(1+(eta/eta0)^n)^{-p/n}",
        "branch": rows,
        "statement": (
            "On the Minkowski-approaching horizon branch the matter-frame "
            "Ricci scalar is finite for every 0<p<=1/2 and decays at the "
            "boundary. A frozen nonzero gravitational-frame R diverges as "
            "A^{-2} and is not this solution."
        ),
    }
    dest = Path(__file__).resolve().parents[2] / "results" / "step_27_10_invariant_divergence.json"
    dest.write_text(json.dumps(out, indent=2))
    print(json.dumps(rows, indent=2))
    print(f"wrote {dest}")


if __name__ == "__main__":
    main()
