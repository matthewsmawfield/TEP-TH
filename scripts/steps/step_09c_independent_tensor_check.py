#!/usr/bin/env python3
"""Step 09c: Independent verification of the Step 09b tensor quadrature (W2 audit).

Step 09b moved the reported r at the CMB pivot from ~9e-6 (fixed-subdivision
quad on an integrand oscillating ~k_tilde/pi times) to 1.9e-9 (QUADPACK
weighted Filon rule cross-checked against explicit half-period cell
integration).  This step verifies the new integrator with two methods that
share no code path with it:

  (1) mpmath quadosc: arbitrary-precision adaptive oscillatory quadrature
      (Gauss-Legendre on each oscillation with Richardson-type acceleration)
      at dps=40.

  (2) Exact analytic Fourier transform, valid for the n=2 profile:
          V(x) = p [(p+1) x^2 - 1] / (1 + x^2)^2
               = p [(p+1)/(1+x^2) - (p+2)/(1+x^2)^2]
      with
          int_0^inf e^{-i w x}/(1+x^2)   dx = C1 - i S1
          int_0^inf e^{-i w x}/(1+x^2)^2 dx = C2 - i S2
      C1 = (pi/2) e^{-w}
      S1 = (1/2)[e^{-w} Ei(w) - e^{w} Ei(-w)]
      C2 = (pi/4)(1+w) e^{-w}
      S2 = (1/4)[F(w) - w F'(w)],
          F(u) = e^{-u} Ei(u) - e^{u} Ei(-u),
          F'(u) = -[e^{-u} Ei(u) + e^{u} Ei(-u)]

      The analytic formulas are validated against a brute-force
      non-oscillatory mpmath integral at w = 1 before use.

      beta_k = -(i/2 k_tilde) I(2 k_tilde),  I = int V e^{-i w x} dx
      r(k)   = (4 k^3 / pi^2) |beta|^2 / P_zeta(k),   k = k_tilde/eta_0

Checks reported:
  * |beta|^2 at k_tilde in {1.2, 300, 2400, 5000} (the Step 09b self-check
    points) from quadosc and analytic vs the pipeline's Filon/split values.
  * r(k_pivot), k_tilde = 300.
  * r_max over the k grid (transition-scale peak ~ k_tilde ~ 1).
  * r_max for p = 0.5 and p = 1.0 (falsification-surface corners).
  * Truncation sensitivity: split/cell integral truncated at x = 100 vs
    the analytic infinite-domain value.

Output: results/step_09c_independent_tensor_check.json
"""

import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 40

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_DIR.mkdir(exist_ok=True)

P = mp.mpf("0.1")
N = mp.mpf("2.0")
ETA_0_MPC = mp.mpf("6000.0")
A_S = mp.mpf("2.10e-9")
N_S = mp.mpf("0.9649")
K_PIVOT_MPC = mp.mpf("0.05")


def V(x, p=P, n=N):
    xn = x**n
    return p * ((p + 1) * xn - 1) / (1 + xn)**2


def integral_mpmath(kt, p=P):
    """I(w) = int_0^inf V(x) e^{-i w x} dx via mpmath quadosc, w = 2 kt."""
    w = 2 * kt
    f = lambda x: V(x, p) * mp.e**(-1j * w * x)
    return mp.quadosc(f, [0, mp.inf], omega=w)


def _F(u):
    return mp.e**(-u) * mp.ei(u) - mp.e**u * mp.ei(-u)


def _Fp(u):
    return -(mp.e**(-u) * mp.ei(u) + mp.e**u * mp.ei(-u))


def integral_analytic(kt, p=P):
    """Exact closed form for the n=2 profile."""
    w = 2 * kt
    ew = mp.e**(-w)
    C1 = mp.pi / 2 * ew
    S1 = mp.mpf("0.5") * (ew * mp.ei(w) - mp.e**w * mp.ei(-w))
    C2 = mp.pi / 4 * (1 + w) * ew
    S2 = mp.mpf("0.25") * (_F(w) - w * _Fp(w))
    J1 = mp.mpc(C1, -S1)
    J2 = mp.mpc(C2, -S2)
    return p * ((p + 1) * J1 - (p + 2) * J2)


def beta_sq(integral, kt):
    beta = -1j * integral / (2 * kt)
    return abs(beta)**2


def r_of_kt(kt, p=P, method=integral_analytic):
    I = method(kt, p)
    b2 = beta_sq(I, kt)
    k = kt / ETA_0_MPC
    P_T = 4 * k**3 / mp.pi**2 * b2
    P_zeta = A_S * (k / K_PIVOT_MPC)**(N_S - 1)
    return float(P_T / P_zeta), float(b2)


