#!/usr/bin/env python3
"""Step 09: Temporal-Horizon Claim Gate.

Aggregates results from steps 00--08 and the CMB/LSS step into a three-level claim hierarchy
and evaluates whether TEP-TH satisfies the temporal-horizon cosmology claims.
"""

from __future__ import annotations

import json
import time
import hashlib
from pathlib import Path

from th_common import (
    TEPLogger, ensure_dirs, print_status, read_json, set_step_logger,
    step_json_path, write_json,
)

STEP_ID = "step_09_temporal_horizon_claim_gate"


def _load_prior_results() -> dict:
    """Load prerequisite step results."""
    results = {}
    steps = [
        ("step_00_temporal_horizon_mapping", "mapping_valid"),
        ("step_01_matter_frame_curvature", "curvature_regular"),
        ("step_02_geodesic_completeness", "geodesic_complete"),
        ("step_03_effective_stress_energy", "sec_violated"),
        ("step_04_full_bbn_abundances", "bbn_preserved"),
        ("step_05_recombination_visibility", "recombination_preserved"),
        ("step_06_cmb_blackbody_origin", "blackbody_preserved"),
        ("step_07_entropy_arrow", "entropy_regular"),
        ("step_08_primordial_perturbation_boundary", "perturbation_well_defined"),
        ("step_10_cmb_lss_class", "cmb_lss_consistent"),
    ]
    for step_name, key_hint in steps:
        path = step_json_path(step_name)
        if path.exists():
            results[step_name] = read_json(path)
        else:
            results[step_name] = None
            print_status(f"Missing prerequisite: {step_name}", "WARNING")
    return results


def _extract_status(step_result, *keys, default=None):
    """Read an explicit JSON boolean; absent/malformed values remain unknown."""
    current = step_result
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, list) and isinstance(key, int) and 0 <= key < len(current):
            current = current[key]
        else:
            return default
    return current if isinstance(current, bool) else default


def _all_status(*values):
    """Conjunction with unknown distinct from both success and failure."""
    if any(v is False for v in values):
        return False
    return True if all(v is True for v in values) else None


def evaluate_inputs(prior):
    """Use producer verdicts without replacing explicit failures by controls."""
    get = lambda step, *keys: _extract_status(prior.get(step), *keys)
    mapping = get('step_00_temporal_horizon_mapping', 'mapping_valid')
    if mapping is None:
        mapping = get('step_00_temporal_horizon_mapping', 'epsilon_sensitivity', 0, 'mapping_valid')
    curvature = get('step_01_matter_frame_curvature', 'overall_status', 'matter_frame_regular')
    if curvature is None:
        curvature = get('step_01_matter_frame_curvature', 'pure_conformal', 'regularity_status', 'matter_frame_regular')
    bbn = get('step_04_full_bbn_abundances', 'summary', 'BBN_preserved')
    if bbn is None:
        bbn = _all_status(*(get('step_04_full_bbn_abundances', 'abundance_comparison', sp, 'TEP_consistent')
                            for sp in ('Y_p', 'D_H')))
    sec = get('step_03_effective_stress_energy', 'energy_conditions', 'SEC')
    cmb = get('step_10_cmb_lss_class', 'cmb_scorecard', 'cmb_consistent')
    lss = get('step_10_cmb_lss_class', 'lss_scorecard', 'lss_consistent')
    return dict(mapping_valid=mapping, curvature_regular=curvature,
        geodesic_complete=get('step_02_geodesic_completeness', 'completeness_status', 'geodesically_complete'),
        bbn_preserved=bbn,
        recombination_preserved=get('step_05_recombination_visibility', 'baseline_comparison', 'tep_with_screening', 'visibility_preserved'),
        thermal_preserved=get('step_06_cmb_blackbody_origin', 'blackbody_preserved'),
        entropy_regular=get('step_07_entropy_arrow', 'entropy_regularity', 's_standard_finite'),
        perturbation_well_defined=get('step_08_primordial_perturbation_boundary', 'boundary_well_defined'),
        sec_violated=None if sec is None else not sec,
        cmb_consistent=cmb, lss_consistent=lss, cmb_lss_consistent=_all_status(cmb,lss))


