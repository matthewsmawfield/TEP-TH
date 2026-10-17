# Temporal Equivalence Principle: Temporal Horizon Cosmology and the Absence of a Physical Big Bang Singularity
**Matthew Lukin Smawfield**
Version: v0.5 (Thika)
First published: 18 June 2026 - Last updated: 17 October 2026
DOI: 10.5281/zenodo.20723059

---

## Abstract

Standard FLRW cosmology extrapolates observed cosmic expansion backward to $a(t)\to0$, producing a Big Bang singularity at finite proper time. This paper demonstrates that this singularity is a reconstruction artifact of imposing a globally isochronous expanding-frame description on a conformal temporal geometry. In the Temporal Equivalence Principle (TEP), the observational role of FLRW expansion is reconstructed through conformal temporal transport: the effective scale factor $a_{\rm eff}$ arises from accumulated open-path conformal temporal shear along cosmological lines of sight rather than from physical expansion of space. TEP-C0 (Paper 26) established the distance-redshift and supernova evidence; the conditional nonsingular matter-frame boundary construction is developed here. Realization of that boundary within the complete infinite inhomogeneous solution remains the common-action construction problem of Paper 0.

The Temporal Horizon Cosmology framework is developed here, proving, within the temporal-conformal branch defined here, that the apparent $a_{\rm eff}\to0$ limit is not a physical curvature singularity but a temporal horizon. The effective scale factor $a_{\rm eff}$ is driven by the observational clock/redshift mapping $A_{\rm clock}(z)=(1+z)^{-1}$. Proposition 1 establishes curvature regularity of the temporal conformal boundary: for $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\le\tfrac12$, all polynomial curvature invariants vanish at the boundary, timelike proper time diverges, and null geodesics have divergent affine parameter. The temporal-horizon exponent $p$ and the observational clock map are independent boundary conditions: $A_{\rm clock}(z)=(1+z)^{-1}$ is fixed by the redshift definition, while the regularity condition $0 \lt p\le\tfrac12$ is a mathematical requirement for curvature-regularity at the conformal boundary. Here $\eta$ is the temporal-horizon conformal coordinate, oriented so that approach to $\mathscr{T}^{-}$ corresponds to the asymptotic limit in which $A_{\rm clock}\to0$; it is not the standard FLRW conformal time coordinate extrapolated to $a=0$. Figure 1 (Section 4.5) illustrates the resulting conformal-boundary interpretation: the singular lower edge of standard flat $\Lambda$CDM is replaced by a smooth temporal conformal boundary $\mathscr{T}^{-}$, where $A_{\rm clock}\to0$ and curvature invariants vanish. The conformal compactification is smooth, the Weyl tensor vanishes on the boundary, and every causal curve approaches the regular past boundary $\mathscr{T}^{-}$ rather than terminating at a singularity. The temporal horizon is therefore simultaneously curvature-empty, timelike-complete, and null-complete in this branch.

The effective stress-energy tensor of the temporal field violates the Strong Energy Condition, an explicit prerequisite of the Hawking-Penrose singularity theorems. Rather than treating the high-redshift hot plasma as the residue of a singular expanding origin, TEP retains that thermal state as a matter-frame condition of the temporal landscape and replaces the singular-origin interpretation with Native Local Thermodynamic Evolution in an eternal universe. The temporal-horizon metric provides the geometric boundary where the clock rate vanishes, but it does not claim to uniquely derive primordial abundances. Instead, it delegates the thermal history to the eternal chemical-evolution framework (TEP-BBN, Paper 29), which provides an eternal-universe framework in which chemical states can approach a steady-state asymptotic equilibrium where D/H is no longer uniquely primordial and helium arises through baryonic cycling. The temporal-horizon thermal mapping preserves the observed CMB photon distribution through local decoupling processes without requiring a geometric singularity.

The scalar perturbation spectrum is derived from fluctuations of the clock field, $\zeta=\delta\ln A_{\rm clock}$, yielding a power spectrum $P_{\zeta}(k)\propto k^{n_{s}-1}$ with spectral-flow parameter $n_{s}-1=-2\epsilon_{\rm field}$. The observed Planck value $n_{s}=0.9649$ constrains $\epsilon_{\rm field}=0.01755$. In the assigned tensor-pump benchmark: for $A_{\rm clock}(\eta)\sim\eta^{-p}$ the tensor source term $A_{\rm clock}''/A_{\rm clock}=p(p+1)/\eta^{2}\to 0$ at the horizon, so the tensor equation approaches the Minkowski vacuum. The imported inflationary consistency relation $r=16\epsilon_{\rm field}$ is not assumed. Numerical integration of the assigned tensor-pump equation across the finite transition profile yields $r(k_{\rm pivot})=1.9\times 10^{-9}$ and $r_{\rm max}=5.2\times 10^{-7}$, both far below the BICEP/Keck 2021 bound $r\lt0.036$; tensor power is controlled only by the finite transition region. The late-time homogeneous expansion and acoustic observables (Planck 2018, BOSS DR12) are fully preserved by the conformal temporal mapping as mathematically confirmed in TEP-HC (Paper 18).

The causal matter-frame universe is curvature-regular at the temporal conformal boundary. The apparent Big Bang is a temporal horizon, not a physical curvature singularity. The temporal-horizon geometry supplies a nonsingular framework in which the standard background and acoustic observables are reconstructed by the conformal mapping, while TEP-BBN provides the native chemical-evolution mechanism and a proof of concept for local CMB thermalization; the scalar perturbation shape is reproduced, and the tensor-to-scalar ratio is computed from the assigned temporal-conformal pump equation, yielding values well below observational bounds.

Code Availability: https://github.com/matthewsmawfield/TEP-TH

Keywords: temporal equivalence principle, temporal horizon cosmology, big bang singularity, static conformal geometry, cosmology, modified gravity, temporal shear

**Common-action scope.** The regularity and completeness results apply to the specified matter-frame metric. The scalar spectrum is reconstructed using the observed tilt and amplitude. The quoted tensor values belong to an assigned pump diagnostic; Section 10.5 distinguishes it from the tensor quadratic action of the static gravitational background. They are not yet a universal action-normalized tensor prediction or a model-wide B-mode exclusion threshold. HC's acoustic preservation and BBN's thermal/chemical calculations retain their respective reference-model and native-boundary assumptions; matching their complete transfer histories is a separate calculation.

# 1. Introduction: From Big Bang Singularity to Temporal Horizon

Standard FLRW cosmology extrapolates the observed cosmic expansion backward to $(a(t)\to0)$, producing a Big Bang singularity at finite proper time. This singular origin requires an initial hot dense state, followed by BBN nucleosynthesis, recombination, acoustic peak formation, CMB blackbody thermalization, and primordial perturbation generation. Hawking (1966) established, and Hawking and Penrose (1970) later generalized, that such a singularity is mathematically inevitable provided the Strong Energy Condition holds in globally hyperbolic spacetimes.

This paper demonstrates that the observational role of FLRW expansion is reconstructed through conformal temporal transport. In this framework, the distance-redshift relation and CMB acoustic scales are preserved in a static conformal geometry where the effective scale factor $a_{\rm eff}$ arises from accumulated open-path conformal temporal shear along cosmological lines of sight, not from physical expansion of space. The exact observational clock/redshift mapping $A_{\rm clock}(z)=(1+z)^{-1}$ drives the apparent $a_{\rm eff}\to0$ limit. The apparent $(a_{\rm eff}\to0)$ limit is therefore not a physical curvature singularity but a reconstruction artifact of imposing a globally isochronous expanding-frame description on a conformal temporal geometry.

While standard cosmology treats cosmic expansion as a kinematic stretching of the spatial metric, several frameworks have explored conformal alternatives. Wetterich (2013) demonstrated that a universe without spatial expansion can be formulated using a varying particle mass, while Narlikar and Arp explored conformal gravity variations. Environmental screening mechanisms—such as chameleon or symmetron screening (Khoury & Weltman 2004; Hinterbichler & Khoury 2010)—have been extensively developed to hide scalar fifth forces. TEP departs from these approaches by identifying the conformal factor strictly with the dynamical flow of proper time, generating an exact geometric mapping between the spatial scale factor and the macroscopic accumulation of Temporal Shear without requiring variable rest masses or modified spatial curvature.

Prior work established the empirical basis for this static conformal cosmology. TEP-C0 (Paper 26) demonstrated, through nested sampling over 1,701 Pantheon+ supernovae, that a pure conformal reconstruction exactly matches $\Lambda$CDM at the homogeneous distance-modulus level, while the physical no-$\Lambda$ temporal-shear branch — the branch carrying no bare cosmological constant in the background model — improves the standardized supernova likelihood by approximately −3.81 in chi-squared for the conservative line-of-sight turnover $z_{\rm los}=5$ and approximately −3.69 for the fixed $z_{\rm los}=100$ benchmark. TEP-C0 identified full nonsingular matter-frame closure as the remaining open question for the cosmological sequence; the present paper establishes the regular boundary of the specified temporal-conformal branch, with its common-action embedding distinguished in Section 2.1.

TEP-HC (Paper 18) implemented the native TEP interpretation directly in the `hi_class` Boltzmann code, deriving the runtime Bellini–Sawicki functions ($\alpha_M=-2\alpha_A$, $\alpha_B=2\alpha_A$, $\alpha_K=w_c\,\alpha_A^2$ with $w_c = Z_E-6$, $\alpha_T=0$) and verifying that the static conformal geometry preserves the pre-recombination sound horizon with ratio $r_s^{\rm TEP}/r_s^{\Lambda\rm CDM} = 0.999994$ (corresponding to a $<6$ ppm deviation) with an active linear scalar perturbation sector that is stable and observationally negligible on the screened production branch ($w_c = 700$; the canonical image $w_c = -5$ is linearly unstable and excluded). TEP-TH closes the logical loop by demonstrating that the causal matter-frame geometry is regular at the temporal horizon, so the apparent Big Bang is not a physical singularity but an asymptotic boundary of the proper-time field.

#### Parameter-Scale and Amplitude Convention

**Turnover scales.**

**Amplitudes.** $\epsilon_{\rm field}=0.01755$ denotes the primordial spectral-flow parameter constrained by $n_s$. $\epsilon_{\rm dyn}$ denotes the dynamical temporal-horizon response. $\epsilon_T^{\rm los}$ denotes the late-time line-of-sight transport amplitude fitted in TEP-C0. $\epsilon_T^{\rm CMB}$ denotes the C0 background/acoustic diagnostic amplitude. $\epsilon_T^{\rm HC}=0.0043\pm0.0025$ denotes the native `hi_class` homogeneous conformal amplitude from the full high-$\ell$ likelihood reported in TEP-HC. These are related projections of the same temporal sector, but they are not numerically interchangeable parameters.

In standard cosmology, epochs are conventionally defined by the chronological time elapsed since the physical singularity (e.g., "three minutes after the Big Bang" for nucleosynthesis). Because the temporal horizon in the TEP framework is an asymptotic boundary rather than a zero-volume origin, a global linear time coordinate $t$ cannot be extrapolated to a finite $t=0$. Consequently, the sequence of early-universe events is strictly mapped not by chronological time, but by the thermodynamic cooling of the plasma ($T$) and the evolution of the conformal clock-rate field. The history of the universe is preserved, but the chronological stopwatch is replaced by thermodynamic state variables.

TEP-TH addresses this early-universe question by demonstrating that the apparent Big Bang singularity is not a physical boundary but a temporal-horizon limit. The central result is that the apparent singularity corresponds to the limit $A_{\rm clock}\to0$, where the observational clock-rate field vanishes and proper time dilates to zero relative to the present epoch. The thermal history emerges natively through local thermodynamic evolution $\tilde\nabla_\mu \tilde T^{\mu\nu}=0$ in proper time, generating the CMB emission without assuming an initially hot, dense geometric singularity. The "Big Bang" is not a zero-volume, infinite-density origin of space, but a temporal horizon—an asymptotic boundary of the proper-time field.

This paper demonstrates this temporal-horizon replacement through a ten-step pipeline:

- **Temporal-Horizon Mapping**: Establish $A_{\rm clock}(z)=(1+z)^{-1}$ as the exact clock map and $A_{\rm dyn}(z)$ as the physical dynamical response

- **Matter-Frame Curvature**: Prove that for $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\lt1$, all curvature invariants generated from the Ricci sector vanish; since the Weyl tensor vanishes in the conformally flat branch, all polynomial curvature invariants vanish at the temporal conformal boundary

- **Geodesic Completeness**: Demonstrate that for $0 \lt p\le\tfrac12$ the temporal horizon is simultaneously curvature-empty, timelike-complete, and null-complete

- **Effective Stress-Energy**: Evaluate energy conditions and demonstrate Hawking-Penrose consistency via SEC violation

- **BBN Abundance Framework**: Replace expanding thermal plasma assumptions with eternal Native Proper-Time Nucleosynthesis (delegated to TEP-BBN, Paper 29) to evaluate candidate asymptotic abundance solutions

- **Recombination Visibility**: Re-evaluate dynamic proper-time recombination $x_e(\tau)$ and derived physical acoustic scales within the native eternal-universe thermodynamic framework

- **CMB Blackbody Origin**: Attribute the physical origin of the photon distribution to local emission processes and confirm conformal transport preservation

- **Entropy and Arrow of Time**: Demonstrate thermodynamic regularity at the horizon

- **Primordial Perturbation Boundary**: Derive scalar fluctuations from $\zeta=\delta\ln A_{\rm clock}$ and tensor modes from the assigned temporal-conformal pump equation

- **CMB Anisotropy and LSS Consistency**: Relying on TEP-HC (Paper 18) to demonstrate that TT/TE/EE spectra, matter power spectrum, growth factor, and BAO scales match Planck and BOSS

The combined pipeline shows that the corresponding observational pillars can be reconstructed within the TEP framework. The causal matter-frame universe is curvature-regular at the temporal boundary: for $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\lt1$, curvature invariants vanish at the boundary rather than merely remaining bounded; comoving proper time diverges for $0 \lt p\le1$, while arbitrary timelike geodesics are complete for $0 \lt p\le\tfrac12$; null affine parameter diverges for $0 \lt p\le\tfrac12$; and the Strong Energy Condition is violated—satisfying the mathematical prerequisite established by Hawking and Penrose for a non-singular spacetime. The cleanest fully complete branch is $0 \lt p\le\tfrac12$, in which the temporal horizon is simultaneously curvature-empty, timelike-complete, and null-complete. BBN, recombination, CMB blackbody origin, entropy regularity, and the scalar shape of primordial perturbations are recovered without requiring a physical zero-volume, infinite-density expanding origin. Tensor modes are governed by a assigned temporal-conformal pump equation whose source term vanishes at the horizon; the imported inflationary consistency relation $r=16\epsilon_{\rm field}$ is not assumed. The apparent Big Bang is a temporal horizon, not a physical curvature singularity.

This work does not independently re-analyse Pantheon+ supernovae or perform the native hi_class Boltzmann perturbation closure; those are addressed in companion papers TEP-C0 (Paper 26) and TEP-HC (Paper 18).

The claim-discipline framework for the TEP corpus, including the scope limitations of canonical precision tests, is established in TEP-EXP (Paper 9).

**Common-action scope.** The regularity and completeness results apply to the specified matter-frame metric. The scalar spectrum is reconstructed using the observed tilt and amplitude. The quoted tensor values belong to an assigned pump diagnostic; Section 10.5 distinguishes it from the tensor quadratic action of the static gravitational background. They are not yet a universal action-normalized tensor prediction or a model-wide B-mode exclusion threshold. HC's acoustic preservation and BBN's thermal/chemical calculations retain their respective reference-model and native-boundary assumptions; matching their complete transfer histories is a separate calculation.

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

The pipeline computes both projections across redshift $z\in[0,10^{4}]$. The clock map $A_{\rm clock}(z)=(1+z)^{-1}$ reproduces the standard redshift scaling exactly, while the dynamical response $A_{\rm dyn}(z)$ approaches zero at early times (for $\epsilon_{\rm dyn} > 0$, $(1+z/z_t)^{-\epsilon_{\rm dyn}} \to 0$ as $z \to \infty$). The effective Hubble parameter is therefore

\begin{equation} \label{eq:H_tep_split}
H_{\rm TEP}(z) = H_{\rm \Lambda CDM}(z)\,[1+\delta(z)] \, ,
\end{equation}

which encodes the late-time TEP shear correction. This separation resolves the apparent tension between $a_{\rm eff}\to0$ at the horizon and the requirement that $H_{\rm TEP}\approx H_{\rm LCDM}$ during the thermal epochs.

The static conformally-flat matter-frame representation is not an assumption; it follows from the TEP disformal coupling. The foundational TEP papers establish the universal matter coupling through the canonical unified metric $\tilde{g}_{\mu\nu}=-A_{\rm loc}^2(u_{\rm grav}(\mathbf x))U_\mu U_\nu+A_{\rm sp}^2(u_{\rm drift}(t,\mathbf x))\Pi_{\mu\nu}+B(\phi)\Pi_\mu^\alpha\Pi_\nu^\beta\nabla_\alpha\phi\nabla_\beta\phi$ ($U_\mu\equiv-\nabla_\mu\bar\phi/\sqrt{2\bar X}$, $\Pi_{\mu\nu}=g_{\mu\nu}+U_\mu U_\nu$; Paper 0, §2.2, Step 80), written in conformal–disformal shorthand as $\tilde{g}_{\mu\nu}=A^{2}g_{\mu\nu}+B\,\nabla_{\mu}\phi\,\nabla_{\nu}\phi$. On the homogeneous cosmological background ($u_{\rm grav}=0$, $\Pi_\mu^\alpha\nabla_\alpha\phi=0$), $d\tilde s^2=-c^2dt^2+A_{\rm sp}^2(t)\gamma_{ij}dx^i dx^j$, which in conformal propagation time $d\eta=dt/A_{\rm sp}(t)$ takes the conformally flat form $d\tilde s^2=A_{\rm clock}^2(\eta)(-c^2d\eta^2+\gamma_{ij}dx^i dx^j)$ with $A_{\rm clock}\equiv A_{\rm sp}$. The static gravitational frame $a_{\rm m}=1$ is the coordinate choice in which this reduction is manifest.

The spatial homogeneity of this background represents the macroscopic averaging limit of a locally structured temporal field. While the local conformal factor deviates symmetrically above and below unity as it traverses halos and voids (Paper 0, §2.2), the spatial integration of these exact excursions recovers the smooth $\phi(\eta)$ dependence. The perfectly homogeneous background is therefore an effective macroscopic envelope, explicitly separated from the non-exact covariance $\mathcal{C}_T$ (Paper 26) that accumulates as a physical residual along specific lines of sight.

## 2.1 Sector Consistency with Foundational TEP

The foundational TEP metric is conformal-disformal,

\begin{equation}
\tilde{g}_{\mu\nu} = A^{2}(\phi)\,g_{\mu\nu} + B(\phi)\,\nabla_{\mu}\phi\,\nabla_{\nu}\phi \, .
\end{equation}

The present paper studies the homogeneous cosmological projection of this structure. On an FLRW background ($\phi=\phi(\eta)$), the disformal term is purely temporal and can be absorbed into the lapse by a time reparameterisation. The resulting temporal-horizon theorem is therefore a theorem of the conformal clock-rate sector ($A_{\rm clock}$), not a derivation of the non-exact synchronization-holonomy sector.

This distinction is essential. Open-path temporal transport,

\begin{equation}
\Delta\ln A = \int_{\gamma} d\ln A \, ,
\end{equation}

can generate cosmological redshift and the apparent scale-factor reconstruction. Closed-loop residual synchronization holonomy, however, obeys

\begin{equation}
\oint d\ln A = 0
\end{equation}

