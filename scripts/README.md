# TEP-TH Pipeline

## Clean Run

To reproduce all results from a clean state:

```bash
cd "$(dirname "$0")/.."
rm -rf results/*.json results/*.csv results/figures/*
python -m scripts.steps.step_00_temporal_horizon_mapping
python -m scripts.steps.step_01_matter_frame_curvature
python -m scripts.steps.step_02_geodesic_completeness
python -m scripts.steps.step_03_effective_stress_energy
python -m scripts.steps.step_04_full_bbn_abundances
python -m scripts.steps.step_05_recombination_visibility
python -m scripts.steps.step_06_cmb_blackbody_origin
python -m scripts.steps.step_07_entropy_arrow
python -m scripts.steps.step_08_primordial_perturbation_boundary
python -m scripts.steps.step_09b_native_tensor_integration
python -m scripts.steps.step_10_cmb_lss_class
```

Or run individually:

```bash
python scripts/steps/step_09b_native_tensor_integration.py
```

## Dependencies

- Python 3.11+
- NumPy, SciPy
- CLASS Python bindings (`external/class/python/classy.pyx` built)
- AlterBBN (`external/AlterBBN/` built)

## Outputs

All step results are written to `results/` as JSON and CSV.
Key results include BBN abundances (step_04), recombination parameters (step_05), tensor-mode suppression (step_09b), and CMB/LSS consistency (step_10).

## Audit

Run the automated integrity audit:

```bash
python scripts/utils/full_audit.py
python scripts/utils/check2_audit.py
```
