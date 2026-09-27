# Temporal Equivalence Principle: Temporal Horizon Cosmology and the Absence of a Physical Big Bang Singularity

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20723059.svg)](https://doi.org/10.5281/zenodo.20723059)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Version:** v0.4 (Thika)  
**First published:** 18 June 2026 · **Last updated:** 13 September 2026

## Abstract

Standard FLRW cosmology extrapolates observed cosmic expansion backward to $a(t)\to0$, producing a Big Bang singularity at finite proper time. This paper demonstrates that this singularity is a reconstruction artifact of imposing a globally isochronous expanding-frame description on a conformal temporal geometry. In the Temporal Equivalence Principle (TEP), the observational role of FLRW expansion is reconstructed through conformal temporal transport: the effective scale factor $a_{\rm eff}$ arises from accumulated open-path conformal temporal shear along cosmological lines of sight rather than from physical expansion of space. TEP-C0 (Paper 26) established the distance-redshift and supernova evidence ; the full nonsingular matter-frame closure is delivered here.

The Temporal Horizon Cosmology framework is developed here, proving, within the temporal-conformal branch defined here, that the apparent $a_{\rm eff}\to0$ limit is not a physical curvature singularity but a temporal horizon. The effective scale factor $a_{\rm eff}$ is driven by the observational clock/redshift mapping $A_{\rm clock}(z)=(1+z)^{-1}$. Proposition 1 establishes curvature regularity of the temporal conformal boundary: for $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\le\tfrac12$, all polynomial curvature invariants vanish at the boundary, timelike proper time diverges, and null geodesics have divergent affine parameter. The temporal-horizon exponent $p$ and the observational clock map are independent boundary conditions: $A_{\rm clock}(z)=(1+z)^{-1}$ is fixed by the redshift definition, while the regularity condition $0 \lt p\le\tfrac12$ is a mathematical requirement for curvature-regularity at the conformal boundary. Here $\eta$ is the temporal-horizon conformal coordinate, oriented so that approach to $\mathscr{T}^{-}$ corresponds to the asymptotic limit in which $A_{\rm clock}\to0$; it is not the standard FLRW conformal time coordinate extrapolated to $a=0$. Figure 1 (Section 4.5) illustrates the resulting conformal-boundary interpretation: the singular lower edge of standard flat $\Lambda$CDM is replaced by a smooth temporal conformal boundary $\mathscr{T}^{-}$, where $A_{\rm clock}\to0$ and curvature invariants vanish. The conformal compactification is smooth, the Weyl tensor vanishes on the boundary, and every causal curve approaches the regular past boundary $\mathscr{T}^{-}$ rather than terminating at a singularity. The temporal horizon is therefore simultaneously curvature-empty, timelike-complete, and null-complete in this branch.

The effective stress-energy tensor of the temporal field violates the Strong Energy Condition, an explicit prerequisite of the Hawking-Penrose singularity theorems. Rather than assuming the early universe was a globally hot expanding plasma, TEP replaces the hot Big Bang framework with Native Local Thermodynamic Evolution in an eternal universe. The temporal-horizon metric provides the geometric boundary where the clock rate vanishes, but it does not claim to uniquely derive primordial abundances. Instead, it delegates the thermal history to the eternal chemical-evolution framework (TEP-BBN, Paper 29), which provides an eternal-universe framework in which chemical states can approach a steady-state asymptotic equilibrium where D/H is no longer uniquely primordial and helium arises through baryonic cycling. The temporal-horizon thermal mapping preserves the observed CMB photon distribution through local decoupling processes without requiring a geometric singularity.

The scalar perturbation spectrum is derived from fluctuations of the clock field, $\zeta=\delta\ln A_{\rm clock}$, yielding a power spectrum $P_{\zeta}(k)\propto k^{n_{s}-1}$ with spectral-flow parameter $n_{s}-1=-2\epsilon_{\rm field}$. The observed Planck value $n_{s}=0.965$ constrains $\epsilon_{\rm field}=0.01755. Tensor modes are derived directly from the temporal-conformal metric: for $A_{\rm clock}(\eta)\sim\eta^{-p}$ the tensor source term $A_{\rm clock}''/A_{\rm clock}=p(p+1)/\eta^{2}\to 0$ at the horizon, so the tensor equation approaches the Minkowski vacuum. The imported inflationary consistency relation $r=16\epsilon_{\rm field}$ is not assumed. Numerical integration of the native tensor equation across the finite transition profile (Step 09b) yields $r(k_{\rm pivot})=9\times 10^{-6}$ and $r_{\rm max}=6.26\times 10^{-4}$, both well below the BICEP/Keck 2021 bound $r\lt0.036$; tensor power is controlled only by the finite transition region. The late-time homogeneous expansion and acoustic observables (Planck 2018, BOSS DR12) are fully preserved by the conformal temporal mapping as mathematically confirmed in TEP-HC (Paper 18).

The causal matter-frame universe is curvature-regular at the temporal conformal boundary. The apparent Big Bang is a temporal horizon, not a physical curvature singularity. The temporal-horizon geometry supplies a nonsingular framework in which the standard background and acoustic observables are reconstructed by the conformal mapping, while TEP-BBN provides the native chemical-evolution mechanism and a proof of concept for local CMB thermalization; the scalar perturbation shape is reproduced, and the tensor-to-scalar ratio is computed from the native temporal-conformal wave equation, yielding values well below observational bounds.

Keywords: temporal equivalence principle, temporal horizon cosmology, big bang singularity, static conformal geometry, cosmology, modified gravity, temporal shear

# 1. Introduction: From Big Bang Singularity to Temporal Horizon

Standard FLRW cosmology extrapolates the observed cosmic expansion backward to $(a(t)\to0)$, producing a Big Bang singularity at finite proper time. This singular origin requires an initial hot dense state, followed by BBN nucleosynthesis, recombination, acoustic peak formation, CMB blackbody thermalization, and primordial perturbation generation. Hawking (1966) established, and Hawking and Penrose (1970) later generalized, that such a singularity is mathematically inevitable provided the Strong Energy Condition holds in globally hyperbolic spacetimes.

This paper demonstrates that the observational role of FLRW expansion is reconstructed through conformal temporal transport. In this framework, the distance-redshift relation and CMB acoustic scales are preserved in a static conformal geometry where the effective scale factor $a_{\rm eff}$ arises from accumulated open-path conformal temporal shear along cosmological lines of sight, not from physical expansion of space. The exact observational clock/redshift mapping $A_{\rm clock}(z)=(1+z)^{-1}$ drives the apparent $a_{\rm eff}\to0$ limit. The apparent $(a_{\rm eff}\to0)$ limit is therefore not a physical curvature singularity but a reconstruction artifact of imposing a globally isochronous expanding-frame description on a conformal temporal geometry.

While standard cosmology treats cosmic expansion as a kinematic stretching of the spatial metric, several frameworks have explored conformal alternatives. Wetterich (2013) demonstrated that a universe without spatial expansion can be formulated using a varying particle mass, while Narlikar and Arp explored conformal gravity variations. Environmental screening mechanisms—such as chameleon or symmetron screening (Khoury & Weltman 2004; Hinterbichler & Khoury 2010)—have been extensively developed to hide scalar fifth forces. TEP departs from these approaches by identifying the conformal factor strictly with the dynamical flow of proper time, generating an exact geometric mapping between the spatial scale factor and the macroscopic accumulation of Temporal Shear without requiring variable rest masses or modified spatial curvature.

Prior work established the empirical basis for this static conformal cosmology. TEP-C0 (Paper 26) demonstrated, through nested sampling over 1,701 Pantheon+ supernovae, that a pure conformal reconstruction exactly matches $\Lambda$CDM at the homogeneous distance-modulus level, while the physical no-$\Lambda$ temporal-shear branch improves the standardized supernova likelihood by approximately −3.4 in chi-squared for the conservative line-of-sight turnover $z_{\rm los}=5$ and approximately −7.5 for the fixed $z_{\rm los}=100$ benchmark. TEP-C0 identified full nonsingular matter-frame closure as the remaining open question for the cosmological sequence; the present paper delivers that closure for the temporal-conformal branch.

TEP-HC (Paper 18) implemented the native TEP interpretation directly in the `hi_class` Boltzmann code, deriving the runtime Bellini–Sawicki functions ($\alpha_M=-2\alpha_A$, $\alpha_B=2\alpha_A$, $\alpha_K=-5\alpha_A^2$, $\alpha_T=0$) and verifying that the static conformal geometry preserves the pre-recombination sound horizon with ratio $r_s^{\rm TEP}/r_s^{\Lambda\rm CDM} = 0.999994$ (corresponding to a $<6$ ppm deviation) with an active linear scalar perturbation sector that is stable and observationally negligible. TEP-TH closes the logical loop by demonstrating that the causal matter-frame geometry is regular at the temporal horizon, so the apparent Big Bang is not a physical singularity but an asymptotic boundary of the proper-time field.

#### Parameter-Scale and Amplitude Convention

**Turnover scales.**
**Amplitudes.** $\epsilon_{\rm field}=0.01755 denotes the primordial spectral-flow parameter constrained by $n_s$. $\epsilon_{\rm dyn}$ denotes the dynamical temporal-horizon response. $\epsilon_T^{\rm los}$ denotes the late-time line-of-sight transport amplitude fitted in TEP-C0. $\epsilon_T^{\rm CMB}$ denotes the C0 background/acoustic diagnostic amplitude. $\epsilon_T^{\rm HC}=0.00547\\pm0.00429$ denotes the native `hi_class` homogeneous conformal amplitude reported in TEP-HC. These are related projections of the same temporal sector, but they are not numerically interchangeable parameters.

In standard cosmology, epochs are conventionally defined by the chronological time elapsed since the physical singularity (e.g., "three minutes after the Big Bang" for nucleosynthesis). Because the temporal horizon in the TEP framework is an asymptotic boundary rather than a zero-volume origin, a global linear time coordinate $t$ cannot be extrapolated to a finite $t=0$. Consequently, the sequence of early-universe events is strictly mapped not by chronological time, but by the thermodynamic cooling of the plasma ($T$) and the evolution of the conformal clock-rate field. The history of the universe is preserved, but the chronological stopwatch is replaced by thermodynamic state variables.

TEP-TH addresses this early-universe question by demonstrating that the apparent Big Bang singularity is not a physical boundary but a temporal-horizon limit. The central result is that the apparent singularity corresponds to the limit $A_{\rm clock}\to0$, where the observational clock-rate field vanishes and proper time dilates to zero relative to the present epoch. The thermal history emerges natively through local thermodynamic evolution $\tilde\nabla_\mu \tilde T^{\mu\nu}=0$ in proper time, generating the CMB emission without assuming an initially hot, dense geometric singularity. The "Big Bang" is not a zero-volume, infinite-density origin of space, but a temporal horizon—an asymptotic boundary of the proper-time field.

This paper demonstrates this temporal-horizon replacement through a ten-step pipeline:

- **Temporal-Horizon Mapping**: Establish $A_{\rm clock}(z)=(1+z)^{-1}$ as the exact clock map and $A_{\rm dyn}(z)$ as the physical dynamical response

- **Matter-Frame Curvature**: Prove that for $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\lt1$, all curvature invariants generated from the Ricci sector vanish; since the Weyl tensor vanishes in the conformally flat branch, all polynomial curvature invariants vanish at the temporal conformal boundary

- **Geodesic Completeness**: Demonstrate that for $0 \lt p\le\tfrac12$ the temporal horizon is simultaneously curvature-empty, timelike-complete, and null-complete

- **Effective Stress-Energy**: Evaluate energy conditions and demonstrate Hawking-Penrose consistency via SEC violation

- **BBN Abundance Framework**: Replace expanding thermal plasma assumptions with eternal Native Proper-Time Nucleosynthesis (delegated to TEP-BBN, Paper 29) to determine asymptotic equilibrium abundances

- **Recombination Visibility**: Re-evaluate dynamic proper-time recombination $x_e(\tau)$ and derived physical acoustic scales within a steady-state asymptotic equilibrium

- **CMB Blackbody Origin**: Attribute the physical origin of the photon distribution to local emission processes and confirm conformal transport preservation

- **Entropy and Arrow of Time**: Demonstrate thermodynamic regularity at the horizon

- **Primordial Perturbation Boundary**: Derive scalar fluctuations from $\zeta=\delta\ln A_{\rm clock}$ and tensor modes from the native temporal-conformal wave equation

- **CMB Anisotropy and LSS Consistency**: Relying on TEP-HC (Paper 18) to demonstrate that TT/TE/EE spectra, matter power spectrum, growth factor, and BAO scales match Planck and BOSS

The pipeline demonstrates that the observational pillars of early-universe cosmology are natively produced by the TEP framework. The causal matter-frame universe is curvature-regular at the temporal boundary: for $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\lt1$, curvature invariants vanish at the boundary rather than merely remaining bounded; timelike proper time diverges for $0 \lt p\le 1$; null affine parameter diverges for $0 \lt p\le\tfrac12$; and the Strong Energy Condition is violated—satisfying the mathematical prerequisite established by Hawking and Penrose for a non-singular spacetime. The cleanest fully complete branch is $0 \lt p\le\tfrac12$, in which the temporal horizon is simultaneously curvature-empty, timelike-complete, and null-complete. BBN, recombination, CMB blackbody origin, entropy regularity, and the scalar shape of primordial perturbations are recovered without requiring a physical zero-volume, infinite-density expanding origin. Tensor modes are governed by a native temporal-conformal wave equation whose source term vanishes at the horizon; the imported inflationary consistency relation $r=16\epsilon_{\rm field}$ is not assumed. The apparent Big Bang is a temporal horizon, not a physical curvature singularity.

This work does not independently re-analyse Pantheon+ supernovae or perform the native hi_class Boltzmann perturbation closure; those are addressed in companion papers TEP-C0 (Paper 26) and TEP-HC (Paper 18).

The claim-discipline framework for the TEP corpus, including the scope limitations of canonical precision tests, is established in TEP-EXP (Paper 9).

# 2. Temporal-Horizon Mapping

The central temporal-horizon mapping establishes the relationship between the apparent FLRW singularity and the conformal clock-rate field. In standard FLRW cosmology, the Big Bang corresponds to the limit $a(t)\to0$ at finite proper time. In TEP, the effective scale factor is reconstructed from accumulated open-path conformal temporal shear. Two distinct projections of the temporal field are required to maintain consistency across all redshifts:

\begin{equation} \label{eq:aeff}
a_{\rm eff}(z) = A_{\rm clock}(z)\,a_{\rm m}(z) \, ,
\end{equation}

where $a_{\rm m}(z)=1$ in the clean static matter-frame case. The clock map

\begin{equation} \label{eq:A_clock}
A_{\rm clock}(z) = \frac{1}{1+z}
\end{equation}

is the exact observational clock/redshift mapping that drives $a_{\rm eff}\to0$ as $z\to\infty$. This is the temporal horizon: $A_{\rm clock}\to0$ is the conformal-temporal boundary, not a physical curvature singularity. The dynamical response

\begin{equation} \label{eq:A_dyn}
A_{\rm dyn}(z) = \left(1+\frac{z}{z_{t}}\right)^{-\epsilon_{\rm dyn}}
\end{equation}

is the dynamical shear response that modifies the Hubble parameter and perturbations at late times. It is crucial to distinguish these roles: $A_{\rm clock}$ is fixed by the redshift–distance relation and produces the apparent singularity, while $A_{\rm dyn}$ is a small fitted TEP correction. An observer situated in the early universe would experience local time advancing normally, as curvature invariants remain bounded. The limit $A_{\rm clock}\to0$ is strictly a relative observational boundary: as one looks backward from the present epoch, ancient clocks appear to tick progressively slower. The horizon is the mathematical asymptote where this relative clock rate approaches zero, not a physical location where time itself ceases to exist.

The pipeline computes both projections across redshift $z\in[0,10^{4}]$. The clock map $A_{\rm clock}(z)=(1+z)^{-1}$ reproduces the standard redshift scaling exactly, while the dynamical response $A_{\rm dyn}(z)$ approaches unity at early times. The effective Hubble parameter is therefore

\begin{equation} \label{eq:H_tep_split}
H_{\rm TEP}(z) = \frac{H_{\rm LCDM}(z)}{A_{\rm dyn}(z)} \, ,
\end{equation}

which encodes the late-time TEP shear correction. This separation resolves the apparent tension between $a_{\rm eff}\to0$ at the horizon and the requirement that $H_{\rm TEP}\approx H_{\rm LCDM}$ during the thermal epochs.

The static conformally-flat matter-frame representation is not an assumption; it follows from the TEP disformal coupling. The foundational TEP papers establish the matter coupling through $\tilde{g}_{\mu\nu}=A^{2}g_{\mu\nu}+B\,\nabla_{\mu}\phi\,\nabla_{\nu}\phi$. On the homogeneous cosmological background the field depends only on conformal time, $\phi=\phi(\eta)$, so $\nabla_{\mu}\phi=\delta_{\mu}^{0}\,\phi'$ is purely temporal. The disformal term therefore rescales only $g_{00}$, which a time reparameterisation absorbs, leaving the spatial metric unchanged and the causal metric conformally flat. The static matter frame $a_{\rm m}=1$ is the coordinate choice in which this disformal reduction is manifest.

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
A_dyn(z) = (1 + z/z_t)^(-epsilon_dyn)  # Dynamic shear response

```

Where:
- `A_clock(z)`: drives a_eff → 0 as z → ∞ (temporal horizon)
- `A_dyn(z)`: modifies expansion, BBN, recombination, perturbations at late times
- `epsilon_dyn`: baseline shear amplitude
- `z_t`: transition redshift (=100)

### Curvature Regularity

For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0<p\le\tfrac12$:
- All polynomial curvature invariants vanish at the boundary
- Timelike proper time diverges for $0<p\le 1$
- Null affine parameter diverges for $0<p\le\tfrac12$
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