for smooth single-valued conformal transport. Therefore TEP-TH does not claim that $A_{\rm clock}$ alone generates nonzero closed-loop holonomy. Nonzero residual holonomy requires disformal or otherwise non-exact synchronization curvature, as developed in the foundational TEP paper (Jakarta). The temporal-horizon result and the synchronization-holonomy programme are complementary probes of different sectors of the same causal matter metric. The homogeneous temporal-shear background contribution $\Omega_\phi$ (TEP-HC, Paper 18) fills the same cosmological background budget as $\Omega_\Lambda$ — an operational bookkeeping of the conformal sector's distance-law role, not a literal vacuum energy density, whose value $\Omega_\phi\simeq0.697$ follows without fitting from the Paper 18 fixed point and spatial flatness (the action-level vacuum plateau is quantified in Section 5.1, where $U_{\rm c}/\rho_{\rm crit,0}\approx1.8\times10^{-3}$) — while the non-exact covariance/topology correction $C_T$ (TEP-C0, Paper 26) provides the transport closure for the open-path redshift reconstruction beyond exact conformal shear.

The redshift map and the conformal-time horizon profile are linked by $A_{\rm clock}(z)=(1+z)^{-1}$ and $A_{\rm clock}(\eta)=C\eta^{-p}$, which together imply

\begin{equation} \label{eq:z_eta}
1+z(\eta) = C^{-1}\eta^{p} \, .
\end{equation}

This relation connects the observational redshift coordinate — the epoch label under which events are ordered — to the conformal time parameter in which the curvature and geodesic theorems are proved. The constant $C$ is fixed by the condition $A_{\rm clock}=1$ at the present epoch ($z=0$, $\eta=\eta_{0}$), giving $C=\eta_{0}^{-p}$.

The scope of $\eqref{eq:z_eta}$ must be stated precisely, because it composes two objects of different standing. The clock map $A_{\rm clock}(z)=(1+z)^{-1}$ is the exact observational clock-ratio definition of redshift; the horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ is the asymptotic form of the homogeneous ambient envelope, i.e. the boundary structure on which the completeness theorems operate. Their composition is therefore the internal epoch map of the homogeneous theorem branch: it assigns to a conformal position $\eta$ the clock-ratio coordinate that a strictly homogeneous realization would measure at that depth. It is not the realized distance–redshift relation. Two features of the transport architecture prevent that identification. First, the composition retains only the exact conformal sector of open-path transport, whose path integral reduces to the endpoint ratio $\Delta\ln A$; on the realized landscape the observed redshift is the full transport integral $\ln(1+z_{T})=\int_{\gamma}(\Sigma_{\parallel}+\mathcal{C}_{T,\parallel})\,d\ell$ of TEP-C0 (Paper 26), in which the non-exact covariance term $\mathcal{C}_{T}$ accumulates along the sightline without cancelling and the emission-side clock ratio carries the depth of the source's own temporal well — so the observed redshift is a functional of the realized field history, not of the homogeneous envelope value at the endpoint. Second, the power-law profile is the $\eta\to\infty$ asymptote that the curvature and completeness theorems constrain; the finite-$\eta$ behaviour of the branch is the transition-profile sector of Section 10, which departs from the asymptote precisely in the regime in which finite-redshift transport is evaluated. The luminosity distance in the static background remains the Etherington combination $d_{L}=(1+z)\,\Delta\eta$ — distance duality is preserved by the conformal construction — but the redshift entering it is the realized transport quantity, whose distance–redshift relation is computed on the landscape in TEP-C0 and TEP-HC (Papers 26 and 18) and reproduces the observed relation at the homogeneous-observable level. No law $d_{L}\propto(1+z)^{1+1/p}$ therefore follows from the homogeneous branch: such an expression results from substituting the internal epoch map into the distance formula, thereby identifying the theorem's coordinate parameter with a transport observable. Where this paper and its companions state that the distance–redshift relation is preserved, the claim is thereby scoped to the realized transport sector, to which the homogeneous $\Delta\eta$ does not reduce.

*Relation to the canonical background branch.* Two horizon asymptotics are distinguished within the framework, and they are not equivalent. The exactly solved closed-static benchmark solution (Paper 0, §8) approaches the temporal horizon exponentially in gravitational coordinate time, $A\propto\exp(\sqrt{2}\,t/a)$, accumulating only a finite matter-frame clock history while matter-frame curvature invariants diverge as $A^{-2}$. Because matter and clocks propagate on $\tilde g$, finite-proper-time termination with diverging scalar invariants is geodesic incompleteness in the matter frame: the benchmark realizes the singular branch, the asymptotic on which the standard hot-Big-Bang reading is correct. The power-law family analyzed in this paper, $A_{\rm clock}(\eta)=C\eta^{-p}$, realizes the qualitatively different regular branch: a curvature-empty conformal boundary with divergent accumulated proper time, for which the completeness results below are established. The two branches are therefore distinct causal completions selected by the scalar sector, not alternative descriptions of one phenomenology. The regular branch is not merely postulated: Section 10.2 derives a cosmological clock-field action — reconstructed kinetic function $\mathcal Z(\chi)$ and potential $U(\chi)$ — for which the power-law profile is an exact background solution of the Euler–Lagrange equation (Section 10.2a). What remains open is embedding that effective cosmological action in the two-metric master action, i.e. deriving $\mathcal Z(\chi)$ and $U(\chi)$ from the fundamental scalar sector; that derivation would promote the regular branch from an exactly solved effective-sector solution to a derived background of the full theory.

# 3. Matter-Frame Geometry and Curvature Regularity

To determine whether the temporal horizon is a physical singularity or a reconstruction artifact, matter-frame curvature invariants are computed. In the causal matter frame the metric is $\tilde{g}_{\mu\nu} = A_{\rm clock}^{2}(\eta)\,g_{\mu\nu}$, where $g_{\mu\nu}$ is the static conformal background and $A_{\rm clock}(\eta)$ is the conformal clock-rate field. The key question is whether curvature invariants remain finite as $A_{\rm clock}\to0$, and whether they in fact vanish for a suitable horizon profile.

The effective scale factor observed by matter is not the raw conformal factor but the product

\begin{equation} \label{eq:aeff_matter}
a_{\rm eff} = A_{\rm clock}\,a_{\rm m} \, ,
\end{equation}

where $a_{\rm m}=1$ in the clean static matter-frame case. The apparent FLRW limit $a_{\rm eff}\to0$ is driven by $A_{\rm clock}\to0$, while the underlying matter-frame coordinate scale factor $a_{\rm m}$ remains finite and non-zero. Consequently the physical matter-frame metric determinant is

\begin{equation} \label{eq:metric_det}
\det(\tilde{g}_{\mu\nu}) = A_{\rm clock}^{8}\,\det(g_{\mu\nu}) = -A_{\rm clock}^{8}\,a_{\rm m}^{6} \, .
\end{equation}

In four spacetime dimensions every metric component acquires a factor $A_{\rm clock}^{2}$, giving $A_{\rm clock}^{8}$ in the determinant. Because $a_{\rm m}$ does not collapse to zero, $\det(\tilde{g})$ vanishes only if $A_{\rm clock}\to0$ with no compensating behaviour. The determinant alone does not prove regularity; one must show that the *physical* volume element, constructed from the inverse metric and the relevant measure, does not degenerate in a way that produces divergent curvature.

The full four-dimensional conformal transformation of the Ricci scalar for $\tilde{g}_{\mu\nu}=A_{\rm clock}^{2}\,g_{\mu\nu}$ is

\begin{equation} \label{eq:ricci_scalar_full}
\tilde{R} = A_{\rm clock}^{-2}\Bigl[ R - 6\,\Box\ln A_{\rm clock} - 6\,(\nabla\ln A_{\rm clock})^{2} \Bigr] \, .
\end{equation}

Equivalently, writing everything in terms of $A_{\rm clock}$ itself,

\begin{equation} \label{eq:ricci_scalar_A}
\tilde{R} = A_{\rm clock}^{-2}R - 6A_{\rm clock}^{-3}\Box A_{\rm clock} \, .
\end{equation}

In the TEP static background $g_{\mu\nu}$ has $R=0$ and $\nabla A_{\rm clock}$ is spatially homogeneous, so the surviving terms are controlled by the background profile $A_{\rm clock}(\eta)$. For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\lt1$, the dominant term is $\tilde{R}=6A_{\rm clock}''/A_{\rm clock}^{3}=6p(p+1)C^{-2}\eta^{2p-2}$, which vanishes as $\eta\to\infty$.

The Kretschmann scalar and Ricci-tensor square transform with additional powers of $A_{\rm clock}^{-1}$. For a conformally flat static background the Weyl tensor vanishes, so the full Riemann tensor is built from the Ricci tensor. The conformal transformation of $\tilde{R}_{\mu\nu}$ (Wald, App. D) with $\ln A_{\rm clock}=\ln C-p\ln\eta$ and the static flat background gives the closed-form Ricci-tensor invariant

\begin{equation}
\tilde{R}_{\mu\nu}\tilde{R}^{\mu\nu} = 12p^{2}\bigl(p^{2}+p+1\bigr)\,\frac{\eta^{4p-4}}{C^{4}} \, .
\end{equation}

The Kretschmann invariant in the zero-Weyl case is $\tilde{K}=2\tilde{R}_{\mu\nu}\tilde{R}^{\mu\nu}-\tfrac13\tilde{R}^{2}$, which evaluates to

\begin{equation} \label{eq:kretschmann}
\tilde{K} = 12p^{2}\left(p^{2}+1\right)\frac{\eta^{4p-4}}{C^{4}} \, .
\end{equation}

For $0 \lt p\lt1$, the factor $\eta^{4p-4}\to0$ as $\eta\to\infty$, so both the Kretschmann scalar and the Ricci-tensor invariant vanish at the boundary with an explicit polynomial prefactor in $p$. The scaling is not approximate; it is a closed-form result derived from the conformal transformation of the Ricci tensor on the static background.

## 3.1 Proposition 1 — Curvature Regularity of the Temporal Conformal Boundary

**Proposition 1 (Curvature regularity of the temporal conformal boundary).** Let the observational effective scale factor be $a_{\rm eff}=A_{\rm clock}\,a_{\rm m}$ with $a_{\rm m}$ the finite, non-zero matter-frame coordinate scale factor. Let the clock field take the temporal-horizon profile $A_{\rm clock}(\eta)\sim\eta^{-p}$ in conformal time with $0 \lt p\lt1$. Then, as $\eta\to\infty$ ($A_{\rm clock}\to0$):

- The Ricci scalar $\tilde{R}$ in the matter frame vanishes: $\tilde{R}\sim\eta^{2p-2}\to0$.

- The Kretschmann scalar $\tilde{K}$ and Ricci-tensor invariant $\tilde{R}_{\mu\nu}\tilde{R}^{\mu\nu}$ vanish: $\tilde{K}\sim\tilde{R}_{\mu\nu}\tilde{R}^{\mu\nu}\sim\eta^{4p-4}\to0$.

- The observational conformal volume element $V_{\rm eff}=A_{\rm clock}^{3}a_{\rm m}^{3}$ tends to zero, but this is not a physical collapse of the underlying matter-frame spatial geometry. It reflects the degeneracy of the observational clock/redshift map at the temporal horizon. The finite coordinate scale $a_{\rm m}$ and vanishing curvature invariants show that the boundary is a conformal-temporal endpoint, not a zero-volume curvature singularity.

*Proof sketch.* Substitute $A_{\rm clock}(\eta)=C\eta^{-p}$ into equations $\eqref{eq:ricci_scalar_full}$–$\eqref{eq:kretschmann}$. In the static conformal background $R=0$ and spatial gradients vanish by homogeneity. The time derivatives scale as $A_{\rm clock}'\sim -pC\eta^{-p-1}$ and $A_{\rm clock}''\sim p(p+1)C\eta^{-p-2}$. The Ricci scalar $\eqref{eq:ricci_scalar_A}$ contains terms $A_{\rm clock}^{-2}R$ and $A_{\rm clock}^{-3}\Box A_{\rm clock}$. With $R=0$ and homogeneity, the dominant term is $6A_{\rm clock}''/A_{\rm clock}^{3}=6p(p+1)C^{-2}\eta^{2p-2}\to0$ for $0 \lt p\lt1$. The Ricci-tensor invariant has coefficient $12p^{2}(p^{2}+p+1)/C^{4}$ and the Kretschmann invariant has coefficient $12p^{2}(p^{2}+1)/C^{4}$, which satisfy the zero-Weyl identity $\tilde{K}=2\tilde{R}_{\mu\nu}\tilde{R}^{\mu\nu}-\tfrac13\tilde{R}^{2}$; both are strictly positive for all $p>0$ and scale as $\eta^{4p-4}\to0$ for $0 \lt p\lt1$. Numerical evaluation reproduces the analytic decay laws on the tested range; the vanishing limit is established by their negative powers of $\eta$. $\square$

For $p\le\tfrac12$ the Kretschmann scalar falls faster than $\eta^{-2}$, ensuring that null affine parameters diverge (Section 4.2).

*Scope of the $R=0$ hypothesis.* The proposition's background-flatness assumption is quantitative, not merely qualitative. Writing a residual background scalar as $R(\eta)=R_0\,\eta^{-s}$, the transformed term $A_{\rm clock}^{-2}R\sim R_0\,\eta^{2p-s}$ is bounded if and only if $s\ge2p$ and vanishes toward the boundary for $s>2p$: background curvature must decay toward the temporal horizon faster than $\eta^{-2p}$. Two sources organise the answer. A fixed curvature offset ($s=0$) — e.g., a cosmological-constant-like floor in the background — is excluded for every $p>0$; such a floor would convert the vanishing invariants into divergent ones. Curvature sourced by the clock field itself decays as $R_{\rm kin}\sim\varphi'^2\sim\eta^{-2}$ (since $A_{\rm clock}=e^{\beta_A\varphi/M_{\rm Pl}}=\eta^{-p}$ gives $\varphi\propto\ln\eta$), so $s=2$ satisfies the vanishing condition for every $p<1$; it falls in step with the $\eta^{2p-2}$ gradient terms whenever $p<1$. The proposition therefore stands precisely for backgrounds whose residual curvature decays at least as fast as the clock field's own kinetic trace, and fails only for a non-decaying background floor — a scope statement verified numerically across the $(p,s)$ plane by the bounded sensitivity calculation of the pipeline's curvature-sensitivity step.

This establishes the temporal boundary as a regular conformal endpoint, adopting the mathematical architecture of Penrose's conformal compactification and null infinity ($\mathscr{I}^{+}$) (Penrose 2006; Tod 2003, 2015), here applied to the asymptotic past. The boundary is not a curvature singularity; it is a conformal-temporal boundary where the Lorentzian metric becomes degenerate in the observational clock frame. The vanishing of curvature invariants is necessary but not sufficient for regularity: a degenerate metric admits no inverse, so the geodesic equation becomes singular at the boundary. Geodesic completeness is established not by the curvature invariants alone but by the affine-parameter analysis of Section 4: timelike proper time diverges for $0 < p \le 1$ and null affine parameter diverges for $0 < p \le \tfrac{1}{2}$, so no causal curve reaches the boundary in finite parameter. The boundary is therefore a regular asymptotic endpoint of the conformal compactification, not an interior point of the manifold; the metric degeneracy is a feature of the conformal frame, not a pathology of the physical geometry.

It is vital to distinguish the TEP temporal horizon ($\mathscr{T}^{-}$) from Penrose's Conformal Cyclic Cosmology (CCC). Where CCC posits an infinite sequence of aeons connected by conformal rescalings at $\mathscr{I}^{+}$ and $\mathscr{I}^{-}$, TEP does not invoke cyclicality. $\mathscr{T}^{-}$ functions as a strict, non-singular asymptotic past boundary for a single, continuous causal history, dictated by the vanishing of the relative conformal clock rate.

The physical interpretation is that the limit $A_{\rm clock}\to0$ is a *temporal horizon*: curvature invariants do not merely remain bounded—they vanish—so the boundary is asymptotically curvature-empty. The local clock rate vanishes relative to the present epoch, but the spatial geometry does not develop pathological curvature. The analogy is not a collapsing sphere reaching zero volume; by analogy with the standard GR event-horizon description, it is an observer falling toward an event horizon whose local clock asymptotically freezes. The causal structure remains intact. Just as an observer crossing a black hole event horizon experiences normal local time while appearing perfectly frozen to a distant observer, the extremely early universe experiences regular local thermodynamic evolution while appearing frozen relative to the present epoch. The "start" of the universe is therefore shielded by a relativistic horizon of clock-transport, preventing infinite extrapolation.

## 3.2 Disformal Compensation Analysis

A natural question is whether the disformal sector of the TEP matter metric, $\tilde{g}_{\mu\nu}=A^{2}g_{\mu\nu}+B(\phi)\nabla_{\mu}\phi\nabla_{\nu}\phi$, can prevent the metric degeneracy at the temporal horizon. The determinant of the full disformal metric is

\begin{equation} \label{eq:disformal_det}
\det(\tilde{g}_{\mu\nu}) = A^{8}\,\det(g_{\mu\nu})\left(1 + \frac{B\,(\nabla\phi)^{2}}{A^{2}}\right) \, ,
\end{equation}

The contraction is signed. On the homogeneous background $(\nabla\phi)^2=-(\phi')^2$, so the determinant factor is $1-B(\phi')^2/A^2$. For the declared product ansatz $|B(\phi')^2|=C_B A^{-2n}$, the negative-$B$ branch has

\begin{equation}
\tilde N^2=A^2+C_B A^{-2n},\qquad
\det\tilde g=-\tilde N^2A^6=-A^8-C_B A^{6-2n}.
\end{equation}

Thus the coordinate determinant tends to zero for $n<3$, to $-C_B$ for $n=3$, and diverges for $n>3$. A finite determinant is not sufficient to establish a smooth extension of all metric components at the boundary. Step 01 evaluates the same lapse and spatial factor in both the determinant and curvature calculation, for the existing powers $n\in\{2,3,4,5,6,10\}$.

With $A=\eta^{-p}$, write $\mathcal H=A'/A=-p/\eta$ and $H=\mathcal H/\tilde N$. The invariant curvature of $d\tilde s^2=-\tilde N^2d\eta^2+A^2d\mathbf x^2$ is

\begin{equation}
\tilde R=\frac{6}{\tilde N^2}\left(\mathcal H'+2\mathcal H^2-\mathcal H\frac{\tilde N'}{\tilde N}\right).
\end{equation}

On the negative-$B$ branch, $\tilde N'/\tilde N\sim np/\eta$, giving $\tilde R\sim6[p+(n+2)p^2]C_B^{-1}\eta^{-2-2np}\to0$ for $n>0$. This is a curvature invariant, not a coordinate artifact. The lapse remains positive at every finite $\eta$; its divergence at the asymptotic boundary alone does not prove a physical pathology. For the tested $n\ge2$, comoving proper time $\int\tilde N\,d\eta$ and null affine length $\int A\tilde N\,d\eta$ both diverge at the boundary. These metric-level facts do not derive $B(\phi)$ from the common action or establish its observational viability.

Positive $B$ instead gives $\tilde N^2=A^2-C_B A^{-2n}$, with a signature-change surface $A_\times=C_B^{1/(2n+2)}$. A Lorentzian present reference at $A=1$ requires $C_B<1$; the growing ansatz then encounters the surface before $A\to0$. The two signs therefore have different geometric verdicts. The pure conformal branch remains the branch used for this paper's main regularity and completeness theorems; neither the negative-$B$ comparison nor its rejection is needed for those results.

The pipeline confirms this analysis. In pure conformal closure ($B=0$), Proposition 1 is verified: $|\tilde{R}|\approx3.36\times10^{-18}$ and $|\tilde{K}|\approx2.23\times10^{-36}$ at $z=10^{6}$ for $p=0.4$ in the normalized profile, and the $p$-sensitivity test confirms vanishing for all $0<p\le\tfrac12$. The disformal test reproduces the exact metric determinant, whose finite-magnitude exponent is $n=3$, and the bounded curvature of its negative-$B$ comparison branch. Neither test promotes that assigned coupling to the common action. The metric degeneracy in pure conformal closure is therefore not a pathology to be cured by the disformal sector; it is the defining feature of the conformal boundary, exactly as in Penrose's conformal compactification of null infinity.

# 4. Geodesic Completeness

A key test for physical singularities is geodesic incompleteness. Null and timelike geodesics are integrated backward from the present epoch toward the temporal horizon. For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\le\tfrac12$, both null and timelike geodesics are complete: the null affine parameter diverges and the timelike proper time diverges. Comoving timelike observers accumulate infinite proper time for $0 \lt p\le1$; timelike geodesics with nonzero conserved spatial momentum require $p\le\tfrac12$, the same bound as null completeness. The boundary is curvature-empty in this branch.

