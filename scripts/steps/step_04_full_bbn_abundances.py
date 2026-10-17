#!/usr/bin/env python3
"""Step 04: Full BBN Abundance Validation.

Validate light-element abundances (Y_p, D/H, He-3/H, Li-7/H, N_eff) under
temporal-horizon cosmology to test whether BBN is preserved without
requiring a physical zero-volume Big Bang singularity.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
from th_common import (
    TEPLogger, ensure_dirs, print_status, rounded, set_step_logger,
    step_json_path, step_csv_path, write_json, write_csv,
    conformal_factor_A, DEFAULT_EPSILON_T, DEFAULT_Z_T, DEFAULT_N_T,
    DEFAULT_T_LOCK, DEFAULT_N_EPOCH,
    H0_KM_S_MPC, OMEGA_M
)

STEP_ID = "step_04_full_bbn_abundances"


# Observational anchors and diagnostic references; this is not a joint likelihood.
OBSERVED_ABUNDANCES = {
    'Y_p': {'value': 0.245, 'error': 0.003, 'description': 'Primordial helium-4 mass fraction',
            'source': 'PDG 2024 BBN review, Eq. 24.3',
            'source_url': 'https://pdg.lbl.gov/2024/reviews/rpp2024-rev-bbang-nucleosynthesis.pdf'},
    'D_H': {'value': 2.527e-5, 'error': 0.030e-5, 'description': 'Deuterium/Hydrogen ratio'},
    'He3_H': {'value': 1.66e-5, 'error': 0.08e-5, 'description': 'Helium-3/Hydrogen ratio'},
    'Li7_H': {'value': 1.58e-10, 'error': 0.10e-10, 'description': 'Lithium-7/Hydrogen ratio'},
    'N_eff': {'value': 3.04, 'error': 0.17, 'description': 'Effective neutrino species'}
}


# Standard ΛCDM BBN predictions (for comparison)
LCDM_BBN = {
    'Y_p': 0.2472,
    'D_H': 2.456e-5,
    'He3_H': 1.033e-5,
    'Li7_H': 5.383e-10,  # Lithium problem known
    'N_eff': 3.046
}


def tep_hubble_parameter_bbn(z: np.ndarray, epsilon_t: float = DEFAULT_EPSILON_T,
                             z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T,
                             T_lock: float = DEFAULT_T_LOCK, n_epoch: float = DEFAULT_N_EPOCH,
                             use_screening: bool = False) -> np.ndarray:
    """TEP-modified Hubble parameter during BBN epoch.
    
    H_TEP(z) = H_LCDM(z) * M(z) where M(z) = A(z) / (1 - α_A(z))
    Simplified: H_TEP ≈ H_LCDM * A^(-1) for pure conformal case
    
    With screening: H_TEP ≈ H_LCDM * A_eff^(-1) where A_eff uses epoch-screened epsilon
    """
    from th_common import e_z
    H_lcdm = H0_KM_S_MPC * e_z(z)
    A = conformal_factor_A(z, epsilon_t, z_t, n_t, T_lock, n_epoch, use_screening)
    
    # Jordan-frame conformal factor (simplified)
    M = 1.0 / A  # Pure conformal limit
    
    H_tep = H_lcdm * M
    return H_tep


def compute_bbn_abundances_tep(omega_b: float = 0.022, omega_cdm: float = 0.12,
                               epsilon_t: float = DEFAULT_EPSILON_T,
                               z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T,
                               T_lock: float = DEFAULT_T_LOCK, n_epoch: float = DEFAULT_N_EPOCH,
                               use_screening: bool = False) -> dict:
    """Compute BBN abundances under TEP temporal-horizon cosmology.

    Uses full AlterBBN nuclear network.  For unscreened TEP the modified
    Hubble parameter H_TEP = H_LCDM / A at one BBN epoch is mapped to
    AlterBBN's extra-radiation parameter dnnu. This is an expansion-rate
    proxy, not a calculation of a physical neutrino population or the
    full temperature-dependent TEP expansion history.
    """

    # BBN redshift (z ~ 1e9)
    z_bbn = 1e9

    # Compute conformal factor at BBN
    A_bbn = conformal_factor_A(z_bbn, epsilon_t, z_t, n_t, T_lock, n_epoch, use_screening)

    # Expansion rate modification factor
    expansion_factor = 1.0 / A_bbn

    # Map TEP H-modification to AlterBBN extra-neutrino parameter dnnu.
    # In radiation domination H^2 \propto \rho_rad \propto g_eff T^4.
    # TEP gives H_TEP = H_LCDM / A, so we need g_eff_TEP = g_eff_LCDM / A^2.
    # Adding dnnu extra neutrino species increases g_eff by 1.75 per species:
    #   g_eff = 5.5 + 1.75 * (3.046 + dnnu)
    # Solving for dnnu gives:
    #   dnnu = g_eff_LCDM * (1/A^2 - 1) / 1.75
    g_eff_lcdm = 5.5 + 1.75 * 3.046  # ≈ 10.83
    dnnu = g_eff_lcdm * ((1.0 / (A_bbn ** 2)) - 1.0) / 1.75

    lcdm_ref = LCDM_BBN.copy()
    try:
        import sys
        project_root = Path(__file__).resolve().parents[2]
        sys.path.insert(0, str(project_root / 'external'))
        from alterbbn_wrapper import AlterBBNWrapper

        eta = 2.73e-8 * omega_b
        wrapper = AlterBBNWrapper()

        # LCDM baseline
        abund_lcdm = wrapper.compute_abundances(eta=eta, DeltaN=0.0, tau_neutron=880.3)
        lcdm_ref = {
            'Y_p': abund_lcdm.Y_p,
            'D_H': abund_lcdm.D_H,
            'He3_H': abund_lcdm.He3_H,
            'Li7_H': abund_lcdm.Li7_H,
            'N_eff': LCDM_BBN['N_eff'],
        }

        if dnnu == 0.0:
            # Reuse baseline only when the mapped expansion is exactly unchanged
            abund_tep = abund_lcdm
        else:
            # True TEP abundances from modified-expansion AlterBBN run
            abund_tep = wrapper.compute_abundances(eta=eta, DeltaN=dnnu, tau_neutron=880.3)
    except Exception as exc:
        raise RuntimeError(
            "AlterBBN network failed; refusing to substitute LCDM abundances "
            f"for TEP (A_BBN={A_bbn}, dnnu={dnnu})"
        ) from exc

    Y_p_tep = abund_tep.Y_p
    D_H_tep = abund_tep.D_H
    He3_H_tep = abund_tep.He3_H
    Li7_H_tep = abund_tep.Li7_H
    # Reference neutrino abundance is assumed, not inferred by this mapping.
    N_eff_tep = lcdm_ref['N_eff']

    return {
        'Y_p': Y_p_tep,
        'D_H': D_H_tep,
        'He3_H': He3_H_tep,
        'Li7_H': Li7_H_tep,
        'N_eff': N_eff_tep,
        'expansion_factor': expansion_factor,
        'A_at_BBN': A_bbn,
        'dnnu_mapped': dnnu,
        'engine': 'AlterBBN network',
        'mapping_scope': 'single-epoch extra-radiation expansion proxy',
        'N_eff_status': 'assumed standard reference; not a network prediction',
        'lcdm_reference': lcdm_ref,
        'use_screening': use_screening,
        'T_lock': T_lock,
        'n_epoch': n_epoch
    }


def compare_abundances(tep_abundances: dict) -> dict:
    """Compare TEP abundances with observed values."""
    
    comparison = {}
    
    for species in ['Y_p', 'D_H', 'He3_H', 'Li7_H', 'N_eff']:
        obs = OBSERVED_ABUNDANCES[species]
        tep = tep_abundances[species]
        lcdm_ref = tep_abundances.get('lcdm_reference', LCDM_BBN)
        lcdm = lcdm_ref[species]
        
        diff_tep = (tep - obs['value']) / obs['error']
        diff_lcdm = (lcdm - obs['value']) / obs['error']
        
        comparison[species] = {
            'observed': obs['value'],
            'observed_error': obs['error'],
            'source': obs.get('source'),
            'source_url': obs.get('source_url'),
            'prediction_test': species != 'N_eff',
            'TEP': tep,
            'LCDM': lcdm,
            'TEP_sigma_diff': rounded(diff_tep, 2),
            'LCDM_sigma_diff': rounded(diff_lcdm, 2),
            'TEP_consistent': abs(diff_tep) < 3,
            'LCDM_consistent': abs(diff_lcdm) < 3,
            'TEP_better': abs(diff_tep) < abs(diff_lcdm)
        }
    
    return comparison


def test_bbn_preservation(omega_b: float = 0.022, omega_cdm: float = 0.12,
                         epsilon_t: float = DEFAULT_EPSILON_T,
                         z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T,
                         T_lock: float = DEFAULT_T_LOCK, n_epoch: float = DEFAULT_N_EPOCH,
                         use_screening: bool = False) -> dict:
    """Test BBN abundance preservation under temporal-horizon cosmology."""
    
    # Compute TEP abundances
    tep_abundances = compute_bbn_abundances_tep(omega_b, omega_cdm, epsilon_t, z_t, n_t, 
                                                  T_lock, n_epoch, use_screening)
    
    # Compare with observations
    comparison = compare_abundances(tep_abundances)
    
    # Count successes
    primary_species = ['Y_p', 'D_H']
    diagnostic_species = ['He3_H', 'Li7_H']
    assumed_reference_species = ['N_eff']
    tep_passes_primary = sum(1 for sp in primary_species if comparison[sp]['TEP_consistent'])
    lcdm_passes_primary = sum(1 for sp in primary_species if comparison[sp]['LCDM_consistent'])
    total_primary = len(primary_species)

    tep_passes = sum(1 for name, sp in comparison.items()
                     if name not in assumed_reference_species and sp['TEP_consistent'])
    lcdm_passes = sum(1 for name, sp in comparison.items()
                      if name not in assumed_reference_species and sp['LCDM_consistent'])
    total_tests = len(comparison) - len(assumed_reference_species)
    
    results = {
        'step': STEP_ID,
        'description': 'BBN abundance validation under temporal-horizon cosmology',
        'parameters': {
            'omega_b': omega_b,
            'omega_cdm': omega_cdm,
            'epsilon_t': epsilon_t,
            'z_t': z_t,
            'n_t': n_t,
            'T_lock': T_lock,
            'n_epoch': n_epoch,
            'use_screening': use_screening
        },
        'TEP_abundances': {
            'Y_p': rounded(tep_abundances['Y_p'], 6),
            'D_H': rounded(tep_abundances['D_H'], 10),
            'He3_H': rounded(tep_abundances['He3_H'], 10),
            'Li7_H': rounded(tep_abundances['Li7_H'], 15),
            'N_eff': rounded(tep_abundances['N_eff'], 4),
            'expansion_factor_at_BBN': rounded(tep_abundances['expansion_factor'], 6),
            'A_at_BBN': rounded(tep_abundances['A_at_BBN'], 15)
        },
        'calculation_provenance': {key: tep_abundances[key] for key in
                                   ('engine', 'mapping_scope', 'dnnu_mapped', 'N_eff_status')},
        'abundance_comparison': comparison,
        'summary': {
            'primary_species': primary_species,
            'diagnostic_species': diagnostic_species,
            'assumed_reference_species': assumed_reference_species,
            'scope': 'Conditional single-epoch expansion benchmark; observation-only residuals, no nuclear theory covariance.',
            'TEP_passes_primary': tep_passes_primary,
            'LCDM_passes_primary': lcdm_passes_primary,
            'total_primary': total_primary,
            'TEP_success_rate_primary': rounded(tep_passes_primary / total_primary, 3),
            'LCDM_success_rate_primary': rounded(lcdm_passes_primary / total_primary, 3),
            'TEP_passes': tep_passes,
            'LCDM_passes': lcdm_passes,
            'total_tests': total_tests,
            'TEP_success_rate': rounded(tep_passes / total_tests, 3),
            'LCDM_success_rate': rounded(lcdm_passes / total_tests, 3),
            'BBN_preserved': tep_passes_primary == total_primary
        },
        'interpretation': 'BBN abundances preserved under temporal-horizon cosmology' if 
                          tep_passes_primary == total_primary else
                          'BBN abundances require further analysis or disformal corrections'
    }
    
    # Generate CSV output
    csv_rows = []
    for species, comp in comparison.items():
        csv_rows.append({
            'species': species,
            'observed': comp['observed'],
            'observed_error': comp['observed_error'],
            'TEP': comp['TEP'],
            'LCDM': comp['LCDM'],
            'TEP_sigma_diff': comp['TEP_sigma_diff'],
            'LCDM_sigma_diff': comp['LCDM_sigma_diff'],
            'TEP_consistent': comp['TEP_consistent'],
            'LCDM_consistent': comp['LCDM_consistent']
        })
    
    write_csv(step_csv_path(STEP_ID), csv_rows)
    
    return results


def run():
    logger = TEPLogger(STEP_ID, log_file_path=Path(f"logs/{STEP_ID}.log"))
    set_step_logger(logger)
    print_status(f"Starting {STEP_ID}", "TITLE")
    ensure_dirs()
    
    # Test with default parameters (no screening)
    print_status("Testing TEP without screening", "INFO")
    results_no_screening = test_bbn_preservation(use_screening=False)
    
    # Test with early-epoch screening
    print_status("Testing TEP with early-epoch screening", "INFO")
    results_screening = test_bbn_preservation(use_screening=True, T_lock=1.0, n_epoch=2.0)
    
    # Compare results
    comparison = {
        'no_screening': {
            'TEP_success_rate': results_no_screening['summary']['TEP_success_rate'],
            'expansion_factor': results_no_screening['TEP_abundances']['expansion_factor_at_BBN']
        },
        'with_screening': {
            'TEP_success_rate': results_screening['summary']['TEP_success_rate'],
            'expansion_factor': results_screening['TEP_abundances']['expansion_factor_at_BBN']
        }
    }
    
    results_screening['screening_comparison'] = comparison
    results_screening['no_screening_baseline'] = results_no_screening
    
    write_json(step_json_path(STEP_ID), results_screening)
    print_status(f"Step {STEP_ID} completed successfully", "SUCCESS")
    print_status(f"BBN preserved (no screening): {results_no_screening['summary']['BBN_preserved']}", "INFO")
    print_status(f"BBN preserved (with screening): {results_screening['summary']['BBN_preserved']}", "INFO")
    print_status(f"TEP success rate (no screening): {results_no_screening['summary']['TEP_success_rate']}", "INFO")
    print_status(f"TEP success rate (with screening): {results_screening['summary']['TEP_success_rate']}", "INFO")
    print_status(f"Expansion factor (no screening): {results_no_screening['TEP_abundances']['expansion_factor_at_BBN']}", "INFO")
    print_status(f"Expansion factor (with screening): {results_screening['TEP_abundances']['expansion_factor_at_BBN']}", "INFO")
    
    return results_screening


if __name__ == "__main__":
    run()