def main():
    out = {"step": "step_09c_independent_tensor_check",
           "parameters": {"p": float(P), "n": float(N),
                          "eta_0_Mpc": float(ETA_0_MPC),
                          "A_s": float(A_S), "n_s": float(N_S)}}

    # --- validate analytic formulas against direct integration at w=1 ---
    w0 = mp.mpf("1.0")
    direct = mp.quad(lambda x: mp.e**(-1j * w0 * x) / (1 + x**2)**2,
                     [0, mp.inf])
    C2 = mp.pi / 4 * (1 + w0) * mp.e**(-w0)
    S2 = mp.mpf("0.25") * (_F(w0) - w0 * _Fp(w0))
    analytic_J2 = mp.mpc(C2, -S2)
    out["analytic_formula_validation"] = {
        "w": 1.0,
        "J2_direct": [float(mp.re(direct)), float(mp.im(direct))],
        "J2_analytic": [float(mp.re(analytic_J2)), float(mp.im(analytic_J2))],
        "rel_err": float(abs(direct - analytic_J2) / abs(direct)),
    }

    # --- the four Step-09b self-check points ---
    pipeline_filon = {1.2: 0.0004118578221904456, 300.0: 7.71631604561036e-14,
                      2400.0: 1.883799713781573e-17,
                      5000.0: 1.0000091265557096e-18}
    pipeline_split = {1.2: 0.0004118229106548708, 300.0: 7.715825644687705e-14,
                      2400.0: 1.8835134850257846e-17,
                      5000.0: 1.000206161483132e-18}
    checks = []
    for kt_s in (1.2, 300.0, 2400.0, 5000.0):
        kt = mp.mpf(kt_s)
        b2_q = beta_sq(integral_mpmath(kt), kt)
        b2_a = beta_sq(integral_analytic(kt), kt)
        checks.append({
            "k_tilde": kt_s,
            "beta_sq_quadosc": float(b2_q),
            "beta_sq_analytic": float(b2_a),
            "beta_sq_pipeline_filon": pipeline_filon[kt_s],
            "beta_sq_pipeline_split": pipeline_split[kt_s],
            "rel_diff_analytic_vs_filon":
                float(abs(b2_a - pipeline_filon[kt_s])
                      / max(abs(b2_a), 1e-300)),
            "rel_diff_quadosc_vs_analytic":
                float(abs(b2_q - b2_a) / max(abs(b2_a), 1e-300)),
        })
    out["beta_sq_checks"] = checks

    # --- r at the CMB pivot (k_tilde = 300) ---
    r_piv_a, b2_piv = r_of_kt(mp.mpf("300.0"))
    r_piv_q, _ = r_of_kt(mp.mpf("300.0"), method=integral_mpmath)
    out["r_at_pivot"] = {
        "analytic": r_piv_a, "quadosc": r_piv_q,
        "pipeline": 1.8614911311895358e-09,
        "manuscript": 1.9e-9,
    }

    # --- r_max scan (p = 0.1): transition-scale peak ---
    import numpy as np
    kts = np.unique(np.concatenate([
        np.logspace(np.log10(0.6), np.log10(10.0), 60),
        np.logspace(np.log10(10.0), np.log10(6000.0), 40)]))
    r_vals = [r_of_kt(mp.mpf(str(k)))[0] for k in kts]
    i_max = int(np.argmax(r_vals))
    out["r_max_p0.1"] = {
        "analytic": float(r_vals[i_max]),
        "k_tilde_at_max": float(kts[i_max]),
        "pipeline": 5.238867813628414e-07,
        "manuscript": 5.2e-7,
    }

    # --- falsification-surface corners: p = 0.5, 1.0 ---
    surface = []
    for p_s in (0.05, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0):
        pv = mp.mpf(str(p_s))
        rv = [r_of_kt(mp.mpf(str(k)), p=pv)[0] for k in kts]
        surface.append({"p": p_s, "r_max_analytic": float(max(rv))})
    out["falsification_surface_analytic"] = surface

    # --- truncation check: analytic (infinite) vs cell-sum truncated x=100
    kt = mp.mpf("300.0")
    w = 2 * kt
    half = mp.pi / w
    edges = [i * half for i in range(int(100 / half) + 1)] + [mp.mpf(100)]
    Itr = mp.mpc(0)
    for a, b in zip(edges[:-1], edges[1:]):
        Itr += mp.quad(lambda x: V(x) * mp.e**(-1j * w * x), [a, b])
    out["truncation_x100"] = {
        "beta_sq_trunc100": float(beta_sq(Itr, kt)),
        "beta_sq_infinite_analytic": float(beta_sq(integral_analytic(kt), kt)),
    }

    out_path = RESULTS_DIR / "step_09c_independent_tensor_check.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(out, indent=1)[:4000])
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