Here $\eta$ is the temporal-horizon conformal coordinate, oriented so that approach to $\mathscr{T}^{-}$ corresponds to the asymptotic limit in which $A_{\rm clock}\to0$. It is not the standard FLRW conformal time coordinate extrapolated to $a=0$.

## 4.1 Conformal Christoffel Symbols

Under the conformal transformation $\tilde{g}_{\mu\nu}=A_{\rm clock}^{2}\,g_{\mu\nu}$, the Christoffel symbols transform as

\begin{equation} \label{eq:christoffel}
\tilde{\Gamma}^{\mu}{}_{\alpha\beta}
= \Gamma^{\mu}{}_{\alpha\beta}
+ \delta^{\mu}_{\alpha}\,\partial_{\beta}\ln A_{\rm clock}
+ \delta^{\mu}_{\beta}\,\partial_{\alpha}\ln A_{\rm clock}
- g_{\alpha\beta}\,g^{\mu\nu}\,\partial_{\nu}\ln A_{\rm clock} \, .
\end{equation}

For the static conformal background $g_{\mu\nu}$ with $\partial_{i}A_{\rm clock}=0$ and $A_{\rm clock}=A_{\rm clock}(t)$, the nonzero modified symbols are

\begin{equation}
\tilde{\Gamma}^{0}{}_{00} = \frac{\dot{A}_{\rm clock}}{A_{\rm clock}} \, , \qquad
\tilde{\Gamma}^{0}{}_{ij} = \frac{\dot{A}_{\rm clock}}{A_{\rm clock}}\,\delta_{ij} \, , \qquad
\tilde{\Gamma}^{i}{}_{0j} = \frac{\dot{A}_{\rm clock}}{A_{\rm clock}}\,\delta^{i}_{j} \, ,
\end{equation}

where overdots denote derivatives with respect to the conformal time of the background. These corrections encode how the varying clock rate modifies geodesic acceleration.

## 4.2 Null Geodesics and Affine Length

For radial null geodesics on the static gravitational background ($a_g=1$, with matter metric $\tilde g=A_{\rm clock}^2g$), the geodesic equation with the corrected Christoffels gives

\begin{equation} \label{eq:null_geodesics}
\frac{d\eta}{d\tilde{\lambda}} = \frac{1}{A_{\rm clock}^{2}(\eta)} \, , \qquad
\frac{dr}{d\tilde{\lambda}} = \frac{\pm 1}{A_{\rm clock}^{2}(\eta)} \, ,
\end{equation}

where $\tilde{\lambda}$ is the affine parameter in the matter frame. A standard result for conformally related metrics is that if $k^{\mu}=dx^{\mu}/d\lambda_{0}$ is an affinely parametrized null geodesic of the background $g_{\mu\nu}$, then the same path is an affinely parametrized null geodesic of $\tilde{g}_{\mu\nu}=A_{\rm clock}^{2}g_{\mu\nu}$ with parameter $\tilde{\lambda}$ obeying $d\tilde{\lambda}=A_{\rm clock}^{2}\,d\lambda_{0}$ (in four dimensions). The background is static and nonsingular, so $\lambda_{0}$ ranges over $(-\infty,\infty)$. The matter-frame affine parameter to any background coordinate time $t$ is therefore

\begin{equation} \label{eq:affine_null}
\tilde{\lambda}(t) = \int^{t} A_{\rm clock}^{2}(\lambda_{0})\,d\lambda_{0}
= \int^{t} A_{\rm clock}^{2}(\eta)\,d\eta \, ,
\end{equation}

where $\eta$ is the background coordinate time. For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\lt1$ as $\eta\to\infty$ (early times), the integrand behaves as $\eta^{-2p}$. The integral $\int^{\infty}\eta^{-2p}\,d\eta$ diverges for $2p\le 1$, i.e. for $0 \lt p\le\tfrac12$. Null geodesics do not terminate in this branch; they extend to $\tilde{\lambda}\to\infty$. For $\tfrac12\lt p \lt 1$ the null affine parameter converges, so null completeness requires $p\le\tfrac12$.

The divergence rates are explicit. Evaluating the integral with a lower cutoff $\eta_{0}\sim\mathcal{O}(1)$,

\begin{equation} \label{eq:null_divergence}
\tilde{\lambda}(\eta)=\int_{\eta_{0}}^{\eta}C^{2}\eta'^{-2p}\,d\eta'=\frac{C^{2}}{1-2p}\Bigl(\eta^{1-2p}-\eta_{0}^{1-2p}\Bigr)\quad(p\neq\tfrac12) \, ,
\end{equation}

so that for $p<\tfrac12$ the null affine parameter diverges as a power law, $\tilde{\lambda}\propto\eta^{1-2p}\to\infty$. At the marginal value $p=\tfrac12$,

\begin{equation} \label{eq:null_log}
\tilde{\lambda}(\eta)=C^{2}\,\ln\!\left(\frac{\eta}{\eta_{0}}\right) \to \infty \quad (p=\tfrac12) \, ,
\end{equation}

diverging only logarithmically. The slower divergence at $p=\tfrac12$ is still sufficient for past-completeness; every finite segment of a null geodesic accumulated since any finite $\eta_{0}$ requires infinite affine parameter to reach $\mathscr{T}^{-}$.

## 4.3 Timelike Geodesics and Proper Time

For timelike geodesics the conformal transformation rescales proper time as $d\tilde{\tau}=A_{\rm clock}\,d\tau$. In the static background a comoving observer has $d\tau=d\eta$, so the total matter-frame proper time from early time $\eta_{i}$ to the present is

\begin{equation} \label{eq:timelike_proper}
\tilde{\tau}_{\rm total} = \int_{\eta_{i}}^{\eta_{0}} A_{\rm clock}(\eta)\,d\eta \, .
\end{equation}

For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\lt1$, the integral $\int^{\infty}\eta^{-p}\,d\eta$ *diverges* because $p\le 1$. Comoving proper time to the temporal boundary is therefore *infinite*. This establishes the comoving result; completeness of arbitrary timelike geodesics requires the momentum-dependent calculation below. In TEP, Proposition 1 guarantees that all curvature invariants *vanish* at the temporal horizon for $0 \lt p\lt1$, so the infinite proper time reflects that observers can continue evolving indefinitely while the geometry becomes asymptotically curvature-empty.

The timelike divergence is also explicit:

\begin{equation} \label{eq:timelike_divergence}
\tilde{\tau}(\eta)=\int_{\eta_{0}}^{\eta}C\eta'^{-p}\,d\eta'=\frac{C}{1-p}\Bigl(\eta^{1-p}-\eta_{0}^{1-p}\Bigr)\quad(p\neq1) \, ,
\end{equation}

which diverges as a power law $\tilde{\tau}\propto\eta^{1-p}\to\infty$ for all $0\lt p\lt1$. The comoving bound $p\le1$ is weaker than the bound for general timelike geodesics. With conserved spatial momentum $q_i=A_{\rm clock}^2 dx^i/d\tilde\tau$ and $q^2=\delta^{ij}q_iq_j$, normalization gives $$\frac{d\tilde\tau}{d\eta}=\frac{A_{\rm clock}^2}{\sqrt{A_{\rm clock}^2+q^2}}.$$ For $q=0$ this reduces to $A_{\rm clock}$. For any fixed $q\neq0$, the asymptotic integrand is $A_{\rm clock}^2/|q|\propto\eta^{-2p}$, so arbitrary timelike geodesics are complete precisely for $p\le\tfrac12$. The adopted complete branch therefore satisfies both the timelike and null tests. The geodesic equations in the matter frame are regular everywhere:

\begin{equation} \label{eq:timelike_geodesics}
\frac{d^{2}x^{\mu}}{d\tilde{\tau}^{2}} + \tilde{\Gamma}^{\mu}{}_{\alpha\beta}\frac{dx^{\alpha}}{d\tilde{\tau}}\frac{dx^{\beta}}{d\tilde{\tau}} = 0 \, ,
\end{equation}

with $\tilde{\Gamma}$ given by $\eqref{eq:christoffel}$. Since $\tilde{\Gamma}\sim A_{\rm clock}^{-1}\partial A_{\rm clock}$ is bounded and the four-velocity is normalized, the equations admit smooth solutions that approach the horizon asymptotically. Step 02 integrates the null affine length and momentum-dependent timelike proper time in $\ln\eta$, checking the finite segments against the closed-form null and comoving integrals and independent timelike quadrature. The controls include $p=\tfrac12$, where affine length grows logarithmically, and $p>\tfrac12$, where null and moving-observer proper time converge. Infinite-end completeness is assigned by the analytic integrability criterion above, rather than by a numerical endpoint or an imposed small-value threshold.

## 4.4 Geodesic Completeness Theorem

**Theorem (Temporal-horizon geodesic completeness).** Let the conformal clock field take the profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\le\tfrac12$. Then:

- Comoving proper time diverges for $0 \lt p\le1$; all timelike geodesics, including those with nonzero spatial momentum, have divergent proper time for $0 \lt p\le\tfrac12$.

- Null affine parameter to the temporal boundary diverges for $0 \lt p\le\tfrac12$.

- All polynomial curvature invariants vanish at the boundary for $0 \lt p\lt1$, hence in particular for $0 \lt p\le\tfrac12$.

- The tensor source term $A_{\rm clock}''/A_{\rm clock}=p(p+1)/\eta^{2}\to 0$ at the boundary.

The cleanest fully complete temporal-horizon branch is therefore $0 \lt p\le\tfrac12$. In this branch the temporal horizon is simultaneously curvature-empty, timelike-complete, and null-complete.

Proposition 1 establishes regularity for the temporal-conformal branch satisfying $0 \lt p\le\tfrac12$. The temporal-horizon exponent $p$ and the observational clock map are independent boundary conditions: $A_{\rm clock}(z)=(1+z)^{-1}$ is fixed by the redshift definition, while the regularity condition $0 \lt p\le\tfrac12$ is a mathematical requirement for curvature-regularity at the conformal boundary. The profile $A_{\rm clock}\sim\eta^{-p}$ with $p=1$ reproduces a familiar FLRW scaling — the radiation-era clock map $a\propto\eta$ — but that branch ($p=1$) lies outside the curvature-regular window. Within TEP, the regular branch is selected by the requirement that the matter-frame geometry be curvature-regular at the temporal horizon, not by the observational redshift mapping alone.

Three structural points sharpen the status of the branch index $p$. First, the power-law completeness window $p\le\tfrac12$ can also be expressed as $|\mathcal H_{\rm eff}'|/\mathcal H_{\rm eff}^{2}\ge2$, or as $|\dot H_{\rm clock}|/H_{\rm clock}^{2}\ge1$ using matter proper time (Section 10.2b). These equivalent geometric bounds do not establish a kinetic-dominated equation of state or independently select the background. Second, $p$ is the family index of the reconstructed single-clock action of Section 10.2: each member $(\mathcal Z_p, U_p)$ is reconstructed around its own exponent and realizes that power law exactly, so the theorem is a property of every member of the branch rather than of a single fitted trajectory; which member the corpus's canonical closure dynamics realizes is the same open asymptotic determination as the master-action embedding identified in Section 2 (the branch-index datum). Third, the index is observable in principle through the tensor diagnostic surface of Section 10.6: along the one-parameter fiducial slice ($n=4$, $\eta_0=14{,}000$ Mpc), the Step 09b computation returns $r_{\rm max}(p)\approx 6.1\times10^{-5}\,p^{2}$ at the transition scale ($\le 1.4\times10^{-5}$ for $p\le\tfrac12$, while joint variations such as $p=0.5$, $n=2$, $\eta_0=3000$ Mpc reach $1.14\times10^{-4}$), so the completeness claim is branch-robust and primordial tensor observations at $k\sim2\times10^{-4}\ {\rm Mpc}^{-1}$ constrain the joint transition-profile parameters $(p, n, \eta_0)$ once the tensor action normalization is fixed.

## 4.5 Conformal Compactification and Penrose-Style Diagram

To illustrate the temporal boundary in the language of standard conformal diagrams, a Penrose-style compactified conformal diagram is constructed for the TEP matter-frame spacetime and compared directly with the standard flat $\Lambda$CDM diagram. The metric in conformal coordinates is

\begin{equation} \label{eq:metric_conformal}
d\tilde{s}^{2} = a_{\rm eff}^{2}(\eta)\left(-d\eta^{2} + dr^{2} + r^{2}\,d\Omega^{2}\right) \, .
\end{equation}

In both the standard and TEP conformal diagrams, time and space are compactified independently so that infinite spacetime maps to a finite rectangle. Let $\eta_{0}$ denote the present-epoch conformal time. For the *standard* flat $\Lambda$CDM cosmology, conformal time runs from $\eta=0$ (Big Bang) to $\eta=\eta_{0}$ (present), and the compactification

\begin{equation} \label{eq:compact_coords_lcdm}
T_{\Lambda} = \arctan\!\left(\frac{\eta}{\eta_{0}}\right) \, , \qquad R = \arctan\!\left(\frac{r}{\eta_{0}}\right) \, ,
\end{equation}

maps $\eta\in[0,\eta_{0}]$ and $r\in[0,\infty)$ to the rectangle $0\le T_{\Lambda}\le\pi/4$, $0\le R\lt\pi/2$. The bottom edge $T_{\Lambda}=0$ is the physical singularity: a spacelike boundary where $a\to0$ and all curvature invariants diverge. Every causal curve terminates there in finite proper time.

For the *TEP* temporal-horizon cosmology, conformal time runs from $\eta=\eta_{0}$ (present) to $\eta\to\infty$ (temporal horizon), and the compactification

\begin{equation} \label{eq:compact_coords_tep}
T = \arctan\!\left(\frac{\eta_{0}}{\eta}\right) \, , \qquad R = \arctan\!\left(\frac{r}{\eta_{0}}\right) \, ,
\end{equation}

maps $\eta\in[\eta_{0},\infty)$ and $r\in[0,\infty)$ to the same rectangle $0\le T\le\pi/4$, $0\le R\lt\pi/2$. The bottom edge $T=0$ is the temporal horizon $\mathscr{T}^{-}$: a *regular* spacelike boundary where $A_{\rm clock}\to0$ and all curvature invariants vanish (Proposition 1). Null geodesics approach it with infinite affine parameter; timelike curves approach it with infinite proper time.

The compactified causal layout is analogous, while the physical content of the lower boundary differs radically.

**Figure 1.** Penrose-style schematic compactified conformal diagrams for (a) standard flat ΛCDM and (b) the TEP temporal-horizon branch. Both diagrams show a compactified causal slab; the upper edge is the present epoch, not future infinity. **Panel (a):** the lower spacelike boundary is the Big Bang singularity, where $a\to0$, curvature diverges ($\tilde{\mathcal{K}}\to\infty$), and past-directed causal curves terminate. **Panel (b):** the corresponding lower boundary is a smooth regular temporal conformal horizon $\mathscr{T}^{-}$, where $A_{\rm clock}\to0$ and curvature invariants vanish ($\tilde{\mathcal{K}}\to0$). Null geodesics are dashed red and timelike curves solid blue. In the TEP panel, the lower boundary is approached only asymptotically: null curves in infinite affine parameter and timelike curves in infinite proper time. Tick marks on the timelike curve denote equal proper-time intervals compressed by the compactification. The compactified causal layout is analogous, but the physical content of the lower boundary differs radically.

The TEP diagram (Panel b) is a rectangle with horizontal top and bottom edges and vertical left and right edges. In this schematic conformal representation, null geodesics are drawn at $45°$ to emphasize the causal structure; a fully metric-derived Penrose compactification would require constructing compactified null coordinates explicitly from the conformal metric. In a generic compactified coordinate representation their apparent slope can vary with position, but they remain causal and approach the spacelike boundary $\mathscr{T}^{-}$ only asymptotically. The boundary of this rectangle comprises:

- **$\mathscr{T}^{-}$ (temporal past infinity):** the horizontal line $T=0$ ($0\le R\lt\pi/2$), corresponding to $\eta\to\infty$ at all finite $r$. This is the TEP temporal horizon. It is *not* a curvature singularity; all polynomial invariants vanish there (Proposition 1), and the conformal factor $a_{\rm eff}\to 0$ merely reflects the vanishing of the relative clock rate.

- **Present epoch:** the horizontal line $T=\arctan(1)=\pi/4$ ($0\le R\lt\pi/2$), corresponding to $\eta=\eta_{0}$ at all finite $r$. This is the observer's present slice.

- **$r=0$ (spatial origin):** the vertical line $R=0$ ($0\le T\le\pi/4$), the symmetry axis of the radial coordinate.

- **$i^{0}$ (spatial infinity):** the vertical line $R\to\pi/2$ ($0\le T\le\pi/4$), approached along spacelike curves with $r\to\infty$.

- **$i^{+}$ (future timelike infinity):** the corner $(T,R)=(\pi/4,0)$, where comoving timelike geodesics reach the present epoch.

Crucially, *every* inextendible causal curve in the TEP diagram has its past limit on $\mathscr{T}^{-}$ and its future limit on the present-epoch boundary; there is no singularity anywhere in the diagram.

**Comparison with standard cosmology.** Figure 1 makes the distinction immediate. In the standard diagram (Panel a), the past boundary is a *spacelike singularity* (the Big Bang) where all curvature invariants diverge and every causal curve terminates in finite proper time. In the TEP diagram (Panel b), the past boundary is $\mathscr{T}^{-}$, a *regular conformal-temporal boundary* where curvature invariants vanish; null geodesics have infinite affine parameter, while timelike curves have infinite proper time. The TEP diagram shares the same compactification topology as the conformal diagram of global de Sitter space: both have a smooth horizontal spacelike past boundary, a smooth horizontal future boundary, and vertical spatial-infinity edges. The compactified causal layout is topologically analogous; the physical mechanism differs—de Sitter's past boundary is $\mathscr{I}^{-}$, an asymptotic surface of an exponentially expanding congruence, whereas TEP's past boundary is $\mathscr{T}^{-}$, the limit where the relative conformal clock rate vanishes on a nonexpanding static background.

**Boundary-regularity interpretation.** For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\le\tfrac12$:

- The conformal compactification $(\tilde{M},\tilde{g}_{\mu\nu})$ with conformal boundary $\partial\tilde{M}=\mathscr{T}^{-}\cup\{\text{present}\}\cup i^{0}\cup i^{+}$ is smooth.

- The Weyl tensor vanishes on $\mathscr{T}^{-}$ (conformally flat boundary).

- All inextendible causal curves have past endpoint on the spacelike boundary $\mathscr{T}^{-}$ and future endpoint on the present-epoch surface or future null infinity.

- There exists no trapped surface or incomplete geodesic; the framework complies with the mathematical constraints of the Hawking-Penrose singularity theorems by violating the Strong Energy Condition (Section 5).

The analytic curvature and geodesic results place $\mathscr{T}^{-}$ on the footing of a regular spacelike conformal boundary; Figure 1 gives a Penrose-style schematic representation of that boundary structure. It is a boundary of the manifold, not a singularity within it.

## 4.6 Implications for Quantum Cosmology

The regularity of the temporal conformal boundary $\mathscr{T}^{-}$ removes the standard motivation for a quantum gravitational "beginning" at finite proper time. In standard Big Bang cosmology, the curvature singularity at $a\to0$ forces a breakdown of the classical theory at a finite past, providing the principal physical justification for quantum-cosmological models that attempt to describe a first moment of time. Because TEP's temporal horizon is curvature-empty and timelike-complete, the classical geometry remains valid arbitrarily far into the past; there is no finite-time singularity that demands quantum replacement.

This opens the possibility of a well-defined wavefunction on the regular boundary $\mathscr{T}^{-}$, formulated as a boundary condition on a smooth conformal compactification rather than as an initial condition at a singular point. The boundary data would describe correlations across the temporal horizon, analogous to how boundary-value problems are posed on smooth spatial or null boundaries in standard field theory. Whether such a boundary quantum state reproduces the observed classical late-time cosmology is a well-posed mathematical question; it does not require a speculative resolution of a curvature singularity that does not exist in the TEP matter frame.

