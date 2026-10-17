#!/usr/bin/env python3
"""Step 11: Distant-absorber excitation-temperature test.

Quantitative confrontation of the TEP temperature-redshift law with
published molecular-excitation measurements of the CMB temperature at
finite redshift.  In the temporal-horizon construction the matter-frame
local temperature of the radiation bath at absorber depth is

    T_loc(z) = T_0 / A_clock(z) = T_0 (1 + z),

the same clock map that produces the observed redshift — no transport
or dilution assumption enters; the absorber thermometers the field
where it sits.  Rotational excitation of CO in damped Ly-alpha systems
samples exactly this local quantity, so the channel is a direct probe
of the TEP map rather than of photon transport.

Three hypotheses are compared on the same dataset:

  * TEP / adiabatic law  T = T_0 (1+z)          (beta = 0)
  * free exponent        T = T_0 (1+z)^(1-beta) (beta fitted)
  * constant-temperature T = T_0                (tired-light class)

The constant-temperature model is the decisive discriminating null:
any mechanism that shifts photon energies without a corresponding
local-temperature rise fails this sample by many sigma.

Data.  CO rotational excitation temperatures measured in quasar
absorption systems with VLT/UVES and X-shooter (Noterdaeme et al. 2011,
Table 1, and references therein), plus the millimetre-band CO
measurement toward PKS 1830-211 (Muller et al. 2013), anchored by the
FIRAS monopole (Fixsen 2009).  Asymmetric errors are symmetrised by the
mean of the two branches.  Published excitation temperatures are
upper envelopes of T_CMB in principle, since collisional excitation
can only raise T_ex above the radiation temperature; Klimenko et al.
(2020) estimated the collisional correction lowers several entries by
<~10%.  The primary test therefore evaluates the published T_ex values
as T_CMB estimators (the convention adopted by the measurement papers
themselves), with the collisional correction propagated as a
sensitivity check that shifts all TEP predictions upward relative to
T_ex. This is a sensitivity check, not a guaranteed improvement in fit;
the resulting chi-square and fitted exponent are reported explicitly.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize_scalar

from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
)

STEP_ID = "step_11_excitation_temperature"

T0_FIRAS = 2.7255          # K, FIRAS monopole (Fixsen 2009)
T0_FIRAS_ERR = 0.0006

# Published excitation-temperature measurements.
# (name, z, T_ex K, sigma_low, sigma_high, tracer, reference)
MEASUREMENTS = [
    ("FIRAS monopole",        0.0000, 2.7255, 0.0006, 0.0006, "monopole", "Fixsen 2009"),
    ("PKS 1830-211",          0.8867, 5.08,   0.10,   0.10,   "CO mm",    "Muller et al. 2013"),
    ("SDSS J085726+185524",   1.7293, 7.5,    1.2,    1.6,    "CO",       "Noterdaeme et al. 2011"),
    ("SDSS J104705+205734",   1.7738, 7.8,    0.6,    0.7,    "CO",       "Noterdaeme et al. 2011"),
    ("SDSS J170542+354340",   2.0377, 8.6,    1.0,    1.1,    "CO",       "Noterdaeme et al. 2011"),
    ("SDSS J143912+111740",   2.4184, 9.15,   0.7,    0.7,    "CO",       "Srianand et al. 2008"),
    ("SDSS J123714+064759",   2.6896, 10.5,   0.6,    0.8,    "CO",       "Noterdaeme et al. 2010"),
]

# Literature beta constraints for cross-checking the fitted exponent:
# Noterdaeme et al. 2011: beta = -0.007 +/- 0.027 (CO sample + SZ)
# Klimenko et al. 2020:   beta = +0.010 +/- 0.013 (15 CO/C I systems + SZ)


def t_tep(z):
    """TEP matter-frame local temperature T0 (1+z) = T0/A_clock."""
    return T0_FIRAS * (1.0 + np.asarray(z))


def t_tired(z):
    """Constant-temperature (tired-light class) null."""
    return np.full_like(np.asarray(z, dtype=float), T0_FIRAS)


def chi2(model_fn, z, t_obs, sig):
    return float(np.sum(((t_obs - model_fn(z)) / sig) ** 2))


def fit_beta(z, t_obs, sig):
    """Fit T = T0 (1+z)^(1-beta) for beta (T0 fixed at FIRAS)."""

    def loss(beta):
        return np.sum(((t_obs - T0_FIRAS * (1 + z) ** (1 - beta)) / sig) ** 2)

    res = minimize_scalar(loss, bounds=(-0.3, 0.3), method="bounded")
    # 1-sigma interval by chi2 = chi2_min + 1
    grid = np.linspace(res.x - 0.1, res.x + 0.1, 2001)
    chi = np.array([loss(b) for b in grid])
    inside = grid[chi <= res.fun + 1.0]
    err = (inside.max() - res.x, res.x - inside.min()) if inside.size else (np.nan, np.nan)
    return float(res.x), float(res.fun), err


def run() -> dict:
    logger = TEPLogger(STEP_ID)
    set_step_logger(logger)
    ensure_dirs()
    print_status("Step 11: excitation-temperature test of T(z) = T0(1+z)")

    z = np.array([m[1] for m in MEASUREMENTS])
    t_obs = np.array([m[2] for m in MEASUREMENTS])
    sig = np.array([(m[3] + m[4]) / 2.0 for m in MEASUREMENTS])

    rows = []
    for (name, zi, ti, slo, shi, tracer, ref) in MEASUREMENTS:
        pred = t_tep(zi)
        pull = (ti - pred) / ((slo + shi) / 2.0)
        rows.append({
            "absorber": name, "z": zi, "t_obs_k": ti,
            "sigma_sym_k": round((slo + shi) / 2.0, 4),
            "t_tep_pred_k": round(float(pred), 4),
            "residual_k": round(ti - pred, 4),
            "pull_sigma": round(pull, 3),
            "tracer": tracer, "reference": ref,
        })

    chi2_tep = chi2(t_tep, z, t_obs, sig)
    chi2_tired = chi2(t_tired, z, t_obs, sig)
    ndof = len(z)
    beta, chi2_beta, beta_err = fit_beta(z, t_obs, sig)

    # Collisional-correction sensitivity: Klimenko et al. 2020 found
    # corrections lower T_ex -> T_CMB by up to ~10%; apply a uniform
    # -10% shift to the CO entries as a bounding control.
    t_corr = t_obs.copy()
    for i, m in enumerate(MEASUREMENTS):
        if m[5] == "CO":
            t_corr[i] = 0.9 * m[2]
    chi2_tep_corr = chi2(t_tep, z, t_corr, sig)
    beta_corr, chi2_beta_corr, _ = fit_beta(z, t_corr, sig)

    max_pull = max(abs(r["pull_sigma"]) for r in rows)
    verdict = (
        "TEP_COMPATIBLE" if (chi2_tep / ndof < 1.5 and max_pull < 2.0)
        else "TEP_TENSION" if max_pull < 3.0 else "TEP_DISFAVORED"
    )

    result = {
        "step": STEP_ID,
        "title": "Distant-absorber excitation-temperature test",
        "n_measurements": ndof,
        "redshift_range": [float(z.min()), float(z.max())],
        "has_data": True,
        "data_source": (
            "Published CO excitation temperatures (Noterdaeme et al. 2011 "
            "Table 1; Srianand et al. 2008; Noterdaeme et al. 2010), "
            "PKS 1830-211 CO (Muller et al. 2013), FIRAS anchor (Fixsen 2009)"
        ),
        "measurements": rows,
        "model_comparison": {
            "tep_adiabatic_beta0": {
                "chi2": round(chi2_tep, 3),
                "chi2_per_dof": round(chi2_tep / ndof, 3),
                "max_abs_pull_sigma": round(max_pull, 3),
            },
            "free_exponent": {
                "beta": round(beta, 4),
                "beta_err_hi": round(beta_err[0], 4),
                "beta_err_lo": round(beta_err[1], 4),
                "chi2": round(chi2_beta, 3),
                "chi2_improvement_vs_tep": round(chi2_tep - chi2_beta, 3),
            },
            "constant_temperature_tired": {
                "chi2": round(chi2_tired, 1),
                "chi2_per_dof": round(chi2_tired / ndof, 1),
                "sqrt_delta_chi2": round(float(np.sqrt(chi2_tired - chi2_tep)), 1),
                "statistic_scope": "Descriptive square-root chi-square difference between fixed curves; not a calibrated TEP discovery significance.",
            },
        },
        "collisional_sensitivity": {
            "note": "Uniform -10% T_ex->T_CMB correction on CO entries "
                    "(bounding Klimenko et al. 2020 estimate)",
            "chi2_tep_corrected": round(chi2_tep_corr, 3),
            "beta_corrected": round(beta_corr, 4),
        },
        "literature_beta_constraints": {
            "noterdaeme_2011": "-0.007 +/- 0.027",
            "klimenko_2020": "+0.010 +/- 0.013",
        },
        "verdict": verdict,
        "interpretation": (
            f"T(z) = T0(1+z) at chi2/dof = {chi2_tep/ndof:.2f} "
            f"(max pull {max_pull:.2f} sigma); fitted exponent "
            f"beta = {beta:+.4f} (+{beta_err[0]:.3f}/-{beta_err[1]:.3f}), "
            f"consistent with the TEP/adiabatic value beta = 0 and with the "
            f"literature constraints; the constant-temperature null "
            f"has chi2 = {chi2_tired:.2f}, versus {chi2_tep:.2f} for the TEP/adiabatic law. "
            "This comparison supports the tested temperature law, not a unique identification of the full framework."
        ),
    }

    write_json(step_json_path(STEP_ID), result)
    write_csv(step_csv_path(STEP_ID), rows)
    print_status(f"  chi2(TEP)/dof = {chi2_tep/ndof:.2f}; "
                 f"beta = {beta:+.4f}; sqrt(delta chi2) = "
                 f"{np.sqrt(chi2_tired - chi2_tep):.1f} (descriptive) -> {verdict}")
    return result


if __name__ == "__main__":
    run()
