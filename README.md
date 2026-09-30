# Temporal Equivalence Principle: Temporal Horizon Cosmology and the Absence of a Physical Big Bang Singularity

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20723059.svg)](https://doi.org/10.5281/zenodo.20723059)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Version:** v0.4 (Thika)  
**First published:** 18 June 2026 · **Last updated:** 30 September 2026

## Abstract





Standard FLRW cosmology extrapolates observed cosmic expansion backward to a(t)to0, producing a Big Bang singularity at finite proper time. This paper demonstrates that this singularity is a reconstruction artifact of imposing a globally isochronous expanding-frame description on a conformal temporal geometry. In the Temporal Equivalence Principle (TEP), the observational role of FLRW expansion is reconstructed through conformal temporal transport: the effective scale factor a_eff arises from accumulated open-path conformal temporal shear along cosmological lines of sight rather than from physical expansion of space. TEP-C0 (Paper 26) established the distance-redshift and supernova evidence ; the conditional nonsingular matter-frame boundary construction is developed here. Realization of that boundary within the complete infinite inhomogeneous solution remains the common-action construction problem of Paper 0. The Temporal Horizon Cosmology framework is developed here, proving, within the temporal-conformal branch defined here, that the apparent a_effto0 limit is not a physical curvature singularity but a temporal horizon. The effective scale factor a_eff is driven by the observational clock/redshift mapping A_clock(z)=(1+z)⁻¹. Proposition 1 establishes curvature regularity of the temporal conformal boundary: for A_clock(η)=Cη⁻p with 0 < p ≤ ½, all polynomial curvature invariants vanish at the boundary, timelike proper time diverges, and null geodesics have divergent affine parameter. The temporal-horizon exponent p and the observational clock map are independent boundary conditions: A_clock(z)=(1+z)⁻¹ is fixed by the redshift definition, while the regularity condition 0 < p ≤ ½ is a mathematical requirement for curvature-regularity at the conformal boundary. Here η is the temporal-horizon conformal coordinate, oriented so that approach to mathscrT⁻ corresponds to the asymptotic limit in which A_clockto0; it is not the standard FLRW conformal time coordinate extrapolated to a=0. Figure 1 (Section 4.5) illustrates the resulting conformal-boundary interpretation: the singular lower edge of standard flat ΛCDM is replaced by a smooth temporal conformal boundary mathscrT⁻, where A_clockto0 and curvature invariants vanish. The conformal compactification is smooth, the Weyl tensor vanishes on the boundary, and every causal curve approaches the regular past boundary mathscrT⁻ rather than terminating at a singularity. The temporal horizon is therefore simultaneously curvature-empty, timelike-complete, and null-complete in this branch. The effective stress-energy tensor of the temporal field violates the Strong Energy Condition, an explicit prerequisite of the Hawking-Penrose singularity theorems. Rather than treating the high-redshift hot plasma as the residue of a singular expanding origin, TEP retains that thermal state as a matter-frame condition of the temporal landscape and replaces the singular-origin interpretation with Native Local Thermodynamic Evolution in an eternal universe. The temporal-horizon metric provides the geometric boundary where the clock rate vanishes, but it does not claim to uniquely derive primordial abundances. Instead, it delegates the thermal history to the eternal chemical-evolution framework (TEP-BBN, Paper 29), which provides an eternal-universe framework in which chemical states can approach a steady-state asymptotic equilibrium where D/H is no longer uniquely primordial and helium arises through baryonic cycling. The temporal-horizon thermal mapping preserves the observed CMB photon distribution through local decoupling processes without requiring a geometric singularity. The scalar perturbation spectrum is derived from fluctuations of the clock field, ζ=δln A_clock, yielding a power spectrum P_ζ(k)∝ k^n_s-1 with spectral-flow parameter n_s-1=-2ε_field. The observed Planck value n_s=0.9649 constrains ε_field=0.01755. Tensor modes are derived directly from the temporal-conformal metric: for A_clock(η)simη⁻p the tensor source term A_clock''/A_clock=p(p+1)/η²→ 0 at the horizon, so the tensor equation approaches the Minkowski vacuum. The imported inflationary consistency relation r=16ε_field is not assumed. Numerical integration of the native tensor equation across the finite transition profile yields r(k_pivot)=1.9 ×  10⁻⁹ and r_max=5.2 ×  10⁻⁷, both far below the BICEP/Keck 2021 bound rlt0.036; tensor power is controlled only by the finite transition region. The late-time homogeneous expansion and acoustic observables (Planck 2018, BOSS DR12) are fully preserved by the conformal temporal mapping as mathematically confirmed in TEP-HC (Paper 18). The causal matter-frame universe is curvature-regular at the temporal conformal boundary. The apparent Big Bang is a temporal horizon, not a physical curvature singularity. The temporal-horizon geometry supplies a nonsingular framework in which the standard background and acoustic observables are reconstructed by the conformal mapping, while TEP-BBN provides the native chemical-evolution mechanism and a proof of concept for local CMB thermalization; the scalar perturbation shape is reproduced, and the tensor-to-scalar ratio is computed from the native temporal-conformal wave equation, yielding values well below observational bounds. Code Availability: https://github.com/matthewsmawfield/TEP-TH


## Overview

TEP-TH (Paper 27, Thika) delivers the full temporal-horizon closure of the Temporal Equivalence Principle framework, proving that the apparent Big Bang singularity is a reconstruction artifact. Building on TEP-C0 (Paper 26, Athens) which established the distance-redshift and supernova evidence, and TEP-HC (Paper 18, Cambridge) which validated the acoustic-sector perturbations via hi_class, TEP-TH provides:

- **Temporal-horizon curvature analysis** proving regularity at $A_{\rm clock}\to 0$ (Proposition 1)
- **Geodesic completeness** demonstrating infinite affine/proper time at the temporal boundary
- **Penrose diagram** (Figure 1) placing $\mathscr{T}^{-}$ on the same rigorous footing as $\mathscr{I}^{+}$
- **BBN and recombination** delegated to TEP-BBN (Paper 29) eternal-universe architecture
- **Temporal-horizon thermal mapping** preserving FIRAS-compatible blackbody
- **Scalar perturbations** derived from clock-field fluctuations with spectral-flow parameter $\epsilon_{\rm field}=0.01755
- **Tensor perturbations** computed from native temporal-conformal wave equation yielding $r(k_{\rm pivot})=9\times 10^{-6}$
- **CMB anisotropy** (TT, TE, EE) and **LSS observables** validated via conformal acoustic equivalence (TEP-HC, Paper 18)

## Installation

```bash
# Clone repository
git clone https://github.com/matthewsmawfield/TEP-TH.git
cd TEP-TH

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize external submodules (CLASS)
git submodule update --init --recursive
```

## Quick Start

```bash
# Run full pipeline
cd TEP-TH
python scripts/run_pipeline.py

# Individual steps (see scripts/README.md)
python scripts/steps/step_00_temporal_horizon_mapping.py
python scripts/steps/step_01_matter_frame_curvature.py
python scripts/steps/step_02_geodesic_completeness.py
```

## Pipeline Execution

### Full Pipeline
```bash
cd TEP-TH
python scripts/run_pipeline.py
```

### Individual Steps
```bash
# Temporal horizon mapping
python scripts/steps/step_00_temporal_horizon_mapping.py

# Matter-frame curvature
python scripts/steps/step_01_matter_frame_curvature.py

# Geodesic completeness
python scripts/steps/step_02_geodesic_completeness.py

# Scalar perturbations
python scripts/steps/step_08_primordial_perturbation_boundary.py

# Tensor perturbations
python scripts/steps/step_09b_native_tensor_integration.py
```

## Data Sources

All data is downloaded from public repositories:

- **BBN data**: [BBN Frontiers 2020 Review](https://arxiv.org/abs/2005.14167)
  - Light-element abundance constraints
  - Nuclear reaction rates

- **FIRAS CMB**: [NASA LAMBDA](https://lambda.gsfc.nasa.gov)
  - COBE/FIRAS monopole spectrum
  - Perfect blackbody validation

- **CMB/LSS**: Planck 2018 and BOSS DR12 public releases
  - Used for conformal acoustic equivalence validation (TEP-HC)

## Physics Validation

| Observable | Computed | Target | Status |
|------------|----------|--------|--------|
| $\tilde{\mathcal{K}}$ at horizon | 0 | 0 (regular) | ✅ |
| Timelike proper time | $\infty$ | $\infty$ (complete) | ✅ |
| Null affine parameter | $\infty$ | $\infty$ (complete) | ✅ |
| $Y_p$ | 0.247 | Planck 0.247 | ✅ |
| D/H | $2.51\times 10^{-5}$ | PDG $2.6\times 10^{-5}$ | ✅ |
| $n_s$ | 0.965 | Planck 0.965 | ✅ |
| $r(k_{\rm pivot})$ | $9\times 10^{-6}$ | BICEP/Keck $<0.036$ | ✅ |
| $r_{\rm max}$ | $6.26\times 10^{-4}$ | BICEP/Keck $<0.036$ | ✅ |

## Project Structure

```
TEP-TH/
├── core/                 # Physics modules
│   ├── conformal_scaling.py  # Conformal clock field
│   ├── constants.py         # Physical constants
│   └── cosmology.py          # Background cosmology
├── scripts/              # Pipeline scripts
│   ├── steps/               # Individual pipeline steps
│   │   ├── step_00_temporal_horizon_mapping.py
│   │   ├── step_01_matter_frame_curvature.py
│   │   ├── step_02_geodesic_completeness.py
│   │   └── ...
│   └── utils/               # Utilities
├── external/              # External codes
│   └── class/               # CLASS Boltzmann code
├── data/                 # Data directory
│   ├── raw/                 # Downloaded datasets
│   └── processed/          # Intermediate outputs
├── results/              # Pipeline outputs
│   ├── figures/             # Generated plots
│   └── outputs/             # JSON results
├── site/                 # Manuscript site
│   ├── components/          # HTML components
│   └── public/              # Static assets
└── manuscripts/          # Markdown manuscripts
```

## Testing

```bash
# Run individual step with verbose logging
python scripts/steps/step_01_matter_frame_curvature.py --verbose

# Check results
cat results/step_01_matter_frame_curvature.json
```

## Methodology

### Temporal-Horizon Mapping

The TEP framework distinguishes two projections of the temporal field:

```
A_clock(z) = (1 + z)^(-1)  # Exact observational clock/redshift mapping
A_dyn(z) = (1 + z/z_t)^(-ε_dyn)  # Dynamic shear response

```

Where:
- `A_clock(z)`: drives a_eff → 0 as z → ∞ (temporal horizon)
- `A_dyn(z)`: modifies expansion, BBN, recombination, perturbations at late times
- `ε_dyn`: baseline shear amplitude
- `z_t`: transition redshift (=100)

### Curvature Regularity

For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0<p\le\½$:
- All polynomial curvature invariants vanish at the boundary
- Timelike proper time diverges for $0<p\le 1$
- Null affine parameter diverges for $0<p\le\½$
- The boundary is a regular conformal-temporal endpoint

### BBN and Recombination

- **Delegated to**: TEP-BBN (Paper 29) eternal-universe architecture
- **Abundances**: $Y_p$, D/H, $^3$He/H, $^7$Li/H via Galactic Chemical Evolution equilibrium attractors
- **Recombination**: Steady-state ionization equilibrium without a hot origin

### Perturbations

- **Scalar**: Derived from clock-field fluctuations $\zeta=\delta\ln A_{\rm clock}$
- **Spectral flow**: $n_s-1=-2\epsilon_{\rm field}$ with $\epsilon_{\rm field}=0.01755
- **Tensor**: Native temporal-conformal wave equation, source term $\to 0$ at horizon
- **Results**: $r(k_{\rm pivot})=9\times 10^{-6}$, $r_{\rm max}=6.26\times 10^{-4}$

## Citation

If using this work, please cite:

```bibtex
@software{tep_th_2026,
  author       = {Matthew Lukin Smawfield},
  title        = {Temporal Equivalence Principle: Temporal Horizon Cosmology and the Absence of a Physical Big Bang Singularity},
  year         = 2026,
  publisher    = {Zenodo},
  version      = {v0.4 (Thika)},
  doi          = {10.5281/zenodo.20723059},
  url = {https://mlsmawfield.com/tep/th}
}
```

## License

CC-BY-4.0 - see [LICENSE](LICENSE) file.

## Status

- ✅ Temporal-horizon curvature analysis: Complete
- ✅ Geodesic completeness: Complete
- ✅ Penrose diagram: Complete
- ✅ BBN: Complete (TEP-BBN, Paper 29 — GCE equilibrium attractors)
- ✅ Recombination: Complete (TEP-BBN — steady-state ionization equilibrium)
- ✅ Scalar perturbations: Complete
- ✅ Tensor perturbations: Complete (native wave equation)
- ✅ CMB/LSS validation: Complete (conformal acoustic equivalence, TEP-HC Paper 18)

## Related Papers

- **TEP-C0 (Paper 26, Athens)**: Distance-redshift and supernova evidence
- **TEP-HC (Paper 18, Cambridge)**: Acoustic-sector perturbations via hi_class
- **TEP-TH (Paper 27, Thika)**: Temporal-horizon closure (this work)
- **TEP-BBN (Paper 29, Dubai)**: Eternal-universe BBN and recombination architecture

## Contact

For questions or issues, please open a GitHub issue at https://github.com/matthewsmawfield/TEP-TH