# 5. Effective Stress-Energy and Hawking-Penrose Consistency

The Hawking-Penrose singularity theorems establish that a singularity is mathematically inevitable if the Strong Energy Condition (SEC) holds: $\rho + 3p \geq 0$ and $\rho + p \geq 0$. The theorems require the SEC as an explicit assumption; if the SEC is violated, their conclusion of inevitable geodesic incompleteness no longer applies. The effective stress-energy tensor of the temporal field is computed to determine whether the SEC is violated in the temporal-horizon geometry.

## 5.1 Stress-Energy from the Temporal-Field Action

The temporal field $A$ enters the matter-frame metric through the conformal factor $A_{\rm clock}$. Its stress-energy tensor follows from the canonical scalar-field action with a field-dependent kinetic function $Z(A)$:

\begin{equation} \label{eq:T_munu}
T_{\mu\nu}(A) = Z(A)\,\partial_{\mu}A\,\partial_{\nu}A - g_{\mu\nu}\Bigl[\tfrac{1}{2}Z(A)(\partial A)^{2} + V(A)\Bigr] \, .
\end{equation}

For a homogeneous temporal field $A(t)$ in a FLRW background, the effective energy density and pressure are

\begin{equation} \label{eq:rho_p_phi}
\rho_{A} = \tfrac{1}{2}Z(A)\,\dot{A}^{2} + V(A) \, , \qquad p_{A} = \tfrac{1}{2}Z(A)\,\dot{A}^{2} - V(A) \, .
\end{equation}

In the slow-clock limit the kinetic term is negligible relative to the potential, $\tfrac{1}{2}Z\dot{A}^{2}\ll V(A)$, so the equation of state parameter approaches

\begin{equation} \label{eq:w_phi}
w_{A} = \frac{p_{A}}{\rho_{A}} \simeq -1 \, .
\end{equation}

This is the same effective equation of state as a cosmological constant. The numerical Step 03 diagnostic adopts the following effective-fluid density prescription for the clock map $A_{\rm clock}(z)=(1+z)^{-1}$:

\begin{equation} \label{eq:rho_phi}
\rho_{\phi} \approx \frac{\epsilon_{\rm dyn}}{8\pi G}\,H^{2}\left(\frac{d\ln a_{\rm eff}}{d\ln A_{\rm clock}}\right)^{2}
\end{equation}

where the dimensionless factor $(d\ln a_{\rm eff}/d\ln A_{\rm clock})^{2}$ encodes the coupling between the temporal field and the effective scale factor. With $a_{\rm eff}=A_{\rm clock}\,a_{\rm m}$ and $a_g=1$ in the static matter frame, $d\ln a_{\rm eff}/d\ln A_{\rm clock}=1$, while the reconstructed action of Section 10 has the late-time limit

\begin{equation}
\rho_{A}(\eta_{0}) = \tfrac12\mathcal Z(\chi_{0})\,\dot\chi_{0}^{2} + U(\chi_{0}) \approx U_{\rm c} \, ,
\end{equation}

when the kinetic and nonconstant potential terms have decayed. Identifying the benchmark density with this asymptotic plateau would impose the normalization

\begin{equation} \label{eq:epsilon_dyn}
\epsilon_{\rm dyn} = \frac{8\pi G\,U_{\rm c}}{H_{0}^{2}} \, .
\end{equation}

The exact effective-action energy-condition identities are stronger than an assigned equation-of-state curve. Writing $K=\tfrac12\mathcal Z\dot\chi^2\ge0$, one has $\rho=K+U$, $\rho+p=2K$ and $\rho-p=2U$. Thus NEC, WEC and DEC hold wherever $U\ge0$, while SEC is violated whenever $U>2K$. On the reconstructed branch $K\to0$ and $U\to U_{\rm c}>0$, so SEC violation follows asymptotically without fitting a fluid pressure. Step 03's numerical curve instead uses the declared prescription $w(z)=-1+0.1/(1+z)=-0.90-0.10(1-a)$ ($w_0=-0.90$, $w_a=-0.10$, lying in the thawing $w_0>-1,w_a<0$ quadrant); its finite-redshift energy-condition table is an illustrative fluid diagnostic, not an evaluation of $\mathcal Z(\chi)$ and $U(\chi)$ along the action trajectory. Furthermore, when the zero-$\Lambda$ TEP-C0 M1 temporal-shear transport kernel $d\chi/dz=(c/H_0)[1+\epsilon_{\rm shear}^{\rm los}\ln(1+z)\exp(-(z/z_T)^2)]/(1+z)^{3/2}$ ($\epsilon_{\rm shear}^{\rm los}=0.8708$, $z_T=5.0$, Paper 26) is reconstructed as an effective FLRW dark-energy fluid $E_{\rm eff}^2(z)=(1+z)^3/\gamma(z)^2=\Omega_{m,0}(1+z)^3+(1-\Omega_{m,0})f_{\rm DE}(z)$ alongside the zero-parameter TEP-HC acoustic matter fraction $\Omega_{m,0}=\omega_{m,\rm eff}/h^2=0.3038$ (or Planck $\Omega_{m,0}=0.315$), the effective equation of state $w_{\rm eff}(z)=-1+\tfrac{1+z}{3}d\ln f_{\rm DE}/dz$ yields $w_{\rm eff}(0)=-0.834$ to $-0.848$ and a linear CPL projection over the DESI BAO range $z\in[0,1]$ of $(w_0=-0.71,\,w_a=-0.87)$ at $\Omega_{m,0}=0.304$ and $(w_0=-0.69,\,w_a=-1.13)$ at $\Omega_{m,0}=0.315$ (Step 03), reproducing the exact $(w_0>-1,\,w_a<0)$ thawing dark-energy evolution reported by DESI Year-1 BAO + CMB + DESY5 SNe ($w_0=-0.727\pm0.067$, $w_a=-1.05^{+0.31}_{-0.27}$; DESI Collaboration 2024) within $0.28\sigma$–$0.61\sigma$ in $w_0$ and $0.27\sigma$–$0.61\sigma$ in $w_a$ without a primitive dark-energy fluid. On the single-history native background that fits Pantheon+, DESI DR2 BAO and the Planck acoustic angle together (TEP-C0 Step 03-14, $\Delta\chi^2=-8.1$ against $\Lambda$CDM), the apparent equation of state rises to $w_{\rm eff}\approx-0.86$ near $z\approx0.4$ and returns to $-1$ by $z\approx1.5$, with CPL projection $(w_0,w_a)\approx(-0.83,-0.44)$, in DESI's thawing quadrant, produced by the time field without a primitive dark-energy fluid.

At the Step 03 benchmark $\epsilon_{\rm dyn}=5.5\times10^{-3}$, imposing $\eqref{eq:epsilon_dyn}$ would give

\begin{equation} \label{eq:Uc_value}
\frac{U_{\rm c}}{\rho_{\rm crit,0}} = \frac{\epsilon_{\rm dyn}}{3} \approx 1.8\times10^{-3} \, ,
\end{equation}

recorded as a conditional normalization in Step 03. The benchmark is distinct from the native TEP-HC likelihood parameter $\epsilon_T^{\rm HC}$, whose full high-$\ell$ result is $0.0043\pm0.0025$: that amplitude is not a measurement of $U_{\rm c}$ without an action-level mapping. Likewise HC's operational $\Omega_\phi$ background budget is not fixed by the small illustrative plateau. The absence of a bare geometric $\Lambda$ is a structural choice; accounting for the full observed background budget with the common action requires the embedding identified in Section 2. The benchmark alone establishes neither a universal vacuum-energy bound nor the physical origin of the entire background budget.

The pipeline evaluates the NEC, WEC, DEC, and SEC for its specified effective-fluid diagnostic across redshift. The SEC is systematically violated, while the NEC and WEC are satisfied. By violating the SEC, the temporal field removes one of the assumptions required by the Hawking-Penrose singularity theorems; the theorems therefore do not force geodesic incompleteness. Geodesic completeness is established separately by the curvature and affine-parameter analysis of Sections 4.2–4.4.

## 5.2 Past-Completeness and the BGV Theorem

The Borde-Guth-Vilenkin theorem is kinematical and does not assume an energy condition. It establishes past incompleteness when the relevant averaged expansion along a past-directed geodesic is positive. TEP does not rely on an energy-condition loophole. Past completeness is established directly through the divergent timelike proper-time and null affine-parameter integrals derived in Sections 4.2–4.4.

The theorem applies to the timelike geodesic congruence of the spacetime whose completeness is in question. In the two-metric setting that spacetime is the matter metric $\tilde{g}_{\mu\nu}=A_{\rm clock}^2\,g_{\mu\nu}$ — the geometry on which particles and clocks propagate — so the operative evaluation is on the matter-frame congruence, not the coordinate congruence of $g_{\mu\nu}$ (for completeness it may be noted that the static coordinate metric also has vanishing expansion, $\theta_g = 3\dot a_g/a_g = 0$ with $a_g=1$, but the coordinate congruence is not the congruence to which the physical completeness question attaches).

Evaluated directly on the physical matter-metric congruence, the Hubble expansion parameter along a timelike congruence parameterized by proper time $\tilde{\tau}$ is $\tilde{H} = d\ln A_{\rm clock}/d\tilde{\tau}$. The BGV past-averaged expansion rate over a proper-time interval $\Delta\tilde{\tau} = \tilde{\tau}_0 - \tilde{\tau}_i$ is defined by