def run() -> dict:
    logger = TEPLogger(STEP_ID, log_file_path=Path(f"logs/{STEP_ID}.log"))
    set_step_logger(logger)
    print_status(f"Starting {STEP_ID}", "TITLE")
    ensure_dirs()

    prior = _load_prior_results()

    checks = evaluate_inputs(prior)
    mapping_valid = checks['mapping_valid']
    curvature_regular = checks['curvature_regular']
    geodesic_complete = checks['geodesic_complete']
    bbn_preserved = checks['bbn_preserved']
    recombination_preserved = checks['recombination_preserved']
    thermal_preserved = blackbody_preserved = checks['thermal_preserved']
    entropy_regular = checks['entropy_regular']
    perturbation_well_defined = checks['perturbation_well_defined']
    sec_violated = checks['sec_violated']
    cmb_lss_consistent = checks['cmb_lss_consistent']
    level_1_passes = _all_status(mapping_valid, thermal_preserved)
    level_2_passes = _all_status(curvature_regular, geodesic_complete, bbn_preserved, recombination_preserved)
    level_3_passes = _all_status(level_2_passes, blackbody_preserved, entropy_regular,
                               perturbation_well_defined, cmb_lss_consistent)

    payload = {
        "step": STEP_ID,
        "description": "Automated claim gate for temporal-horizon cosmology",
        "claim_levels": {
            "level_1": {
                "name": "Temporal-Horizon Reinterpretation",
                "claim": "The Big Bang singularity is a temporal-horizon limit in the distance/acoustic sector.",
                "passes": level_1_passes,
                "criteria": {
                    "mapping_valid": mapping_valid,
                    "thermal_preserved": thermal_preserved,
                    "passes": level_1_passes,
                    "established_claim": "The Big Bang singularity is a temporal-horizon limit in the distance/acoustic sector.",
                },
            },
            "level_2": {
                "name": "Nonsingular Matter-Frame Cosmology",
                "claim": "The physical matter-frame geometry is nonsingular in the TEP early-universe closure.",
                "passes": level_2_passes,
                "criteria": {
                    "curvature_regular": curvature_regular,
                    "geodesic_complete_or_asymptotic": geodesic_complete,
                    "bbn_preserved": bbn_preserved,
                    "recombination_preserved": recombination_preserved,
                    "passes": level_2_passes,
                    "established_claim": "The physical matter-frame geometry is nonsingular in the TEP early-universe closure.",
                },
            },
            "level_3": {
                "name": "Full Big-Bang Replacement",
                "claim": "TEP-TH replaces the standard Big Bang interpretation with a complete nonsingular temporal-horizon cosmology.",
                "passes": level_3_passes,
                "criteria": {
                    "level_2_required": level_2_passes,
                    "blackbody_preserved": blackbody_preserved,
                    "entropy_regular": entropy_regular,
                    "perturbation_well_defined": perturbation_well_defined,
                    "cmb_lss_consistent": cmb_lss_consistent,
                    "passes": level_3_passes,
                    "established_claim": "TEP-TH replaces the standard Big Bang interpretation with a complete nonsingular temporal-horizon cosmology.",
                },
            },
        },
        "overall_claim": {
            "level_achieved": 3 if level_3_passes else (2 if level_2_passes else (1 if level_1_passes else 0)),
            "final_claim": (
                "Level 3: Full Big-Bang Replacement" if level_3_passes else
                "Level 2: Nonsingular Matter-Frame Cosmology" if level_2_passes else
                "Level 1: Temporal-Horizon Reinterpretation" if level_1_passes else
                "No claim established"
            ),
            "strength": (
                "Full Big-Bang Replacement" if level_3_passes else
                "Nonsingular Matter-Frame Cosmology" if level_2_passes else
                "Temporal-Horizon Reinterpretation" if level_1_passes else
                "None"
            ),
        },
        "singularity_theorem_analysis": {
            "SEC_violated": sec_violated,
            "evades_standard_theorem": sec_violated,
            "supports_nonsingular_claim": sec_violated,
        },
        "subclaims": {
            "horizon_mapping": {
                "description": "Temporal-horizon mapping established (a_eff → 0 ↔ A → 0)",
                "status": mapping_valid,
            },
            "curvature_boundedness": {
                "description": "Matter-frame curvature invariants vanish at the temporal horizon (Proposition 1)",
                "status": curvature_regular,
            },
            "geodesic_non_termination": {
                "description": "Null and timelike geodesics do not terminate at finite affine/proper time",
                "status": geodesic_complete,
            },
            "singularity_theorem_evasion": {
                "description": "SEC violation evades Hawking-Penrose singularity theorems",
                "status": sec_violated,
            },
            "bbn_preservation": {
                "description": "Primary BBN checks (Y_p and D/H); other species retain their producer diagnostic scope",
                "status": bbn_preserved,
            },
            "recombination_visibility": {
                "description": "Recombination visibility function and acoustic scales preserved",
                "status": recombination_preserved,
            },
            "blackbody_preservation": {
                "description": "CMB blackbody spectrum preserved without spectral distortions",
                "status": blackbody_preserved,
            },
            "entropy_regularity": {
                "description": "Entropy and arrow-of-time regularity maintained at horizon",
                "status": entropy_regular,
            },
            "perturbation_boundary": {
                "description": "Primordial perturbation boundary condition is well-defined",
                "status": perturbation_well_defined,
            },
            "cmb_anisotropy_match": {
                "description": "CMB TT/TE/EE anisotropy spectra match Planck within observational tolerance",
                "status": checks["cmb_consistent"],
            },
            "lss_bao_match": {
                "description": "Matter power spectrum, growth factor, and BAO scales match SDSS/BOSS",
                "status": checks["lss_consistent"],
            },
        },
        "subclaim_summary": {},
        "pipeline_status": {
            "all_steps_completed": all(isinstance(v, dict) and not v.get('error') for v in prior.values()),
            "steps_completed": sum(isinstance(v, dict) and not v.get('error') for v in prior.values()),
            "total_steps": len(prior),
            "missing_steps": [k for k,v in prior.items() if v is None],
        },
        "interpretation": "Pending — set after claim evaluation",
        "timestamp": int(time.time()),
    }

    states = [v['status'] for v in payload['subclaims'].values()]
    payload['subclaim_summary'] = {
        'total': len(states), 'passing': sum(v is True for v in states),
        'failing': sum(v is False for v in states),
        'unverified': sum(v is None for v in states),
        'pass_rate': sum(v is True for v in states)/len(states)}
    for level in payload['claim_levels'].values():
        passed = level['passes']
        level['evaluation_status'] = 'PASS' if passed is True else 'FAIL' if passed is False else 'NOT_VERIFIED'
        if passed is not True:
            level['criteria']['established_claim'] = None
    payload['input_sha256'] = {name: hashlib.sha256(step_json_path(name).read_bytes()).hexdigest()
        for name,value in prior.items() if value is not None}
    payload['scope'] = ('Aggregate of the declared saved benchmark verdicts. Passing this summary '
                        'does not extend the physical scope of its component calculations.')

    # Fix the interpretation that references payload before it exists
    if level_3_passes:
        payload["interpretation"] = "TEP-TH achieves Level 3 claim: Full Big-Bang Replacement"
    elif level_2_passes:
        payload["interpretation"] = "TEP-TH achieves Level 2 claim: Nonsingular Matter-Frame Cosmology"
    elif level_1_passes:
        payload["interpretation"] = "TEP-TH achieves Level 1 claim: Temporal-Horizon Reinterpretation"
    else:
        payload["interpretation"] = "TEP-TH has not yet established Level 1 claim."

    if any(v is None for v in states):
        payload["interpretation"] += " Some component checks are unverified; see subclaim_summary."
    write_json(step_json_path(STEP_ID), payload)
    print_status(f"Step {STEP_ID} completed", "SUCCESS")
    return payload


if __name__ == "__main__":
    print(run())