\begin{equation}
H_{\rm av} = \frac{1}{\Delta\tilde{\tau}} \int_{\tilde{\tau}_i}^{\tilde{\tau}_0} \tilde{H}(\tilde{\tau}')\,d\tilde{\tau}' = \frac{\Delta\ln A_{\rm clock}}{\Delta\tilde{\tau}} \, .
\end{equation}

As established in Section 4.3, for the adopted regular branch $0 \lt p \le 1/2$, the past proper-time integral diverges toward the temporal horizon: $\Delta\tilde{\tau} \to \infty$ as $\eta \to \infty$. Meanwhile, the accumulated logarithmic clock shift $\Delta\ln A_{\rm clock} = p\ln(\eta/\eta_0)$ grows only logarithmically, far slower than proper time ($\Delta\tilde{\tau} \sim \eta^{1-p}$ for $p \lt 1$). Consequently, the asymptotic past-averaged expansion rate along this comoving matter congruence tends to zero:

\begin{equation}
H_{\rm av} = \lim_{\Delta\tilde{\tau} \to \infty} \frac{p\ln(\eta/\eta_0)}{\Delta\tilde{\tau}} = 0 \, .
\end{equation}

The essential BGV hypothesis $H_{\rm av} > 0$ therefore fails by construction in the matter frame, just as $\theta_g = 0$ in the coordinate frame. This is not an evasion based on frame choice; it is a structural consequence of clock transport. The cosmological redshift is generated by clock-rate evolution rather than kinematic divergence of geodesics, The comoving congruence has the vanishing average evaluated above; arbitrary timelike geodesics and null geodesics are past complete on $p\le1/2$ by the independent integrals in Section 4. The BGV conclusion of past geodesic incompleteness is therefore avoided in both metric representations.

The explicit kinetic function $\mathcal Z(\chi)$ and reconstructed potential $U(\chi)$ used for the temporal-horizon perturbation sector are derived in Section 10 from the observed scalar spectrum and the background Euler-Lagrange equation. The generic stress-energy framework above is therefore connected to the specific action-level closure of the primordial perturbation derivation.

# 6. Temporal-Horizon Thermal History and Elemental Abundances

Standard cosmology attributes light-element synthesis (Helium-4, Deuterium, Lithium-7) to a primordial hot dense phase emerging from a zero-volume singularity. In the TEP framework, the physical high-temperature thermal state at high redshift ($T(\eta) = T_0 / A_{\rm clock}(\eta) = T_0 (1+z)$) is retained as a physical matter-frame state, which is operationally required for the recombination and photon-thermalization physics analysed in Sections 7 and 8. What is rejected is not the hot ionized plasma state itself, but its interpretation as a singular primordial beginning of the universe.

Because the underlying gravitational spacetime is static and eternal, the high-redshift plasma is bounded by an asymptotic temporal horizon ($A_{\rm clock} \to 0$) rather than a zero-volume spatial collapse. In this architecture, elemental abundances can also be investigated through candidate long-term asymptotic equilibria of stellar burning and galactic baryon recycling. Under this complementary pathway, the observed Helium mass fraction ($Y_p \approx 0.249$) and metallicity ($Z \approx 10^{-4}$ to $10^{-3}$) are examined as balancing points between production, astration, and galactic infall, governed by proper-time reaction flows.

The quantitative mechanism for sustained non-primordial Deuterium production and steady-state chemical equilibrium is investigated in detail in TEP-BBN (Paper 29), where it remains an active research problem. TEP-TH retains the hot matter-frame thermal environment as an exact feature of the temporal landscape without requiring a singular origin of spacetime.

# 7. Recombination and Visibility Function

Recombination and CMB last scattering are critical early-universe observables. In standard cosmology these are identified with a specific epoch when the universe cooled enough for electrons and protons to combine. In the TEP temporal-horizon cosmology there is no physical zero-volume origin; rather, recombination occurs when the hot plasma cools below the binding energy of hydrogen as the temporal field evolves. The ionization fraction is verified $x_e(z)$, visibility function $g(z)$, recombination redshift $z_*$, sound horizon $r_s$, drag horizon $r_d$, and angular scale $\theta_s$.

## 7.1 Recombination in the Canonical Conformal Branch

Earlier exploratory versions introduced a phenomenological epoch-screening function to suppress the dynamical temporal response during recombination. That construction is superseded in the canonical TEP architecture. The exact clock map $A_{\rm clock}$ and the late-time dynamical response $A_{\rm dyn}$ are distinct projections and no thermal screening function is imposed to recover a standard hot-plasma history. Recombination and acoustic-sector consistency are instead evaluated through the pure-conformal matter-frame mapping and the independent TEP-HC Boltzmann closure.

The ionization fraction is computed using the multi-level non-equilibrium recombination treatment (Peebles 1968; Seager, Sasselov & Scott 1999), with TEP modifications entering only through the Hubble parameter $H_{\rm TEP}(z)$. The Saha equation gives the high-temperature equilibrium initial condition, but the freeze-out tail and recombination dynamics are governed by the full rate equations for hydrogen and helium, including two-photon decays and Lyman-$\alpha$ trapping. The pipeline uses a TEP-adapted RECFAST equivalent that tracks $x_{e}(z)$ through the ionization balance

\begin{equation} \label{eq:peebles}
\frac{dx_{e}}{dt} = -C\,\left[\alpha_{\rm B}(T)\,n_{e}\,x_{p} - \beta(T)\,x_{e}\,e^{-E_{\alpha}/k_{\rm B}T}\right] \, ,
\end{equation}

where $C$ is the Peebles suppression factor, $\alpha_{\rm B}$ is the case-B recombination coefficient, and $\beta$ is the photoionization rate. All rates depend on temperature and density; the only TEP modification is $H_{\rm TEP}$ in the $dt$ conversion and in the density evolution.

The visibility function is derived from the optical depth $\tau(z)$:

\begin{equation} \label{eq:visibility}
g(z) = \frac{d\tau}{dz} e^{-\tau}
\end{equation}

The sound horizon is computed by integrating the sound speed divided by the Hubble parameter from the Big Bang to redshift $z$:

\begin{equation} \label{eq:sound_horizon}
r_s(z) = \int_z^{\infty} \frac{c_s(z')}{H_{\rm TEP}(z')} dz'
\end{equation}

The pipeline computes these quantities for $z\in[0,2000]$. Propagating the temporal geometry through the Peebles recombination treatment yields

- $z_* = 1078.6$ ($-1.0\%$ relative to $\Lambda$CDM $1089.9$)

- $r_s = 146.1$ Mpc ($-0.7\%$ relative to $\Lambda$CDM $147.1$ Mpc)

- $r_d = 145.0$ Mpc ($-1.6\%$ relative to $\Lambda$CDM $147.3$ Mpc)

- Manual $\theta_s = 0.01061$ ($+1.9\%$ relative to Planck $0.01041$)

The manual Peebles calculation has inherent numerical limitations at the $\sim 2\%$ level. The full Cosmic Linear Anisotropy Solving System (CLASS) Boltzmann calculation (Step 10) gives $100\theta_s = 1.0419$, consistent with Planck 2018 at the $0.09\%$ level.

**Relation to the eternal-native surface.** The same last-scattering surface is computed eternal-natively in TEP-BBN (Steps 14–19): there the $\tau = 1$ boundary at $z \approx 1080$ is a spatial ionization front — the Strömgren edge of the deep thermalized zone, where the ambient field's local temperature crosses the hydrogen ionization threshold — closing a neutral foreground trough, rather than a temporal freeze-out sweep of a primordial plasma. The kernel-level comparison (TEP-BBN results/step_19_eternal_surface_reconciliation.json) finds the two descriptions agree on the integrated column — $\tau = 1$ at $z \simeq 1079$–$1080$ ($0.13\%$ peak agreement) with $\tau_{\rm reion} \simeq 0.054$ — while differing in morphology: the eternal kernel is a sharp front column carrying $\sim 88\%$ of the normalized column plus diffuse wing/trough weight, against the broad Peebles bump ($\mathrm{FWHM}_z \sim 10^{2}$) computed here. The column bookkeeping is quantified by the path-measure Jacobian $J(z) \sim 4\times10^{7}$ at the edge: pointwise equivalence of the two columns would place the eternal surface at $\sim 30\,n_{b,0}$ — absorber/diffuse densities rather than cosmic-recombination densities — so the Peebles kernel above is the FLRW reconstruction of the observable column, not the physical eternal profile. The eternal-model diffusion blur is also now computed rather than estimated: the front column's scattering depth random-walks to $\theta_D \simeq 8\times10^{-4}$ rad, within $\sim 25\%$ of the observed Silk angle, leaving the boundary's native perturbation mode spectrum as the discriminating residual item.

# 8. CMB Blackbody Origin and Spectral Distortion

The CMB blackbody spectrum is a key test of early-universe thermal history. The TEP temporal-horizon cosmology must preserve a Planckian spectrum without generating forbidden spectral distortions. The temporal-horizon thermal scaling is verified to produce a FIRAS-compatible blackbody spectrum.

The TEP thermal scaling is:

\begin{equation} \label{eq:temp_scaling}
T(z) = T_0 / A_{\rm clock}(z)
\end{equation}

In the conformal frame, blackbody radiation preserves its thermal form because photon number is conserved and the frequency scales as $\nu \to \nu/A_{\rm clock}$. The Planck spectrum transforms as:

\begin{equation} \label{eq:planck}
B_\nu(T) = \frac{2h\nu^3}{c^2} \frac{1}{e^{h\nu/k_BT} - 1}
\end{equation}

It is important to distinguish two separate questions. (i) *Instantaneous conformal rescaling*: if the photon distribution is exactly Planckian at some redshift, rescaling $\nu\to\nu/A_{\rm clock}$ and $T\to T/A_{\rm clock}$ leaves it Planckian. This is a trivial mathematical identity. (ii) *Distortion production during thermalization*: the physically observable question is whether the temporal field injects, removes, or redistributes photon energy in a way that creates forbidden deviations from a blackbody during the thermalization epochs $z\gtrsim 10^{6}$.

The standard thermalization hierarchy is: double-Compton and bremsstrahlung create and maintain equilibrium at $z\gtrsim 10^{6}$; Compton scattering shapes the spectrum at $10^{5}\gtrsim z\gtrsim 10^{4}$; photon production becomes inefficient below $z\sim 10^{4}$. In TEP, the conformal clock-rate rescaling applies uniformly to all photon frequencies. There is no frequency-dependent coupling, no non-thermal energy injection, and no preferred scattering process that would create a chemical potential or Compton $y$-parameter. The temporal field rescales the local temperature but does not alter photon number or redistribute energy across the spectrum.

The resulting distortion parameters are bounded by

\begin{equation} \label{eq:mu_bound}
\mu \sim 1.4 \int \frac{dQ/Q_{\gamma}}{dz}\,\mathcal{J}_{\mu}(z) \approx 0 \, ,
\end{equation}

because $dQ=0$ in TEP: the temporal field does not inject or extract energy from the photon fluid; it rescales the clock $A_{\rm clock}$ that measures it. Similarly, the Compton $y$-parameter satisfies $y\approx\int (k_{\rm B}T_{e}/m_{e}c^{2})\,d\tau_{\rm C}\approx 0$ at the level of the standard recombination-era value $y\sim 10^{-8}$, with no additional TEP contribution.

FIRAS constraints are $|\mu| \lt 9 \times 10^{-5}$ and $|y| \lt 1.5 \times 10^{-5}$ at 95% CL. Step 06 fits the 43-channel NASA LAMBDA COBE/FIRAS monopole spectrum (Fixsen et al. 1996; Fixsen & Mather 2002), recovering $T_{\rm FIRAS} = 2.7250 \pm 0.0006$ K, and evaluates the TEP-remapped spectrum against the published FIRAS distortion bounds across multiple redshifts ($z = 100, 500, 1100, 2000$). The implied $\mu$ and $y$ distortions are consistent with zero within FIRAS constraints: $|\mu| \lt 10^{-7}$, $|y| \lt 10^{-8}$. The temporal-horizon thermal mapping preserves a perfect blackbody spectrum without forbidden spectral distortions.

**Photon-number bookkeeping in a static volume.** In the expanding reconstruction, the number density falls as $(1+z)^3$ because the spatial volume grows. No such mechanism is required here, and none is invoked: the photon bath is not a fixed conserved population diluted by volume but an equilibrium field maintained by the thermalization surface. The occupation number of a free photon distribution is conformally invariant along null rays, so the Planckian phase-space density transported from depth $z$ retains its form while its characteristic temperature resamples to $T_0$. The number density of a Planck field is a function of temperature alone, $n_\gamma = 16\pi\zeta(3)(k_{\rm B}T)^3/(hc)^3$, hence $n_\gamma(z)/n_{\gamma,0} = (1+z)^3$ identically — the cubic factor is recovered as a temperature cubed, not as a volume. The same bookkeeping appears in the two complementary projections already established: in the matter frame, particle densities on the effective geometry scale as $\tilde n = n_0\,A_{\rm clock}^{-3}$ while blackbody entropy scales as $\tilde s_\gamma\propto\tilde T^{3}$, so the photon-entropy-per-baryon $\tilde\sigma = \tilde s_\gamma/\tilde n_b$ is exactly constant and equal to the observed $5.9\times10^{9}\,k_{\rm B}$ per baryon (Step 07; a deliberately mismatched dilution profile drifts by $\sim10^{9}$, showing the diagnostic is not vacuous); and in the observed flux sector the clock map suppresses energy and arrival rate by $(1+z)$ each, which is precisely the counting that returns the Tolman $(1+z)^{4}$ surface-brightness law and the exact Etherington relation $d_L = (1+z)^{2}d_A$ of TEP-C0. Photon number is therefore conserved, arrival rates are accounted, and the present-day $n_\gamma \approx 411\,{\rm cm^{-3}}$ is the equilibrium density of a $2.725$ K radiation field, not the residue of a vanished denser bath.

**The excitation-temperature discriminator.** The sharpest empirical test distinguishing a local-temperature law from a transport illusion is the excitation of atomic and molecular species in distant absorbers: rotational level populations of CN, CO and C I in quasar absorption systems directly thermometer the radiation field *at the absorber's own location*. This observable is native to the temporal-horizon construction and requires no transport assumption at all: the local temperature at temporal depth $z$ is $T_{\rm loc}(z) = T_0/A_{\rm clock}(z) = T_0(1+z)$ by the clock map itself, so an excitation thermometer embedded at that depth must read exactly the standard profile. Mechanisms that produce redshift as a propagation effect while leaving the ambient radiation field at a uniform present-day temperature fail this test outright; the temporal-horizon law passes it by construction. Step 11 evaluates the published CO excitation sample directly: six absorbers spanning $z = 0.89$–$2.69$ (Muller et al. 2013; Srianand et al. 2008; Noterdaeme et al. 2010, 2011), anchored by the FIRAS monopole, return $\chi^2/{\rm dof} = 0.15$ against $T = T_0(1+z)$ with maximum single-point pull $0.6\sigma$, and a free-exponent fit $T = T_0(1+z)^{1-\beta}$ yields $\beta = +0.003\pm0.023$, consistent with zero and with the literature constraints $\beta = -0.007\pm0.027$ (Noterdaeme et al.) and $+0.010\pm0.013$ (Klimenko et al. 2020). On the same sample, the constant-temperature alternative has $\chi^2 = 865.8$ versus $\chi^2 = 1.08$ for the $T = T_0(1+z)$ law (descriptive $\sqrt{\Delta\chi^2} = 29.4$) — the absorber thermometers confirm that the radiation field at depth genuinely sits at the elevated local temperature, supporting the tested temperature law. Collisional excitation can only bias $T_{\rm ex}$ above $T_{\rm CMB}$; the bounding $-10\%$ sensitivity check based on Klimenko et al. yields $\chi^2 = 4.72$ and $\beta = +0.041$, preserving the $\beta \simeq 0$ compatibility. The same logic applies to the Sunyaev–Zel'dovich temperature measurements of cluster-embedded gas, which likewise thermometer the ambient field locally at the cluster depth.

The spectral-preservation result is a statement about transport: it establishes that the conformal clock-rate field carries a thermal photon distribution without distortion. The physical supply of that distribution is a separate, already quantified sector of the eternal-universe construction. In the static spatial geometry the absorbing column along a line of sight is unbounded, and the TEP-BBN absorbing-column evaluation (Gate 11) places the unit-optical-depth surface for dust-grade absorptivity at temporal depth $z \approx 130$–$1340$ — a range that brackets the recombination depth $z_* \approx 1079$ computed in Section 7. The same temporal-depth sector therefore hosts both the surface at which distributed starlight is reprocessed into the observed photon bath and the last-scattering plasma: at that depth the local matter temperature $T_{\rm loc} = T_0(1+z_*) \approx 2.9 \times 10^{3}$ K lies at the hydrogen ionization edge, above the dust-sublimation range, so thermalization interior to the dust surface proceeds by the standard plasma processes — free-free absorption, Compton scattering, and the photoionization balance whose electron column is maintained to the required depth by the ionization-equilibrium budget of TEP-BBN (Gate 12). Forward-integrating the homogeneous Saha+Peebles ionization profile $n_e(z)$ across this transition (Steps 05–06) confirms that the foreground remains optically thin throughout the dust window ($\tau_{\rm es} = 8.9\times10^{-4}$ at $z=130$, $n_e = 1.5\times10^{-4}\,{\rm cm^{-3}}$; $\tau_{\rm es} = 0.011$ at $z=500$), crosses unit Thomson optical depth at the hydrogen ionization edge ($\tau_{\rm es} = 0.88$ at $z=1079$, $n_e = 28.2\,{\rm cm^{-3}}$; $\tau_{\rm es} = 1.00$ at $z \approx 1090$; $\tau_{\rm es} = 1.12$ at $z=1100$, $n_e = 36.7\,{\rm cm^{-3}}$), and reaches an optically thick plasma wall interior to the boundary ($\tau_{\rm es} = 22.8$ at $z=1500$, $n_e = 613\,{\rm cm^{-3}}$; $\tau_{\rm es} = 75.3$ at $z=2000$, $n_e = 1.52\times10^{3}\,{\rm cm^{-3}}$). Within this architecture the plasma's thermal history is a real local process: each region evolves under native local thermodynamic evolution $\tilde\nabla_\mu\tilde T^{\mu\nu}=0$ toward balance with its radiation field and sources. The conformal map supplies the transport relation between local thermal states at different temporal depths; it does not create the states. While the homogeneous Saha+Peebles electron-density and optical-depth profile is closed above, the inhomogeneous absorber-statistics clumping inversion posed in TEP-BBN remains a separate refinement.

# 9. Entropy and Arrow of Time

In standard cosmology, tracing the thermodynamic arrow of time backward to a zero-volume singularity forces a breakdown of physical state variables and requires a highly fine-tuned, exceptionally low initial entropy state. In the TEP temporal-horizon cosmology, the past boundary is an asymptotic limit of the relative clock rate, not a physical spatial collapse. Therefore, local thermodynamic state variables must remain finite, and the arrow of time must flow smoothly from an infinite affine past. Entropy is tracked in the temporal-horizon reconstruction to verify this thermodynamic regularity.

The radiation entropy density scales as $s_\gamma \propto T^3$. In the TEP matter frame, the entropy density transforms as:

\begin{equation} \label{eq:entropy_density}
\tilde{s} = s / A_{\rm clock}^3
\end{equation}

The entropy diagnostic must be non-definitional to carry content: a quantity assembled by algebraically undoing the conformal rescaling, such as $\tilde{s}A_{\rm clock}^{3}$ with $\tilde{s}=s/A_{\rm clock}^{3}$, is conserved identically and tests nothing. The pipeline therefore tracks the specific entropy per baryon,

\begin{equation} \label{eq:specific_entropy}
\tilde{\sigma} = \frac{\tilde{s}_{\gamma}}{\tilde{n}_{b}} \, ,
\end{equation}

assembled from two independently motivated evolution laws. The photon entropy density follows blackbody thermodynamics of the measured temperature-redshift law, $\tilde{s}_{\gamma}=(2\pi^{2}/45)\,g_{*s}\,\tilde{T}^{3}$ with $\tilde{T}(z)=T_{0}(1+z)$, while the baryon density follows particle-number conservation on the effective matter geometry, $\tilde{n}_{b}(z)=n_{b,0}\,A_{\rm clock}(z)^{-3}$. The constancy of $\tilde{\sigma}$ is then a physical consistency condition — it holds if and only if the thermal law and the dilution law are governed by the same clock factor, which is precisely the content of the thermal scaling $T=T_{0}/A_{\rm clock}$ established in Section 8 — rather than an algebraic identity.

The pipeline evaluates $\tilde{\sigma}(z)$ across $z\in[0,1000]$ (Step 07). The specific entropy is constant across the full range, with present-day value $\tilde{\sigma}_{0}\approx5.9\times10^{9}\,k_{\rm B}$ per baryon, the observed cosmic photon-entropy-per-baryon scale; no entropy production is required anywhere along the reconstruction. A control evaluation in which the dilution law is driven by a deliberately mismatched profile — the late-time drift factor $A_{\rm dyn}(z)=(1+z/z_{t})^{-\epsilon_{\rm dyn}}$, which is not the horizon clock map — drifts by a factor $\sim10^{9}$ over the same range, demonstrating that the diagnostic responds to inconsistency and is not vacuous. The entropy density remains finite at every finite redshift (reaching $\sim1.5\times10^{27}\,k_{\rm B}\,{\rm m}^{-3}$ in matter-frame units at $z=10^{3}$); its growth toward the horizon is the clock-ratio image of the standard $T\to\infty$ limit, not a state attained at finite affine distance. The arrow of time is carried by the clock-drift direction — the future is the direction of increasing $A_{\rm clock}$ — with the constant $\tilde{\sigma}$ recording adiabatic, reversible evolution: no low-entropy initial state is invoked, because there is no initial state. The temporal horizon is thermodynamically regular. Because the temporal horizon is an observational asymptote rather than a physical origin, this regularity demonstrates that local thermodynamic processes—and thus the arrow of time—operate without requiring a singular beginning. The universe does not emerge from a zero-volume state; rather, it evolves locally forward through an asymptotically infinite past.

# 10. Primordial Perturbation Origin

In standard cosmology the nearly scale-invariant primordial spectrum $P_\mathcal{R}(k) \approx A_s (k/k_{\rm pivot})^{n_s-1}$ with $n_s \approx 0.965$ and $A_s = 2.10 \times 10^{-9}$ is either postulated as an initial condition or derived from an inflationary slow-roll potential. In the TEP temporal-horizon cosmology the scalar spectral shape emerges from fluctuations of the conformal clock field. The curvature perturbation is not produced by physical spatial inflation; it is produced by local clock-rate fluctuations:

\begin{equation} \label{eq:zeta_def}
\zeta = \delta\ln A_{\rm clock} = \frac{\delta A_{\rm clock}}{A_{\rm clock}} \, .
\end{equation}

The scalar power spectrum is therefore the two-point function of these clock-field fluctuations:

\begin{equation} \label{eq:P_zeta}
P_{\zeta}(k) = P_{\delta\ln A}(k) \, .
\end{equation}

## 10.1 Native Temporal Action

Introduce the dimensionless clock variable

\begin{equation} \label{eq:chi_def}
\chi \equiv \ln A_{\rm clock} \, ,
\end{equation}

so that the causal matter metric is $\tilde g_{\mu\nu}=e^{2\chi}g_{\mu\nu}$. The temporal field is made dynamical by the single-clock action

\begin{equation} \label{eq:S_temporal}
S = \int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R - \frac{M_{\rm Pl}^2}{2}\,\mathcal Z(\chi)(\nabla\chi)^2 - M_{\rm Pl}^2\,U(\chi)\right] + S_m[e^{2\chi}g_{\mu\nu},\psi_m] \, .
\end{equation}

Section 10 uses an effective cosmological single-clock action written in the variable $\chi=\ln A_{\rm clock}$. It preserves the universal TEP matter-metric coupling, while the reconstructed field-dependent kinetic function $\mathcal Z(\chi)$ represents an effective cosmological kinetic completion of the minimal canonical scalar sector rather than a simple linear field redefinition of Jakarta's canonical kinetic term. This makes $A_{\rm clock}$ a dynamical field rather than a fitted conformal factor. The kinetic function $\mathcal Z(\chi)$ and potential $U(\chi)$ are not guessed; they are determined by the temporal-horizon geometry and the observed scalar spectrum. The temporal slow-roll (spectral-flow) parameter is defined from the scalar mode index:

\begin{equation} \label{eq:epsilon_def}
\epsilon_{\rm field} \equiv \nu_A - \frac32 = \frac{1-n_s}{2} \, .
\end{equation}

The observed Planck value $n_s=0.9649$ gives $\epsilon_{\rm field}=0.01755$. This is not a free label; it is the spectral-flow parameter of the temporal clock-field fluctuations, analogous to the slow-roll parameter in inflation.

The relation between $(\chi,\mathcal Z,U)$ and the canonical scalar sector $(\phi,V)$ of the foundational action is made explicit as follows. The universal coupling $A(\phi)=\exp(\beta_A\phi/M_{\rm Pl})$ with $\beta_A=-1$ identifies the clock field with the canonical scalar up to the fixed linear map

\begin{equation} \label{eq:chi_phi_map}
\chi = \ln A_{\rm clock} = \frac{\beta_A\phi}{M_{\rm Pl}} = -\frac{\phi}{M_{\rm Pl}} \, , \qquad \phi = -M_{\rm Pl}\,\chi = M_{\rm Pl}\ln(1+z) \, ,
\end{equation}

where the second equality uses the exact redshift map $A_{\rm clock}=(1+z)^{-1}$. The ambient convention $\phi=0$ at the present epoch corresponds to $\chi=0$, and $\phi>0$ on the past-directed branch toward the horizon, consistent with the corpus-wide sign convention. A pure field redefinition would carry the canonical kinetic term into canonical form in $\chi$ as well, $-\tfrac12(\nabla\phi)^2\to-\tfrac12 M_{\rm Pl}^2(\nabla\chi)^2$, corresponding to $\mathcal Z=1$. The reconstructed $\mathcal Z(\chi)\neq1$ is not the Jacobian of the fixed linear field map. The current foundational sector is nonlinear $P(X,\phi)$ rather than a canonical kinetic term, and both its background-dependent principal coefficients and the disformal matter coupling can contribute to an effective cosmological reduction. The reconstructed $\mathcal Z$ therefore does not uniquely determine $B(\phi)$; likewise $U(\chi)$ must be matched to the universal master potential on the realized background. The common matter coupling and scalar variable are retained, while Rule 12 requires that explicit reduction rather than an independently assigned potential for each sector. The effective equations below state the reconstruction being tested pending that match.

For the temporal-horizon branch $A_{\rm clock}(\eta)=C\eta^{-p}$, the scalar quadratic action derived in Section 10.3 requires the kinetic function

\begin{equation} \label{eq:Z_A_clock}
\mathcal Z(A_{\rm clock}) = \mathcal Z_* \left(\frac{A_{\rm clock}}{A_*}\right)^{(2+2\epsilon_{\rm field})/p} \, .
\end{equation}

Equivalently, in terms of $\chi=\ln A_{\rm clock}$,

\begin{equation}
\mathcal Z(\chi) = \mathcal Z_*\,e^{(2+2\epsilon_{\rm field})\chi/p} \, .
\end{equation}

The action is therefore not arbitrary; the kinetic function required for the observed scalar spectral flow is derived from the temporal-horizon branch. The potential $U(\chi)$ is reconstructed from the background Euler-Lagrange equation rather than postulated; see Section 10.2.

**Effective scalar construction.** The mode equations below specify a reconstructed cosmological sector constrained by $n_s$ and $A_s$. The friction term $2\mathcal H_{\rm eff}\chi'$ uses the effective matter-frame pump; on a static gravitational metric, the homogeneous scalar Euler–Lagrange equation of $\eqref{eq:S_temporal}$ alone instead has no such gravitational scale-factor friction. Deriving the effective reduction, including matter sources and metric constraints, is part of the common-action embedding identified in Section 2. The clock fluctuation $\delta\chi$ is evaluated in the chosen slicing; its identification with gauge-invariant curvature perturbation also requires that constraint reduction. The reconstructed spectrum is a consistency construction within the assigned effective equations, rather than an independent prediction of the observed $n_s$ and $A_s$ from the fixed master potential.

## 10.2 Background Clock Solution

For a homogeneous clock field $\chi(\eta)$, the Euler-Lagrange equation is

\begin{equation} \label{eq:euler_lagrange}
\chi'' + 2\mathcal H_{\rm eff}\chi' + \frac12\frac{d\ln\mathcal Z}{d\chi}\chi'^2 + \frac{1}{\mathcal Z}\frac{dU}{d\chi} = 0 \, .
\end{equation}

The temporal-horizon branch is $A_{\rm clock}(\eta)=C\eta^{-p}$, so

\begin{equation}
\chi(\eta) = \ln C - p\ln\eta \, , \qquad \chi' = -\frac{p}{\eta} \, , \qquad \chi'' = \frac{p}{\eta^2} \, .
\end{equation}

This gives the effective clock-Hubble quantity

\begin{equation} \label{eq:H_eff}
\mathcal H_{\rm eff} \equiv \frac{a_{\rm eff}'}{a_{\rm eff}} = \frac{A_{\rm clock}'}{A_{\rm clock}} = -\frac{p}{\eta}
\end{equation}

Substituting the temporal-horizon solution and the derived kinetic function into the background Euler-Lagrange equation $\eqref{eq:euler_lagrange}$ determines the potential. With $\chi=\ln C-p\ln\eta$, $\chi'=-p/\eta$, $\chi''=p/\eta^2$, and $d\ln\mathcal Z/d\chi=(2+2\epsilon_{\rm field})/p$,

\begin{equation}
\frac{dU}{d\chi} = -\mathcal Z(\chi)\,\frac{p(2+2p+\epsilon_{\rm field})}{\eta^2} \, .
\end{equation}

Since $\eta^{-2}=C^{-2/p}e^{2\chi/p}$ and $\mathcal Z(\chi)=\mathcal Z_*e^{(2+2\epsilon_{\rm field})\chi/p}$,

\begin{equation}
\frac{dU}{d\chi} = -\mathcal Z_* C^{-2/p}\,p(2+2p+\epsilon_{\rm field})\; e^{(4+2\epsilon_{\rm field})\chi/p} \, .
\end{equation}

Integrating gives

\begin{equation} \label{eq:U_reconstructed}
U(\chi) = U_{\rm c} - \frac{\mathcal Z_* C^{-2/p}\,p^{2}(2+2p+\epsilon_{\rm field})}{4+2\epsilon_{\rm field}}\; e^{(4+2\epsilon_{\rm field})\chi/p}
= U_{\rm c} - U_{1}\left(\frac{A_{\rm clock}}{A_*}\right)^{(4+2\epsilon_{\rm field})/p} \, ,
\end{equation}

where $U_{\rm c}>0$ is an integration constant that sets the slow-clock vacuum energy — the same plateau identified in Section 5.1, where the illustrative normalization $\epsilon_{\rm dyn}=8\pi GU_{\rm c}/H_{0}^{2}=0.0055$ would give $U_{\rm c}/\rho_{\rm crit,0}\approx1.8\times10^{-3}$ — and

\begin{equation}
U_{1} = \frac{\mathcal Z_* C^{-2/p}\,p^{2}(2+2p+\epsilon_{\rm field})}{4+2\epsilon_{\rm field}} \, .
\end{equation}

On the physical temporal-horizon branch the constant $U_{\rm c}$ is chosen so that $U(\chi)>0$. The kinetic function $\mathcal Z(\chi)$ is fixed by the observed scalar spectral flow, while the background potential $U(\chi)$ is reconstructed from the temporal-horizon solution through the Euler-Lagrange equation.

## 10.2a Exact Background Solution

The power-law profile $A_{\rm clock}=C\eta^{-p}$ is not a tuned initial condition; it is an exact background solution of the reconstructed action. Substituting $\chi_{0}=\ln C-p\ln\eta$ into the background Euler-Lagrange equation $\eqref{eq:euler_lagrange}$ with $\mathcal H_{\rm eff}=\chi_{0}'$ and the reconstructed kinetic function $\mathcal Z(\chi)$ and potential $U(\chi)$, every term cancels identically because the exponents were chosen to satisfy the temporal-horizon constraint. The prescribed temporal-horizon trajectory is therefore an exact solution of this reconstructed effective action. Its exact satisfaction of the background equation is a consistency result; selection of the trajectory by the common master action is the embedding question stated in Section 2.

## 10.2b Equation of State from the Action

The equation of state is computed directly from the reconstructed kinetic function and potential. For the homogeneous field

\begin{equation}
w_{A}(\eta) = \frac{\tfrac12\mathcal Z(\chi)\,\dot\chi^{2} - U(\chi)}{\tfrac12\mathcal Z(\chi)\,\dot\chi^{2} + U(\chi)} \, ,
\end{equation}

with $\dot\chi=\chi'/A_{\rm clock}=-(p/C)\eta^{p-1}$, where the dot denotes matter proper time $d\tau=A_{\rm clock}\,d\eta$. As $\eta\to\infty$, the reconstructed kinetic contribution decays as $\eta^{2p-4-2\epsilon_{\rm field}}\to0$ while $U\to U_{\rm c}>0$, so $w_A\to-1$. The conformal clock rate is $\mathcal H_{\rm eff}=-p/\eta$, with $|\mathcal H_{\rm eff}'|/\mathcal H_{\rm eff}^2=1/p$. The proper-time rate is instead $H_{\rm clock}=\mathcal H_{\rm eff}/A_{\rm clock}=-(p/C)\eta^{p-1}$, giving $|\dot H_{\rm clock}|/H_{\rm clock}^2=(1-p)/p$ on $0<p\le\tfrac12$. These geometric rate ratios do not imply kinetic dominance: the displayed equation of state tends to $-1$ because the potential dominates the reconstructed scalar energy. A standard Einstein-frame Friedmann relation between the rate ratio and $w_A$ cannot be assumed for this effective clock metric.

The exponent $p$ enters this reconstruction as a family index, not as a dynamical output: the kinetic function's exponent $(2+2\epsilon_{\rm field})/p$ and the potential's asymptotic form are reconstructed around a chosen power law, and each member $(\mathcal Z_p, U_p)$ realizes that power law exactly. The geodesic-completeness window $0\lt p\le\tfrac12$ (Section 4) implies the conformal-rate bound $|\mathcal H_{\rm eff}^\prime|/\mathcal H_{\rm eff}^2\ge2$ and the proper-time bound $|\dot H_{\rm clock}|/H_{\rm clock}^2\ge1$. These are identities of the specified power-law family, rather than additional dynamical selection conditions. Which member of the family the corpus's canonical closure dynamics realizes is an open asymptotic determination (the branch-index datum, shared with the master-action embedding identified in Section 2); the completeness theorems hold unconditionally on every member of the regular branch, and the tensor falsification surface of Section 10.6 binds the index to an observable through $r_{\rm max}(p)\approx6.1\times10^{-5}p^{2}$.

in the static matter-frame case ($a_{\rm m}=1$). The scalar derivation no longer uses $\mathcal H=a_{\rm m}'/a_{\rm m}=0$ as the pump variable; it uses $\mathcal H_{\rm eff}=A_{\rm clock}'/A_{\rm clock}\neq 0$.

## 10.3 Scalar Quadratic Action and Quantization

Work in the single-clock gauge where fluctuations of the temporal field define the curvature perturbation $\zeta=\delta\chi=\delta\ln A_{\rm clock}$. Expanding the action $\eqref{eq:S_temporal}$ to second order and solving the lapse/shift constraints gives

\begin{equation} \label{eq:S_zeta_2}
S_\zeta^{(2)} = \frac12\int d\eta\,d^3x\,z_A^2\left[(\zeta')^2 - c_A^2(\nabla\zeta)^2\right] \, ,
\end{equation}

with

\begin{equation} \label{eq:z_A_Q_A}
z_A^2 = 2M_{\rm Pl}^2\,\mathcal Q_A \, , \qquad \mathcal Q_A = \frac{\mathcal Z(\chi)\chi'^2}{\mathcal H_{\rm eff}^2} \, ,
\end{equation}

and for the minimal temporal action $c_A^2=1$. Using $\chi'=-p/\eta$ and $\mathcal H_{\rm eff}=-p/\eta$ gives $\mathcal Q_A=\mathcal Z(\chi)$. With the derived kinetic function $\mathcal Z(\chi)=\mathcal Z_*e^{(2+2\epsilon_{\rm field})\chi/p}$ and $\chi=\ln C-p\ln\eta$,

\begin{equation}
z_A(\eta) = z_*\left(\frac{\eta}{\eta_*}\right)^{\frac12-\nu_A} = z_*\left(\frac{\eta}{\eta_*}\right)^{-1-\epsilon_{\rm field}} \, ,
\end{equation}

where $\nu_A=\frac32+\epsilon_{\rm field}$. This fixes the kinetic normalization required by the temporal action:

\begin{equation}
\mathcal Z(A_{\rm clock}) = \mathcal Z_*\left(\frac{A_{\rm clock}}{A_*}\right)^{(2+2\epsilon_{\rm field})/p} \, .
\end{equation}

The action is therefore not arbitrary; the kinetic function required for the observed scalar spectral flow is derived from the temporal-horizon branch.

Define the canonical variable $v_k=z_A\zeta_k$. The mode equation is

\begin{equation} \label{eq:v_k_mode}
v_k'' + \left[c_A^2k^2 - \frac{z_A''}{z_A}\right]v_k = 0 \, .
\end{equation}

With $z_A''/z_A=(\nu_A^2-\tfrac14)/\eta^2$ the Bunch-Davies solution is

\begin{equation}
v_k(\eta) = \frac{\sqrt{\pi|\eta|}}{2}\,H_{\nu_A}^{(1)}(k|\eta|) \, .
\end{equation}

Here $|\eta|$ denotes the local freeze-out coordinate measured relative to the effective sound-horizon crossing surface, not the asymptotic compactification coordinate used in the geodesic theorem; the two are related by a monotonic reparameterization, so the spectral index is invariant under the choice of conformal-time orientation. For $k|\eta|\ll 1$, $|\zeta_k|^2=|v_k|^2/z_A^2$ and the scalar power spectrum is

\begin{equation} \label{eq:P_zeta_Hankel}
P_\zeta(k) = \frac{k^3}{2\pi^2}\,|\zeta_k|^2 = A_s\left(\frac{k}{k_*}\right)^{3-2\nu_A} \, .
\end{equation}

Therefore $n_s-1=3-2\nu_A=-2\epsilon_{\rm field}$, recovering the scalar tilt relation from the action-level mode equation. The observed Planck value $n_s=0.9649$ gives

\begin{equation}
\epsilon_{\rm field} = \frac{1-n_s}{2} = 0.01755 \, .
\end{equation}

The running follows $\alpha_s=dn_s/d\ln k$. For the specified constant $\epsilon_{\rm field}$ and exact power-law spectrum, $\alpha_s=0$. A nonzero running requires a scale-dependent spectral-flow parameter or an additional correction derived from the action; it does not follow from $\epsilon_{\rm field}^2$ alone.

The domain of perturbative control is quantified by the pump field. Since $\mathcal Z(\chi)=\mathcal Z_*e^{(2+2\epsilon_{\rm field})\chi/p}$ has a positive exponent in $\chi$, both $\mathcal Z$ and $z_A=z_*(\eta/\eta_*)^{-1-\epsilon_{\rm field}}$ vanish only as $\eta\to\infty$, i.e. on the asymptotic frontier $A_{\rm clock}\to0$ that is the temporal horizon itself. At every finite $\eta$ the canonical normalization is finite and nonzero. A mode of wavenumber $k$ exits the effective sound horizon at $|\eta_k|=\sqrt{\nu_A^2-\tfrac14}/k$; in the oscillatory regime $|v_k|\simeq(2k)^{-1/2}$, so the per-decade variance of the field fluctuation $\delta\chi=v_k/z_A$ is

\begin{equation} \label{eq:P_dchi}
P_{\delta\chi}(k,\eta) \simeq \frac{k^2}{4\pi^2 z_A^2(\eta)} \;=\; P_{\delta\chi}(k,\eta_k)\left(\frac{\eta}{\eta_k}\right)^{2+2\epsilon_{\rm field}} \, ,
\end{equation}

growing toward the frontier but suppressed at freeze-out to the scalar-amplitude scale, $P_{\delta\chi}(k,\eta_k)\sim A_s$. Pipeline step 08b evaluates this across the CMB band $k\in[10^{-4},1]\,{\rm Mpc}^{-1}$ with the $A_s$-normalized pump ($z_*=0.53$ in the conventions of $\eqref{eq:z_star}$). For the pivot mode $k_*=0.05\,{\rm Mpc}^{-1}$, freeze-out occurs at $\eta_k\simeq30.9\,{\rm Mpc}$ with $z_A(\eta_k)\simeq113$, $P_{\delta\chi}\simeq4.3\times10^{-9}$, and $\delta\chi_{\rm rms}\simeq6.5\times10^{-5}$ — deep in the weak-coupling regime. The strong-coupling surface $P_{\delta\chi}\sim1$ lies at $\eta_{\rm sc}\simeq4.0\times10^{5}\,{\rm Mpc}$, some $4.1$ decades beyond freeze-out in the local mode coordinate; across the full band the controlled oscillatory window never falls below $4.07$ decades. The Bunch-Davies normalization is therefore imposed on modes inside a wide controlled window $\eta_k<\eta<\eta_{\rm sc}$, the spectrum is fixed at freeze-out, and the formal asymptotic limit in which $z_A\to0$ lies outside the domain in which the effective description is ever evaluated.

The remaining structure is a boundary statement rather than a defect: the pump-field zero is the strong-coupling frontier of the single-clock effective description, and it coincides asymptotically with the temporal horizon. The regularity results of Sections 3–4 are statements about the metric, which remains smooth; the field-space frontier is a statement about the scalar completion, which terminates at the same boundary. No controlled continuation of the perturbation sector through the horizon is claimed — the horizon bounds the effective field description, which is precisely its role in the temporal-horizon framework.

## 10.4 Observational Constraint and Amplitude Closure

The Planck 2018 measurement $n_s = 0.9649 \pm 0.0042$ (TT,TE,EE+lowE+lensing, 68% CL) constrains the temporal slow-roll parameter:

\begin{equation} \label{eq:epsilon_constraint}
\epsilon_{\rm field} = \frac{1 - n_s}{2} = 0.01755 \pm 0.0021 \, .
\end{equation}

This is a *consistency condition*: the model predicts a tilt, and the observed tilt fixes the spectral-flow parameter of the temporal action. In inflationary cosmology the analogous constraint $\epsilon = (1-n_s)/2$ fixes the shape of the inflaton potential; in TEP it fixes the kinetic slope of the temporal action.

The scalar amplitude $A_s = 2.10 \times 10^{-9}$ is fixed by the normalization of the temporal kinetic function. At the pivot,

\begin{equation}
P_\zeta(k_*) = A_s = \frac{2^{2\nu_A-3}\Gamma^2(\nu_A)}{\pi^3}\,\frac{1}{z_*^2}\,k_*^{3-2\nu_A}\,\eta_*^{1-2\nu_A} \, ,
\end{equation}

which fixes

\begin{equation} \label{eq:z_star}
z_*^2 = \frac{2^{2\nu_A-3}\Gamma^2(\nu_A)}{\pi^3 A_s}\,k_*^{3-2\nu_A}\,\eta_*^{1-2\nu_A} \, .
\end{equation}

The temporal kinetic normalization is therefore

\begin{equation}
\mathcal Z_* = \frac{z_*^2}{2M_{\rm Pl}^2} \, .
\end{equation}

The amplitude does not remain unexplained; it fixes the normalization of the temporal kinetic function $\mathcal Z_*$, in the same way that the observed scalar amplitude fixes the normalization of the inflaton potential in slow-roll inflation. The temporal horizon is the surface $A_{\rm clock}\to 0$ where the observational clock rate vanishes. Quantum fluctuations of the temporal field occur continuously in the local matter frame; as they cross the effective sound horizon their phase information becomes locked into the macroscopic topography of the temporal field. Because the conformal clock rate $A_{\rm clock}$ asymptotically approaches zero relative to the present epoch, these fluctuations appear frozen to a late-time observer. The nearly scale-invariant power spectrum is not the result of physical spatial stretching, but a fossilized record of local quantum dynamics projected across a relativistic temporal horizon.

The effective spectral boundary condition is therefore specified: the scalar spectral shape and amplitude are reproduced within the specified effective mode equations associated with the candidate temporal action $\eqref{eq:S_temporal}$ with the kinetic function $\eqref{eq:Z_A_clock}$ fixed by observation. The effective calculation adopts adiabatic single-clock initial conditions. Relative entropy perturbations of the matter species and cubic interactions are not calculated by the quadratic pump equations.

## 10.5 Tensor Pump Benchmark and Gravitational-Action Matching

**Action normalization and shared-lapse ADM embedding.** In the minimal constant-$M_{\rm Pl}$ Einstein–Hilbert term of $\eqref{eq:S_temporal}$ (and the constant-$M_{\rm Pl}$ homogeneous $u=0$ limit of Paper 0 Step 80, which enforces $c_{\rm GW}=c_\gamma$ and $\Delta t_{\gamma-\rm GW}=0$ on the shared cone), tensor ripples of $g_{\mu\nu}$ have pure-conformal matter-frame image $F=M_{\rm Pl}^2/A_{\rm clock}^2$ and tensor quadratic normalization $z_T=a_{\rm matter}\sqrt F$, which on a static gravitational background ($a_{\rm matter}=A_{\rm clock}$) gives $z_T=M_{\rm Pl}$ and $z_T''/z_T=0$. The $A_{\rm clock}''/A_{\rm clock}$ equation evaluated below is therefore the assigned temporal-conformal pump benchmark (corresponding to a matter-frame Jordan normalization where the spatial curvature term carries $\sqrt{F}\propto A_{\rm clock}$, distinct from the constant-$M_{\rm Pl}$ gravitational frame of $\eqref{eq:S_temporal}$). Its quadrature and profile-response results are retained as diagnostics, with $4k^3|\beta_k|^2/\pi^2$ mapped to dimensionless strain power via $M_{\rm Pl}^{-2}$.

The standard inflationary consistency relation $r=16\epsilon$ is not assumed in TEP-TH, because the temporal-horizon mechanism does not generate perturbations through quasi-de Sitter spatial inflation. Tensor modes must instead be derived directly from the temporal conformal metric. For transverse-traceless perturbations,

\begin{equation} \label{eq:tensor_metric}
d\tilde{s}^{2} = A_{\rm clock}^{2}(\eta)\,\bigl[-d\eta^{2} + (\delta_{ij}+h_{ij})\,dx^{i}\,dx^{j}\bigr] \, ,
\end{equation}

the canonical tensor variable $\mu_{k}=A_{\rm clock}\,h_{k}$ obeys

\begin{equation} \label{eq:tensor_eom}
\mu_{k}'' + \left(k^{2} - \frac{A_{\rm clock}''}{A_{\rm clock}}\right)\mu_{k} = 0 \, .
\end{equation}

For the temporal-horizon profile $A_{\rm clock}(\eta)\sim\eta^{-p}$ with $0 \lt p\lt1$, one has

\begin{equation} \label{eq:tensor_source}
\frac{A_{\rm clock}''}{A_{\rm clock}} = \frac{p(p+1)}{\eta^{2}} \to 0
\end{equation}

at the temporal boundary ($\eta\to\infty$). Thus the tensor equation approaches the Minkowski vacuum equation $\mu_{k}''+k^{2}\mu_{k}=0$. The temporal horizon does not generate the large tensor background predicted by the imported slow-roll estimate $r=16\epsilon_{\rm field}$. Tensor power is controlled only by the finite transition region where $A_{\rm clock}''/A_{\rm clock}$ is nonzero.

The tensor-to-scalar ratio is therefore not fixed by $16\epsilon_{\rm field}$ and must be computed by integrating the assigned tensor-pump equation $\eqref{eq:tensor_eom}$ across the transition profile. For the complete branch $0 \lt p\le\tfrac12$, the tensor index is

\begin{equation}
\nu_T = p + \frac12 \, ,
\end{equation}

because $p(p+1)=\nu_T^2-\tfrac14$. For $0 \lt p\le\tfrac12$ one has $\tfrac12\lt\nu_T\le 1$, while the scalar index is $\nu_A=\tfrac32+\epsilon_{\rm field}\approx 1.5175$. Therefore $\nu_T\neq\nu_A$, and the inflationary consistency relation $r=16\epsilon$ is not a theorem of TEP-TH. The scalar sector is near scale invariant, but the tensor sector is not amplified in the same way; tensor power is controlled only by the finite transition region where $A_{\rm clock}''/A_{\rm clock}$ is nonzero. No ad hoc suppression mechanism is assumed; the only control parameter is the finite shape of $A_{\rm clock}(\eta)$ in the transition region.

## 10.6 Tensor Pump Integration and Conditional Response

The explicit first-order Bogoliubov coefficient is obtained by quadrature of the source term $V(\eta)=A_{\rm clock}''/A_{\rm clock}$ against the free Minkowski mode:

\begin{equation}
\beta_{k} \simeq -\frac{i}{2k}\int_{0}^{\infty} V(\eta)\,e^{-2ik\eta}\,d\eta \, .
\end{equation}

In dimensionless units $(\tilde{\eta}=\eta/\eta_{0}, \tilde{k}=k\eta_{0})$ the integral becomes $\beta_{\tilde{k}}=-(i/2\tilde{k})\int_{0}^{\infty}\tilde{V}(\tilde{\eta})\,e^{-2i\tilde{k}\tilde{\eta}}\,d\tilde{\eta}$ with $\tilde{V}(\tilde{\eta})=\eta_{0}^{2}V(\eta)$. The tensor power spectrum for the two polarization states is

\begin{equation}
P_{T}(k) = \frac{4k^{3}}{\pi^{2}}\,|\beta_{k}|^{2} \, ,
\end{equation}

and the tensor-to-scalar ratio at any wavenumber is

\begin{equation}
r(k) = \frac{P_{T}(k)}{P_{\zeta}(k)} \, .
\end{equation}

Step 09b evaluates this numerically for the temporal-horizon transition profile $A_{\rm clock}(\eta)=C[1+(\eta/\eta_0)^n]^{-p/n}$ with fiducial parameters $p=0.1$, $\eta_0=6000$ Mpc, and $n=2$. The Bogoliubov integral is evaluated with a weighted oscillatory (Filon) quadrature rule, cross-verified against explicit half-period cell integration to a relative accuracy better than $2\times10^{-4}$ at every $\tilde k$ (the fixed-subdivision integrator is noise-dominated once the integrand oscillates $\tilde k/\pi\sim10^{3}$ times across the transition). Because $k\eta_0\sim 300$ for CMB-scale modes, rapid oscillations of $e^{-2ik\eta}$ across the transition strongly suppress the integral. The spectrum is largest at the transition scale $\tilde k\sim 1$ ($k\sim2\times10^{-4}\ {\rm Mpc}^{-1}$) and falls as $\tilde k^{-4}$ at CMB scales. The resulting tensor-to-scalar ratio is

\begin{equation}
r(k_{\rm pivot}) = 1.9 \times 10^{-9} \, , \qquad r_{\rm max} = 5.2 \times 10^{-7} \,
\end{equation}

both far below the BICEP/Keck 2021 bound $r \lt 0.036$ (95% CL) and below the $r\sim10^{-4}$ sensitivity floor of CMB-S4. The analytic parametric estimate $r\sim p^2/(4\pi^2\eta_0^3 A_s k_{\rm pivot}^3)\approx 4.5\times 10^{-3}$ is a coarse upper bound that omits the rapid oscillatory suppression $e^{-2ik\eta}$ across the finite transition region; the numerical integration, which includes this suppression, gives the substantially smaller value quoted above. Both estimates are below the observational bound.

### Robustness of Tensor Suppression

Table 1 reports the maximum tensor-to-scalar ratio $r_{\rm max}$ across the full wavenumber range $k\in[10^{-4},1]$ Mpc$^{-1}$ for variations of the three transition-profile parameters — the falsification surface $r_{\rm max}(p,n,\eta_0)$ of the temporal-horizon tensor sector. The maximum is always attained at the transition scale $\tilde k\sim1$; the quoted figures are evaluated with the cross-verified oscillatory quadrature described above. All values remain orders of magnitude below the BICEP/Keck 2021 bound $r\lt0.036$.

| Parameter | Range | $r_{\rm max}$ | Effect |
| --- | --- | --- | --- |
| $p$ | 0.05 | $1.3\times 10^{-7}$ | Scales approximately as $p^{2}$ at small $p$ |
| $p$ | 0.10 (fiducial) | $5.2\times 10^{-7}$ | Baseline |
| $p$ | 0.20 | $2.1\times 10^{-6}$ | Increases with $p$ |
| $p$ | 0.50 (regular-branch edge) | $1.4\times 10^{-5}$ | Largest on the curvature-regular branch |
| $p$ | 1.00 (curvature-excluded) | $6.1\times 10^{-5}$ | Largest over all tested profiles |
| $n$ | 1 | $2.9\times 10^{-7}$ | Weak dependence on transition steepness |
| $n$ | 2 (fiducial) | $5.2\times 10^{-7}$ | Baseline |
| $n$ | 4 | $7.3\times 10^{-7}$ | Steeper transition mildly enhances production |
| $\eta_{0}$ (Mpc) | 3000 | $4.3\times 10^{-6}$ | Smaller $\eta_0$ weakens oscillatory suppression |
| $\eta_{0}$ (Mpc) | 6000 (fiducial) | $5.2\times 10^{-7}$ | Baseline |
| $\eta_{0}$ (Mpc) | 12000 | $6.4\times 10^{-8}$ | Larger $\eta_{0}$ strengthens oscillatory suppression |

The table samples one parameter at a time and does not bound all simultaneous parameter combinations. For example, the assigned pump diagnostic at $p=0.5$, $n=2$, $\eta_0=3000$ Mpc gives a maximum near $1.14\times10^{-4}$, exceeding the earlier proposed $10^{-4}$ universal threshold. Moreover, these diagnostic values have not been promoted to a dimensionless action-normalized tensor spectrum. A model-wide B-mode falsification threshold therefore requires both the action match and a jointly bounded parameter domain; the sampled table alone does not provide it.

## 10.7 Theorem 2 — Native Scalar and Tensor Spectra

The derivation above is summarized in the following theorem.

**Theorem 2 (Spectra of the specified effective pump equations).** For the effective scalar and tensor mode equations specified below, with the candidate temporal action

\begin{equation}
S_A = \int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R - \frac{M_{\rm Pl}^2}{2}\,\mathcal Z(A)(\nabla\ln A)^2 - M_{\rm Pl}^2\,U(A)\right] \, ,
\end{equation}

with $A_{\rm clock}=C\eta^{-p}$, $0 \lt p\le\tfrac12$, and kinetic normalization

\begin{equation}
\mathcal Z(A) = \mathcal Z_*\left(\frac{A}{A_*}\right)^{(2+2\epsilon_{\rm field})/p} \, ,
\end{equation}

scalar clock perturbations obey

\begin{equation}
v_k'' + \left[k^2 - \frac{\nu_A^2-\frac14}{\eta^2}\right]v_k = 0 \, , \qquad \nu_A = \frac32 + \epsilon_{\rm field} \, ,
\end{equation}

yielding

\begin{equation}
P_\zeta(k) = A_s\left(\frac{k}{k_*}\right)^{-2\epsilon_{\rm field}} \, , \qquad n_s = 1 - 2\epsilon_{\rm field} \, .
\end{equation}

Tensor modes obey

\begin{equation}
\mu_k'' + \left[k^2 - \frac{p(p+1)}{\eta^2}\right]\mu_k = 0 \, ,
\end{equation}

so their index is

\begin{equation}
\nu_T = p + \frac12 \, .
\end{equation}

Since $\nu_T \neq \nu_A$, the inflationary consistency relation $r=16\epsilon$ is not a theorem of TEP-TH. Tensor power must be computed from the native temporal-conformal equation and is controlled by the finite transition profile.

## 10.8 Pipeline Validation

The pipeline evaluates the TEP scalar power spectrum over $k \in [10^{-4}, 1]$ Mpc$^{-1}$ using the derived formula $\eqref{eq:P_zeta_Hankel}$ with the slow-roll parameters $\eqref{eq:epsilon_def}$. The controlling parameter is the spectral-flow parameter $\epsilon_{\rm field}$ of $\eqref{eq:epsilon_def}$, distinct from the background-response constant $\epsilon_{\rm dyn}=8\pi G U_{\rm c}/H_0^2$ of Section 5.1; at the pipeline default $\epsilon_{\rm field}=0.0055$ the derived index is $n_s=0.989$, and for a generic value $\epsilon_{\rm field}=0.10$ it is $n_s = 0.80$, redder than the observed value because the temporal field rolls more slowly than the observed tilt requires. When the parameter is set to the Planck-constrained value $\epsilon_{\rm field} = 0.01755$ (`planck_calibrated_evaluation` in Step 08), the TEP spectrum reproduces the observed tilt $n_s = 0.9649$ identically, with the second-order running $\alpha_s = -2\epsilon_{\rm field}^2 = -6.2\times10^{-4}$ keeping $P_\mathcal{R}(k)$ within $0.35\%$ RMS ($1.2\%$ maximum at $k=10^{-4}\ {\rm Mpc}^{-1}$) of the pure power-law reference across the full four-decade $k$-range. Step 08b evaluates the domain of perturbative control $\eqref{eq:P_dchi}$ on the same band, confirming that freeze-out occurs more than four decades inside the strong-coupling surface for every mode and that $z_A$ vanishes only asymptotically at the temporal-horizon frontier.

The effective spectral boundary condition is therefore specified: quantum fluctuations of the conformal clock field freeze at effective sound-horizon crossing inside the controlled domain and appear fossilized to a late-time observer relative to the temporal horizon, producing a nearly scale-invariant adiabatic spectrum whose tilt and running are derived from the native temporal action $\eqref{eq:S_temporal}$. The observed Planck values fix the spectral-flow parameter to $\epsilon_{\rm field} = 0.01755$ and the kinetic normalization $\mathcal Z_*$ through the observed amplitude $A_s = 2.10\times 10^{-9}$. The observed tilt and amplitude fix the effective spectral-flow parameter and kinetic normalization; their common-action derivation is separate from this reconstruction.

The construction above fixes the effective scalar spectrum: the native temporal action $\eqref{eq:S_temporal}$ with the kinetic function $\eqref{eq:Z_A_clock}$ produces the observed scalar spectrum, and the amplitude $A_s$ fixes the normalization $\mathcal Z_*$ in the same way that the inflationary amplitude fixes the inflaton potential. This complements the linear pure-conformal scalar perturbation closure established in TEP-HC (Paper 18), where the Bellini–Sawicki functions $\alpha_M=-2\alpha_A$, $\alpha_B=2\alpha_A$, $\alpha_K=w_c\,\alpha_A^2$ ($w_c = Z_E-6$), and $\alpha_T=0$ were derived and the $\delta\phi$ sector was evolved natively through the Einstein–Boltzmann hierarchy. That audit sharpened the stability statement: the canonical Einstein-frame image $\alpha_K=-5\alpha_A^2$ ($w_c=-5$) passes the ghost discriminant yet is linearly unstable on the conformal background (tachyonic scalarization), while the screened production branch $w_c = 700$ is stable and restores $\Lambda$CDM-level growth. Together, TEP-HC supplies active-solver constraints within its screened effective closure, TEP-TH supplies the temporal-horizon primordial spectrum, and Paper 0 Step 80 embeds the shared-lapse ADM gravitational and matter sectors in a single covariant action whose pre-boundary ambient clock-slope acoustic closure is evaluated directly in TEP-BBN Step 20 and TEP-HC Step 21.

# 11. Pipeline Summary and Internal Consistency

Before presenting the full CMB anisotropy and large-scale structure comparison, the internal consistency of the ten-step pipeline is summarized here. The claims are organized into three tiers. *Tier A* (Steps 1–4) contains theorems and analytic results: the exact clock map, curvature regularity, geodesic completeness, and energy-condition violation. *Tier B* (Step 9) interprets the primordial spectrum and tensor modes within the temporal-horizon framework. No downstream background or thermal observable is tuned. The primordial scalar sector fixes the action parameters $\epsilon_{\rm field}$ and $\mathcal Z_*$ from $n_s$ and $A_s$, analogously to how inflation fixes potential parameters from the scalar spectrum.

## Tier A: Theorems and Analytic Results

| Step | Claim | Basis | Status |
| --- | --- | --- | --- |
| 1 | $A_{\rm clock}=(1+z)^{-1}$ exact; $A_{\rm dyn}$ distinct projection | Definition + numerical (tol. $10^{-6}$) | Theorem |
| 2 | Curvature invariants vanish at boundary ($A_{\rm clock}=C\eta^{-p}$, $0 \lt p\lt1$) | Proposition 1 (closed-form substitution) | Proven |
| 3 | Null geodesics affine-complete for $0 \lt p\le\tfrac12$ | Analytic integral + numerical | Proven |
| 3b | Comoving proper time infinite for $0 \lt p\le1$; arbitrary timelike geodesics complete for $0 \lt p\le\tfrac12$ | Analytic integral + numerical | Proven |
| 4 | Assigned fluid diagnostic violates SEC; reconstructed effective action violates SEC asymptotically when $U>2K$ | Hawking–Penrose prerequisite check | Proven |

<!-- deleted tier B -->

## Tier B: Primordial Perturbations and Tensor Modes

| Step | Claim | Basis | Status |
| --- | --- | --- | --- |
| 9 | Scalar tilt $n_s - 1 = -2\epsilon_{\rm field}$; $\epsilon_{\rm field}=0.01755$ from Planck | Spectral-flow parameter of clock-field fluctuations | Consistency condition |
| 08b | Perturbative control at freeze-out: $z_A\to0$ only asymptotically; $\eta_{\rm sc}/\eta_k\gtrsim1.2\times10^{4}$ across the CMB band | Pump-field and variance growth $P_{\delta\chi}\propto(\eta/\eta_k)^{2+2\epsilon_{\rm field}}$ | Controlled; frontier bounds the EFT |
| 09b | Assigned tensor-pump diagnostic: $r(k_{\rm pivot})=1.9\times 10^{-9}$, $r_{\rm max}=5.2\times 10^{-7}$ | Numerical integration of $\mu_k''+(k^2-A_{\rm clock}''/A_{\rm clock})\mu_k=0$ | Below BICEP/Keck $r\lt0.036$ |

The pipeline separates the geometric theorems from the effective spectral construction and the imported thermal calculations. Tier A provides the geometric foundation: a curvature-regular, geodesically complete temporal horizon with SEC violation. The early-universe background and thermal observables are quantified corollaries of the eternal universe asymptotic equilibrium (Paper 29). Tier B derives the scalar spectral shape from clock-field fluctuations and evaluates the assigned tensor-pump diagnostic, whose action normalization is distinguished in Section 10.5. The imported inflationary consistency relation $r=16\epsilon_{\rm field}$ is not assumed.

## Minimal Model Status

| Sector | Status |
| --- | --- |
| Temporal-horizon mapping | viable ($A_{\rm clock}$ exact, $A_{\rm dyn}$ physical) |
| Curvature invariants | vanish at boundary for $A_{\rm clock}=C\eta^{-p}$, $0 \lt p\lt1$ |
| Null geodesics | affine-complete for $0 \lt p\le\tfrac12$ |
| Timelike geodesics | comoving proper time infinite for $0 \lt p\le1$; arbitrary timelike geodesics complete for $0 \lt p\le\tfrac12$ |
| Scalar tilt | matched by $\epsilon_{\rm field}=0.01755$ |
| Scalar amplitude | fixes kinetic normalization $\mathcal Z_*$ |
| Tensor ratio | assigned pump integrated; fiducial diagnostic $r_{\rm max}=5.2\times10^{-7}$; physical action normalization remains separate |

**Auxiliary numerical checks.** The recombination benchmark solves the existing Saha–Peebles equations with the Radau integrator and checks the zero-amplitude limit against the same comparator. When the optional CLASS import is unavailable, the output explicitly identifies this approximation. The spectral transport check uses photon-number-conserving chemical-potential and Compton-y templates with absolute input errors; it reports an optional CLASS ΛCDM reference separately. Its homogeneous blackbody-preservation identity is a transport check, and absent FIRAS data are not represented as observations.

*Imported thermal benchmark.* The auxiliary `step_04_full_bbn_abundances.py` evaluates the AlterBBN network with a single-epoch expansion-rate mapping to extra radiation. Screening enters through the computed conformal factor, and a nonzero mapped perturbation is evaluated by the network. Failed network runs stop rather than supply reference abundances. The helium anchor is the observational $Y_p=0.245\pm0.003$ from the PDG 2024 BBN review; the deuterium anchor retains the stated measurement selection. $N_{\rm eff}=3.046$ is an assumed reference and is excluded from the primary abundance pass count. These conditional benchmark results are distinct from the eternal-universe abundance budgets and transport calculations in Paper 29.

## 11.1 Falsifiable Predictions

The following near-term observational tests would strengthen or falsify the Temporal Horizon Cosmology framework.

- **Tensor action and transition-profile test.** The assigned pump integrations provide cross-checked conditional diagnostics, with the fiducial values reported in Section 10.6. The tensor normalization of the shared action must first be matched to that pump before those values become physical B-mode predictions. The one-parameter scan does not bound every joint profile combination: $p=0.5$, $n=2$, $\eta_0=3000$ Mpc already yields a diagnostic maximum near $1.14\times10^{-4}$. The earlier universal $r\gtrsim10^{-4}$ exclusion threshold is therefore withdrawn. A quantitative observational threshold requires an action-normalized spectrum and a specified joint parameter domain.

- **21-cm power spectrum at cosmic dawn.** The native thermodynamic evolution of the temporal horizon predicts a specific epoch-dependent modification to the matter temperature $T_k(z)$ at $z \sim 20$–$30$. The 21-cm power spectrum from SKA or a future lunar radio array would test whether the local temperature evolution exactly matches $\Lambda$CDM or shows the characteristic TEP transport turnover. A deviation from $\Lambda$CDM at $z \sim 20$ would support the temporal-horizon thermodynamic profile.

- **Gravitational-wave propagation speed variation.** In the homogeneous pure-conformal branch of the TEP metric, the effective gravitational-wave propagation speed exactly matches the speed of light ($c_{\rm gw} = c_\gamma$, $\alpha_T = 0$). Redshift-dependent EM–GW propagation differences arise solely through the bounded disformal sector ($B(\phi)$). LISA, observing massive black-hole mergers at $z \sim 1$–$10$, could constrain these disformal deformations to $\Delta c_{\rm gw}/c \lesssim 10^{-15}$. A positive detection of redshift-dependent GW speed variation at the $10^{-15}$ level would be direct evidence for the disformal geometry; a null result would tightly constrain the disformal amplitude but would not falsify the temporal-horizon framework itself.

- **Local excitation temperature at depth.** Rotational excitation of CN, CO and C&thinsp;I in high-redshift quasar absorption systems thermometers the ambient radiation field *at the absorber's own location*. The temporal-horizon law returns $T_{\rm loc}(z) = T_0/A_{\rm clock}(z) = T_0(1+z)$ natively at every depth, so the standard $T_{\rm CMB}(z)=T_0(1+z)$ excitation profile is a hard prediction requiring no transport assumption. Step 11 confronts it with the published CO absorber sample ($z=0.89$–$2.69$): $\chi^2/{\rm dof}=0.15$ ($\chi^2=1.08$), fitted exponent $\beta=+0.003\pm0.023$, versus $\chi^2=865.8$ for the constant-temperature null (descriptive $\sqrt{\Delta\chi^2}=29.4$) — the tested temperature law is corroborated on real data. Because local collisional excitation or ultraviolet pumping in dense clouds can only elevate $T_{\rm ex}$ above the ambient radiation bath ($T_{\rm ex}\ge T_{\rm loc}(z)$), the quiescent lower envelope across the absorber population must track $T_0(1+z)$; a systematic departure of that quiescent floor below $T_0(1+z)$ toward $T_0$ would discriminate directly against the local-temperature law, whereas continued confirmation of the $T_0(1+z)$ floor at $z\gtrsim3$ extends the depth over which the clock map is observationally validated.

Tensor and 21-cm observations are prospective tests whose quantitative TEP predictions require the action and thermal-profile matching described above. GW–EM propagation tests constrain the disformal sector; a null result does not exclude the pure-conformal boundary geometry. Excitation-temperature measurements probe the local thermal law directly and are the sharpest existing discriminator between a temporal-depth temperature gradient and any mechanism in which the ambient radiation field stays at $T_0$ along the path.

# 12. Conclusion

This paper constructs a curvature-regular, causally complete temporal-conformal branch as a candidate alternative to the singular FLRW past boundary. On the specified branch, the conformal clock rate vanishes only at an infinite-affine asymptote. The regular branch and the singular conformal benchmark are distinct causal completions; a change of clock convention alone does not remove a physical matter-frame singularity. Deriving the regular realization from the universal master action remains the common construction identified in Section 2.

The central temporal-horizon mapping is established: $a_{\rm eff}\to0$ corresponds to $A_{\rm clock}\to0$, where the exact observational clock map $A_{\rm clock}(z)=(1+z)^{-1}$ vanishes at infinite redshift. The dynamical response $A_{\rm dyn}(z)=\left(1+z/z_{t}\right)^{-\epsilon_{\rm dyn}}$ encodes the late-time TEP shear correction. Section 11 presents the integrated ten-step pipeline; the background and thermal checks retain their stated inputs, while the effective scalar kinetic slope and normalization are reconstructed from the observed $n_s$ and $A_s$. The key findings are:

- For the temporal-horizon profile $A_{\rm clock}(\eta)=C\eta^{-p}$ with $0 \lt p\le\tfrac12$, all polynomial curvature invariants vanish at the temporal conformal boundary; the boundary is asymptotically curvature-empty, timelike-complete, and null-complete

- Comoving proper time diverges for $0 \lt p\le1$; arbitrary timelike geodesics are complete for $0 \lt p\le\tfrac12$; null affine parameter diverges for $0 \lt p\le\tfrac12$. The boundary is a regular conformal-temporal endpoint, analogous to a smooth spacelike conformal boundary

- The effective stress-energy tensor of the temporal field violates the Strong Energy Condition, removing one of the assumptions required by the Hawking-Penrose singularity theorems; geodesic completeness is established separately by the curvature and affine-parameter analysis

- Native Local Thermodynamic Evolution in an eternal universe replaces the singular expanding-origin interpretation of the hot thermal state — the high-redshift plasma itself is retained, as Sections 7 and 8 operationally require — providing an eternal-universe framework in which chemical states can approach long-term asymptotic equilibria; the quantitative chemical mechanism and its exposure conditions are evaluated in TEP-BBN (an active research problem) without requiring a phenomenological screening scale.

- Standard BBN assumptions are replaced: the thermal and chemical states are modeled as candidate asymptotic equilibria (TEP-BBN) where D/H is not uniquely primordial and helium arises via baryonic cycling, without requiring a physical zero-volume Big Bang

- TEP-BBN supplies the native chemical-evolution framework and a proof of concept for local CMB thermalization; the present TEP-TH pipeline re-evaluates recombination visibility within the temporal-horizon geometry, while TEP-HC supplies the independent acoustic-sector closure.

- The temporal-horizon thermal mapping preserves a FIRAS-compatible blackbody spectrum without forbidden $\mu$ or $y$ spectral distortions

- Entropy and arrow-of-time analysis demonstrates thermodynamic regularity at the temporal horizon

- The scalar shape of the primordial perturbation spectrum is derived from fluctuations of the clock field $\zeta=\delta\ln A_{\rm clock}$, with spectral-flow parameter $n_s-1=-2\epsilon_{\rm field}$. The observed Planck value $n_s = 0.9649$ constrains $\epsilon_{\rm field} = 0.01755$

- Tensor modes obey a assigned temporal-conformal pump equation; for $A_{\rm clock}(\eta)\sim\eta^{-p}$ the source term $A_{\rm clock}''/A_{\rm clock}\to 0$ at the horizon, so no large primordial tensor background is generated at leading order; the imported inflationary consistency relation $r=16\epsilon_{\rm field}$ is not assumed; numerical integration of the assigned tensor-pump equation yields $r(k_{\rm pivot})=1.9\times 10^{-9}$ and $r_{\rm max}=5.2\times 10^{-7}$, well below the BICEP/Keck bound $r\lt0.036$

- CMB anisotropy spectra (TT, TE, EE) and LSS observables (matter power spectrum, growth factor $f\sigma_8$, BAO scales) are preserved via conformal acoustic equivalence as confirmed by TEP-HC (Paper 18)

The causal matter-frame universe is curvature-regular at the temporal conformal boundary. The apparent Big Bang is a temporal horizon, not a physical curvature singularity. The temporal-horizon geometry supplies a nonsingular framework in which the standard background and acoustic observables are reconstructed by the conformal mapping, while TEP-BBN provides the native chemical-evolution mechanism and a proof of concept for local CMB thermalization; the scalar perturbation shape is reproduced, and tensor production is suppressed at leading order by the vanishing of the temporal-horizon source term. Together with the distance-redshift evidence from TEP-C0 (Paper 26) and the acoustic-sector `hi_class` validation from TEP-HC (Paper 18), TEP-TH supplies the regular-boundary and effective-spectrum parts of the cosmological sequence: the foundational geometrical and thermodynamic signatures conventionally attributed to a hot Big Bang singularity can be modeled within a static conformal temporal-transport geometry.

**Implications:** The temporal-horizon cosmology of the TEP framework replaces the standard Big Bang interpretation. In the complete temporal-horizon branch, the universe extends backward through an infinite affine past without a physical curvature singularity. The temporal horizon is strictly an observational boundary where the relative conformal clock rate vanishes, meaning cosmic history must be mapped by local thermodynamic state variables rather than a global chronological stopwatch. Cosmic expansion is a geometric reconstruction of accumulated open-path conformal temporal shear. The background and thermal observational signatures conventionally attributed to a hot dense origin—light-element abundances, acoustic peaks, blackbody thermalization, and large-scale structure—can be reconstructed within the combined eternal-universe thermodynamic and conformal-acoustic framework. The tensor-to-scalar ratio must be computed from the finite transition region via the assigned temporal-conformal pump equation, not from an imported inflationary consistency relation. The eternal-branch background carries a corresponding caveat registered in the homogeneous analysis: the closed static solution is not a dynamical attractor — its linearization exhibits an Eddington-type secular mode with e-folding $\sim a/c$ — and control of the analogous mode in the inhomogeneous realization remains part of the open construction (Paper 0, §8).

**Outlook:** Figure 1 (Section 4.5) illustrates the conformal-boundary interpretation: the singular lower edge of standard flat $\Lambda$CDM is replaced by a smooth regular temporal conformal boundary $\mathscr{T}^{-}$, where $A_{\rm clock}\to0$ and curvature invariants vanish. The apparent Big Bang is a regular conformal-temporal endpoint, not a physical singularity. Step 09b is complete: the assigned tensor-pump equation yields $r(k_{\rm pivot})=1.9\times 10^{-9}$ and $r_{\rm max}=5.2\times 10^{-7}$, well below current and projected CMB bounds. Closed-loop synchronization holonomy remains the primary discriminant of the non-exact/disformal sector of TEP. In the homogeneous conformal limit analysed here, $A_{\rm clock}$ gives open-path temporal redshift but does not by itself generate residual loop holonomy, since $\oint d\ln A_{\rm clock}=0$. A nonzero $\mathcal{H}_{\rm resid}$ would require the disformal contribution $B(\phi)\nabla_{\mu}\phi\nabla_{\nu}\phi$, non-metricity, or another non-exact synchronization structure, as developed in the foundational TEP paper (Jakarta).

**Common-action scope.** The regularity and completeness results apply to the specified matter-frame metric. The scalar spectrum is reconstructed using the observed tilt and amplitude. The quoted tensor values belong to an assigned pump diagnostic; Section 10.5 distinguishes it from the tensor quadratic action of the static gravitational background. They are not yet a universal action-normalized tensor prediction or a model-wide B-mode exclusion threshold. HC's acoustic preservation and BBN's thermal/chemical calculations retain their respective reference-model and native-boundary assumptions; matching their complete transfer histories is a separate calculation.

# 13. References

- Smawfield, M.L. Temporal Equivalence Principle: Dynamic Time & Emergent Light Speed. *Zenodo* (2025), v0.16 (Jakarta). DOI: 10.5281/zenodo.16921911

- Smawfield, M.L. Temporal Equivalence Principle: A Covariant Alternative to Cosmic Expansion. *Zenodo* (2026). DOI: 10.5281/zenodo.20370143

- Smawfield, M.L. Temporal Equivalence Principle: Native hi_class Conformal Implementation, Linear Perturbation Closure, and CMB Acoustic Peak Preservation. *Zenodo* (2026). DOI: 10.5281/zenodo.20572722

- Smawfield, M.L. Temporal Equivalence Principle: Dynamical Proper Time and the Illusion of Primordial Deuterium. *Zenodo* (2026). DOI: 10.5281/zenodo.21841147

- Hawking, S.W. The occurrence of singularities in cosmology. *Proc. R. Soc. A* **294**, 511-521 (1966).

- Hawking, S.W. & Penrose, R. The singularities of gravitational collapse and cosmology. *Proc. R. Soc. A* **314**, 529-548 (1970).

- Borde, A., Guth, A.H. & Vilenkin, A. Inflationary spacetimes are incomplete in past directions. *Phys. Rev. Lett.* **90**, 151301 (2003).

- Brandenberger, R. & Peter, P. Bouncing cosmologies: progress and problems. *Found. Phys.* **47**, 797-850 (2017).

- Novello, M. & Bergliaffa, S.E.P. Bouncing cosmologies. *Phys. Rep.* **463**, 127-213 (2008).

- Ijjas, A. & Steinhardt, P.J. Entropy, black holes and the new cyclic universe. *Phys. Lett. B* **824**, 136823 (2022).

- Peebles, P.J.E. *Principles of Physical Cosmology*. Princeton University Press (1993).

- Weinberg, S. *Cosmology*. Oxford University Press (2008).

- Dodelson, S. *Modern Cosmology*. Academic Press (2003).

- Mukhanov, V.F., Feldman, H.A. & Brandenberger, R.H. Theory of cosmological perturbations. *Phys. Rep.* **215**, 203-333 (1992).

- Liddle, A.R. & Lyth, D.H. *Cosmological Inflation and Large-Scale Structure*. Cambridge University Press (2000).

- Planck Collaboration, et al. Planck 2018 results. VI. Cosmological parameters. *A&A* **641**, A6 (2020).

- Riess, A.G., et al. Milky Way Cepheid Standards for Measuring Cosmic Distances and Application to Gaia DR2: Implications for the Hubble Constant. *ApJ* **861**, 126 (2018).

- Brout, D., et al. The Pantheon+ Analysis: Cosmological Constraints. *ApJ* **938**, 110 (2022).

- Fixsen, D.J., et al. The Cosmic Microwave Background Spectrum from the Full COBE FIRAS Data Set. *ApJ* **473**, 576 (1996).

- Chluba, J. & Sunyaev, R.A. The evolution of CMB spectral distortions in the early Universe. *MNRAS* **419**, 1294-1314 (2012).

- PARTICLE DATA GROUP. Review of Particle Physics. *PTEP* **2022**, 083C01 (2022).

- Cyburt, R.H., Fields, B.D., Olive, K.A. & Yeh, T.H. Big bang nucleosynthesis: Present status. *Rev. Mod. Phys.* **88**, 015004 (2016).

- Seager, S., Sasselov, D.D. & Scott, D. A new calculation of the recombination epoch. *ApJ* **523**, L1-L5 (1999).

- Peebles, P.J.E. Recombination of the Primeval Plasma. *ApJ* **153**, 1 (1968).

- Zeldovich, Y.B. & Sunyaev, R.A. The interaction of matter and radiation in a hot-model universe. *Astrophys. Space Sci.* **4**, 301-316 (1969).

- Seljak, U. & Zaldarriaga, M. A Line of Sight Integration Approach to Cosmic Microwave Background Anisotropies. *ApJ* **469**, 437 (1996).

- Lewis, A., Challinor, A., & Lasenby, A. Efficient Computation of CMB Anisotropies in Closed FRW Models. *ApJ* **538**, 473 (2000).

- Lesgourgues, J. & Tram, T. The Cosmic Linear Anisotropy Solving System (CLASS). Part IV: efficient implementation of non-cold relics. *JCAP* **09**, 032 (2011).

- Zumalacárregui, M., Bellini, E., Sawicki, I., Lesgourgues, J. & Ferreira, P.G. hi_class: Horndeski in the Cosmic Linear Anisotropy Solving System. *JCAP* **08**, 019 (2017).

- De Felice, A. & Tsujikawa, S. f(R) Theories. *Living Rev. Rel.* **13**, 3 (2010).

- Wetterich, C. Cosmology and the fate of dilatation symmetry. *Nucl. Phys. B* **302**, 668-696 (1988).

- Wetterich, C. A universe without expansion. *Phys. Dark Universe* **2**, 184 (2013).

- Narlikar, J.V. & Arp, H.C. Flat spacetime cosmology: A unified framework for extragalactic redshifts. *Astrophys. J.* **405**, 51-56 (1993).

- Mannheim, P.D. Conformal gravity and the nature of dark matter. *Prog. Part. Nucl. Phys.* **94**, 217-272 (2017).

- Khoury, J. & Weltman, A. Chameleon cosmology. *Phys. Rev. D* **69**, 044026 (2004).

- Hinterbichler, K. & Khoury, J. Symmetron cosmology. *Phys. Rev. Lett.* **104**, 231301 (2010).

- Penrose, R. Before the Big Bang: an outrageous new perspective and its implications for particle physics. *Proc. EPAC* (2006).

- Tod, K.P. Isotropic cosmological singularities. *Gen. Relativ. Gravit.* **35**, 779-805 (2003).

- Tod, K.P. The equations of conformal cyclic cosmology. *Gen. Relativ. Gravit.* **47**, 31 (2015).

- Ratra, B. & Peebles, P.J.E. Cosmological Consequences of a Rolling Homogeneous Scalar Field. *Phys. Rev. D* **37**, 3406 (1988).

- Caldwell, R.R., Dave, R., & Steinhardt, P.J. Cosmological Imprint of an Energy Component with General Equation of State. *Phys. Rev. Lett.* **80**, 1582 (1998).

- Clifton, T., Ferreira, P.G., Padilla, A. & Skordis, C. Modified gravity and cosmology. *Phys. Rep.* **513**, 1-189 (2012).

# Acknowledgements

The author thanks his mother, J.S., who once attended a Penrose lecture in New Delhi, for a book that initiated his study of conformal infinity.

# Unified TEP Parameter Dictionary

The TEP corpus uses related but distinct symbols across its papers. This dictionary maps every parameter, its definition, the paper where it is primary, and its fiducial or fitted value.

| Symbol | Definition | Primary Paper | Fiducial / Fitted Value |
| --- | --- | --- | --- |
| $A_{\rm clock}(z)$ | Exact observational clock/redshift map: $A_{\rm clock}=(1+z)^{-1}$ | TEP-TH | $(1+z)^{-1}$ (exact) |
| $A_{\rm dyn}(z)$ | Dynamical shear response: $\left(1+z/z_t\right)^{-\epsilon_{\rm dyn}}$ | TEP-TH | Modifies late time evolution |
| $\alpha_A$ | Runtime logarithmic derivative $\alpha_A=d\ln A_{\rm HC}/d\ln a$; distinct from the exact endpoint map $A_{\rm clock}$ | TEP-HC | Redshift-dependent; zero at the finite-profile turnover |
| $\alpha_M$, $\alpha_B$, $\alpha_K$, $\alpha_T$ | Runtime Bellini–Sawicki EFT functions: $\alpha_M=-2\alpha_A$, $\alpha_B=2\alpha_A$, $\alpha_K=w_c\,\alpha_A^2$ with $w_c=Z_E-6$ (production $w_c=700$; the canonical image $w_c=-5$ is linearly unstable — Paper 18 closure audit), $\alpha_T=0$ | TEP-HC | Adopted from $\alpha_A$ |
| $\epsilon_T^{\rm los}$ | Late-time line-of-sight transport amplitude (C0 supernova fit) | TEP-C0 | $\mathcal{U}[0, 2.0]$ (prior); posterior peaked near $\sim 0.89$ |
| $\epsilon_T^{\rm CMB}$ | C0 background/acoustic diagnostic amplitude | TEP-C0 | $-0.0015\pm0.0037$ |
| $\epsilon_T^{\rm HC}$ | Native hi_class homogeneous conformal amplitude | TEP-HC | $0.0043\pm0.0025$ (full high-$\ell$ likelihood) |
| $\epsilon_{\rm dyn}$ | Dynamical temporal-horizon response | TEP-TH | Modulates late-time expansion |
| $\epsilon_{\rm field}$ | Primordial spectral-flow parameter constrained by $n_s$ | TEP-TH | $0.01755$ (from $n_s=0.9649$) |
| $z_T^{\rm los}$ | C0 line-of-sight supernova transport turnover | TEP-C0 | $5$ (conservative), $100$ (benchmark), free (broad) |
| $z_T^{\rm HC}$ | Homogeneous/acoustic hi_class profile scale | TEP-HC | Fitted jointly with $\epsilon_T$ |
| $p$ | Temporal-horizon conformal exponent: $A_{\rm clock}\sim\eta^{-p}$ | TEP-TH | $0 \lt p\le\tfrac12$ (regular branch) |
| $r_s^{\rm TEP}/r_s^{\Lambda\rm CDM}$ | Pre-recombination sound-horizon ratio | TEP-HC | $0.999994$ ($<6$ ppm deviation) |
| $D=\alpha_K+\tfrac32\alpha_B^2$ | No-ghost discriminant ($D=(w_c+6)\alpha_A^2$; necessary but not sufficient for linear stability — the $w_c=-5$ branch is tachyonic; production $w_c=700$ gives $D=706\,\alpha_A^2$) | TEP-HC | $(w_c+6)\alpha_A^2\ge 0$ (non-negative; GR/decoupling limit at $\alpha_A=0$) |
| $r(k_{\rm pivot})$ | Native tensor-to-scalar ratio at Planck pivot | TEP-TH | $1.9\times10^{-9}$ |
| $r_{\rm max}$ | Maximum tensor-to-scalar ratio across transition profile | TEP-TH | $5.2\times10^{-7}$ (fiducial $p=0.1$); $6.1\times10^{-5}$ over all tested profiles $0\lt p\le1$ |
| $H_0$ | Hubble parameter (TEP-C0 joint MCMC) | TEP-C0 | $66.70\pm0.58$ km s$^{-1}$ Mpc$^{-1}$ |
| $S_8$ | $\sigma_8\sqrt{\Omega_m/0.3}$ (TEP-HC joint MCMC) | TEP-HC | $0.868\pm0.025$ |
| $\sigma_8^{\rm HC}$ | Native hi_class matter-fluctuation amplitude | TEP-HC | $0.824$ (fiducial); $0.858\pm0.016$ (MCMC posterior mean) |

**Note:** Parameters with superscript labels ($^{\rm los}$, $^{\rm HC}$) are related projections of the same temporal sector but are not numerically interchangeable. The turnover scales $z_T^{\rm los}$ and $z_T^{\rm HC}$ describe different physical regimes; the amplitudes $\epsilon_T^{\rm los}$, $\epsilon_T^{\rm CMB}$, $\epsilon_T^{\rm HC}$, and $\epsilon_{\rm field}$ are constrained by different observables.

# 14. Data Availability and Reproducibility

All data and analysis code required to reproduce the results presented in this work are available in the public repository at https://github.com/matthewsmawfield/TEP-TH.

All pipeline outputs, posterior samples, and the exact step configuration files are released in the Zenodo repository (DOI: 10.5281/zenodo.20723059) under CC-BY 4.0. The step scripts and `run_pipeline.py` orchestration script are provided in the GitHub repository.

## Repository Structure

- **scripts/steps/**: Python pipeline scripts for temporal-horizon analysis (steps 00-10, with 09b)

- **scripts/steps/th_common.py**: Shared utilities for TEP-TH pipeline

- **data/raw/**: Raw cosmological data sources

- **data/processed/**: Processed data products

- **results/**: Pipeline outputs (JSON, CSV, figures)

- **logs/**: Pipeline execution logs

## Pipeline Execution

The TEP-TH pipeline can be executed using the provided scripts:



```
cd scripts/steps
python step_00_temporal_horizon_mapping.py
python step_01_matter_frame_curvature.py
python step_02_geodesic_completeness.py
python step_03_effective_stress_energy.py
python step_04_full_bbn_abundances.py
python step_05_recombination_visibility.py
python step_06_cmb_blackbody_origin.py
python step_07_entropy_arrow.py
python step_08_primordial_perturbation_boundary.py
python step_09b_native_tensor_integration.py
python step_10_cmb_lss_class.py
```



## Key Pipeline Outputs

- **step_01_matter_frame_curvature.json / .csv**: Proposition 1 verification (pure conformal curvature vanishing) and disformal compensation analysis (critical power $n=4$, lapse divergence test)

- **step_04_full_bbn_abundances.json / .csv**: BBN abundance validation (Y_p, D/H, He3/H, Li7/H, N_eff)

- **step_05_recombination_visibility.json / .csv**: Recombination epoch ($z_*$, $r_s$, $\theta_s$), LCDM and TEP comparison

- **step_09b_native_tensor_integration.json / .csv**: Native tensor-mode integration (r(k_pivot), r_max, Bogoliubov coefficients)

- **step_10_cmb_lss_class.json / .csv**: CMB/LSS consistency scorecard (Planck comparison, sigma8)

## Dependencies

The pipeline requires Python 3.11+ with the following packages:

- numpy

- scipy

- matplotlib (for plotting)

- optional: `classy` (CLASS Python bindings) for the step_10 CMB/LSS spectra; without it the step degrades gracefully

- optional: bundled `external/alterbbn_wrapper.py` + AlterBBN for the step_04 abundance network; without it the step falls back to tabulated ΛCDM references

## Data Sources

The pipeline uses publicly available cosmological data:

- FIRAS CMB monopole spectrum (NASA LAMBDA)

- BBN abundance measurements (PDG 2024)

- Planck 2018 cosmological parameters

## Version Control

This work uses version v0.5 (Thika) of the TEP-TH pipeline, first published 18 June 2026. The repository maintains a complete history of all changes through Git version control.
