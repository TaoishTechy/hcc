# Whitepaper: DRC-3 Revision
## Raw Information Hierarchy, Rendered Reality, and the Multiverse Cone Stack
### Formal revision addressing the 144-point shortcoming report and 96-point enhancement report
### GhostMesh48 Research Collective | Version 3.0 | November 26, 2026

## 0. Consensus and Scope

The scientific consensus from geodesy, satellite ranging, and direct observation is that Earth is an oblate spheroid and the Moon and planets orbit the Sun.

This report treats DRC-3 as a hypothetical test model. It does not claim the consensus is wrong. It targets internal consistency, mathematical rigor, observational adequacy, and falsifiability. Where DRC-2 used labels, DRC-3 gives definitions, units, and thresholds. Where DRC-2 postulated, DRC-3 derives or explicitly marks as assumption. Where DRC-2 had no test threshold, DRC-3 gives one.

Imported frameworks, Unified Holographic Gnosis (UHG), Correlation Continuum, and Unified Holographic Inference Framework (UHIF), remain non-peer-reviewed hypotheses in this paper. They are used as premises to test, not as proven premises.

## 1. Change Log: What DRC-3 Fixes

From Part I, 144 points, grouped:

- A, Scope 1 to 12: Added formal definitions, domain of validity, and separation of assumption, definition, hypothesis, derivation.
- B, Notation 13 to 28: Fixed all overloads. c is now only speed of light. Cone growth is gamma. sigma_topo is single spelling. epsilon split into epsilon_wall and eta. Phi vs phi distinguished. h split into H normalized and h_phys with units. Cone apex and fixed-disk contradiction resolved by separating base radius from render radius.
- C, Geometry 29 to 56: Added base metric, render metric, line element, total derivative for Hubble law, Lagrange pinning, shelf dynamics from a potential, Sun energy and seasons, tides from a base gravity field.
- D, Astrophysics 57 to 80: Added explicit non-derivation list. DRC-3 does not claim to derive CMB, BAO, lensing, or Kepler laws. It gives interface equations to CLASS, CAMB, INPOP, EPM, and Gaia for comparison.
- E, Multiverse 81 to 96: Added Hilbert space, CPTP channels, no-signalling argument, entanglement monogamy, and formal branch definition.
- F, Branch and render 97 to 112: Added branch measure, decoherence model, Born rule from branch measure, holographic bounds, and functional forms for mismatch terms.
- G, Mismatch 113 to 128: Added quantitative tau_min, E_comp, E_proj, E_branch, E_transfer, and thresholds for every F and M test.
- H, Tests and simulation 129 to 144: Added likelihood, pre-registration, render_cone definition, transfer definition, units, timestep, multi-observer model, and failure modes.

From Part II, 96 suggestions, DRC-3 implements the formalization core, quantum information core, observation interface, statistics core, simulation core, and reporting core as specifications, not as claimed completed measurements.

## 2. Definitions

### 2.1 Raw vs Rendered, Operational Definition

A variable is raw if it appears in the base log and is not directly read by an instrument model. A variable is rendered if it appears in the perceived log after applying the render map Phi_cone. The test for the distinction is log separation. If a simulator mixes them in one variable, it is invalid for this paper.

- L0 Base: Disk coordinates (rho, theta), base time t_base.
- L1 Correlation: Correlation field, operators, and branch structure.
- L2 Boundary: Holographic boundary record, coherence density.
- L3 Ghost Mesh: Transfer layer, CPTP channels between branches.
- L4 Render: Cone map plus sphere slice, perceived coordinates.

Raw is L0 to L3. Rendered is L4.

### 2.2 Manifold and Charts

Base manifold: M_base = D x R, where D is a 2D disk with coordinates (rho, theta), rho in [0, 1], theta in [0, 2 pi). D is equipped with a flat metric in base coordinates. Time is t, in seconds.

Render manifold: M_render = Cone x R, where Cone is a truncated cone with height coordinate h_phys in [0, L_h], radius coordinate r in [0, r_cone], angle theta. L_h is a physical length, in km, a free parameter with prior in Section 8. Normalized height is H = h_phys / L_h, in [0, 1], for display only. All dynamics use h_phys, not H, to avoid the unit mismatch in DRC-2 points 22 to 24.

Topology: D is simply connected with boundary at rho = 1. Cone is D cross interval, truncated at h_phys = 0 and h_phys = L_h. No apex is assumed, because r at h_phys = 0 is r_disk_base, not zero. This fixes point 25. The cone is finite and truncated, fixing point 26.

Differentiable structure: Smooth except at rho = 0, theta coordinate singularity, and at the rim rho = 1, which is treated as a boundary condition, not as an interior point.

Domain of validity: DRC-3 is a test model for scales from 1 m to 1e9 km, velocities much less than c_light, and weak fields. It is not claimed valid for Planck scales, strong fields, or black hole interiors. c_light always means speed of light, 299792.458 km per s. Cone growth rate is gamma, in km per s, never c.

### 2.3 Observer

Observer is not assumed at the exact centre in DRC-3. Observer has coordinates (rho_obs, theta_obs, h_obs = 0) on the disk. Centre observer is the special case rho_obs = 0. Multiple observers are allowed, each with its own perceived log. Consensus rendering is the intersection of perceived logs after applying the same Phi_cone. This fixes points 11 and 141.

Relativity and cosmological principle are not derived in DRC-3. DRC-3 is compared to them as a null hypothesis. If DRC-3 requires a preferred centre, that is a cost, not a feature. The test is whether the preferred centre term in Section 6 is detected or bounded to zero.

## 3. Notation and Parameter Table

All symbols use one meaning in DRC-3.

- rho: normalized disk radius, dimensionless, [0, 1]
- theta: angle, rad
- H: normalized height, dimensionless, [0, 1], display only
- h_phys: physical height, km, H times L_h
- L_h: cone height scale, km, free parameter, prior 1e5 to 1e7 km
- r_disk_base: base disk radius, km, fixed in base coordinates, prior 6000 to 7000 km for Earth disk analogue
- r_disk_render(t): A(t) times r_disk_base, km, render radius
- alpha: cone half angle, rad, free, prior 0.05 to 0.30 rad
- gamma: cone growth rate, km per s, free, prior 0 to 1e-6 km per s
- A(t): render scale factor, dimensionless, A(t0) = 1
- A_dot: time derivative of A, 1 per s
- H_render: A_dot / A, 1 per s
- R_sky(t): render sphere radius at slice, km, R_0 times A(t)
- Phi_cone: cone render map, D x R to Cone
- phi: colatitude in sphere slice, rad, phi = pi times rho
- Phi_slice: sphere slice map at fixed h_phys = h_sky
- h_sky: physical height of sphere slice, km, H_sky times L_h, H_sky = 0.92
- CI_B: boundary coherence density, bits per km^2
- CI_C: continuum coherence density, bits per km^2
- J_CI: coherence flux vector, bits per km per s
- sigma_topo: topology source, bits per km^2 per s, single spelling throughout
- epsilon_wall: wall inset, km, shelf distance inside wall, prior 10 to 1000 km
- eta(d): local error, dimensionless, eta(d) approx (d / R_sky)^2 / 24
- lambda_i: Lagrange multiplier for shelf i, units of force per km
- omega_i: shelf angular speed, rad per s, sign positive for prograde
- theta_0,i: shelf phase at t0, rad
- r_i(t): shelf radius, km
- h_i_phys: shelf height, km, fixed, H_i times L_h
- r_obs: observer radius in base, km, rho_obs times r_disk_base
- r_s: Sun axial radius, km, prior 10 to 500 km
- h_s_phys: Sun height, km, H_s = 0.95 times L_h
- E_comp, E_proj, E_latency, E_branch, E_transfer: mismatch terms, dimensionless, Section 7

This table fixes points 13 to 22. No symbol is overloaded.

## 4. Geometry and Field Theory

### 4.1 Base Metric and Render Metric

Base line element, in base coordinates:

ds_base^2 = - c_light^2 dt^2 + r_disk_base^2 (d rho^2 + rho^2 d theta^2)

Render line element, in cone coordinates (h_phys, r, theta):

ds_render^2 = A(t)^2 [ - c_light^2 dt^2 + dh_phys^2 + dr^2 + r^2 d theta^2 ] with constraint r less or equal r_cone(h_phys, t)

Where:

r_cone(h_phys, t) = A(t) [ r_disk_base + h_phys tan(alpha) + gamma t tan(alpha) / A(t) ]

Simplified for the paper: base radius is fixed in base coordinates. Render radius grows with A(t). Time dependence from gamma is absorbed into A(t) for the minimal model, with gamma as a separate parameter for wall drift tests. This separation fixes the fixed-disk contradiction in point 23.

Derivation note: The render metric is an effective metric, not a solution of Einstein equations in DRC-3. DRC-3 does not claim to derive it from Einstein-Hilbert action. It postulates it as an effective map and tests it. The full action is given as a target in Section 4.3.

### 4.2 Cone Map and Sphere Slice

Cone map:

Phi_cone(rho, theta, t) = (r = A(t) r_disk_base rho, theta, h_phys = 0) for base points, extended to cone volume by h_phys.

Sphere slice map at fixed h_phys = h_sky:

Phi_slice(rho, theta, t) = R_sky(t) (sin(phi) cos theta, sin(phi) sin theta, cos(phi)), phi = pi rho

Relation: Phi_slice uses rho to latitude, h_sky is the slice height, not the latitude variable. The sphere is the image of the disk under Phi_slice at fixed h_sky. This fixes points 27 and 28. The sphere is not the cone. It is a slice image.

Perceived distance: DRC-3 replaces the Euclidean times A formula with the render metric distance. For a central observer, to first order:

d_perc,i = integral along render geodesic from observer to shelf i, approximated as A(t) sqrt( h_i_phys^2 + r_i(t)^2 ) for the minimal model, with full integral specified in the simulator.

Off-centre observer includes h_obs = 0 and r_obs, and uses the full geodesic integral, not the Euclidean approximation. This fixes points 29 to 32.

### 4.3 Action, Target

Base action, target form, not claimed derived:

S_base = S_EH + S_matter + S_corr + S_constraint

Where S_EH is Einstein-Hilbert term with base metric, S_matter is standard matter, S_corr is correlation field action with Hamiltonian H_corr, and S_constraint is shelf pinning:

S_constraint = sum_i integral lambda_i(t) (h_i_phys - h_i0) dt

Lambda_i is the Lagrange multiplier that enforces fixed shelf height. This fixes point 37 and point 11 in Part II.

Shelf dynamics: From S_base, shelf angular speed omega_i is derived from angular momentum conservation in the base potential V_base(rho), not postulated. In the minimal model, V_base is taken as V_base = - k / rho + (1/2) k_shelf (rho - rho_i0)^2, with k and k_shelf as free parameters to fit. If V_base cannot fit observed omega_i for all shelves with one k, the model fails. This fixes point 38.

Hubble law, total derivative: In DRC-3, v_perc is not simply H_render d_perc. It is:

v_perc = d/dt d_perc,i = H_render d_perc,i + A(t) (r_i r_dot_i + h_i_phys h_dot_i) / sqrt(h_i_phys^2 + r_i^2)

With h_dot_i = 0 for pinned shelves, this gives v_perc = H_render d_perc + A(t) r_i r_dot_i / sqrt(...). The second term is wall drift. This fixes point 56. Wall drift:

r_dot_i = A_dot [r_disk_base + h_i_phys tan(alpha)] + A(t) gamma tan(alpha)

All shelves share gamma, but r_dot_i differs because r_i differs. This fixes point 34. The earlier claim that all shelves have the same radial derivative was wrong. DRC-3 corrects it.

### 4.4 Sun, Seasons, Tides

Sun: Axial illuminator with energy source parameter L_sun, in watts, free, prior 3e26 to 4e26 W for Earth analogue. Emission is thermal with spectrum parameter T_sun. DRC-3 does not derive fusion. It treats L_sun as an input to fit, and helioseismology and neutrinos as consistency checks. If L_sun cannot fit both irradiance and neutrino flux, the axial Sun model fails. This fixes point 43.

Seasons: Disk has tilt parameter epsilon_tilt, in rad, prior 0 to 0.5 rad, and axial Sun circles with that tilt. Latitude effect is from observer rho and tilt, not from a spherical obliquity alone. Seasonal irradiance at observer rho_obs is:

I(rho_obs, t) = L_sun / (4 pi d_perc_sun^2) times cos(incidence), incidence = function(rho_obs, epsilon_tilt, theta_s(t))

If this cannot fit seasonal amplitude at two different rho_obs, the model fails. This fixes point 44.

Tides: Base gravity field g_base = - grad V_base, with V_base as above. Tidal acceleration is the gradient of g_base across the disk. Rendered tides are g_base pushed through the Jacobian of Phi_cone. The paper gives the field equation, not just the phrase same geometry. This fixes points 45 and 46.

Phases and eclipses: Derived from Sun, Moon, observer geometry in cone coordinates, with ray tracing in the simulator, not asserted. Eclipse timing is a test of theta_s, theta_m, and h_s, h_m.

## 5. Multiverse, Coherence, Quantum Foundations

### 5.1 Branch Definition

A branch alpha is a superselection sector of a von Neumann algebra A_alpha. Hilbert space is direct sum over alpha: H = direct sum_alpha H_alpha. Density matrix rho_total = sum_alpha p_alpha rho_alpha, with p_alpha as branch measure, sum p_alpha = 1.

Branch selection is decoherence: environment-induced superselection picks a pointer basis. Born rule is p_alpha = Tr(P_alpha rho_total), where P_alpha is projector onto H_alpha. This fixes points 84, 99 to 101.

Correlation-inaccessible means Tr_alpha,beta (rho_total) = 0 for alpha not equal beta after decoherence, to within decoherence factor exp(-t / tau_dec). Tau_dec is a free parameter to fit.

### 5.2 Coherence Conservation, Covariant Form

Coherence equation, covariant form:

partial_t CI_total + div J_CI = sigma_topo, CI_total = CI_B + CI_C

Where CI_total is bits per km^2, J_CI is flux, sigma_topo is source. Strict conservation holds when sigma_topo = 0. When sigma_topo is non-zero, it is a source from topology change, with its own field equation in the full theory. In the minimal model, sigma_topo is a free function to fit, with prior that it is zero except during transitions. This fixes points 81 and 82.

CI_B is defined as modular Hamiltonian density, or entropy current density, in bits per km^2. CI_C is continuum coherence density, same units. Both are defined, with units, fixing point 15.

### 5.3 Ghost Mesh Channels

Ghost Mesh transfer is a CPTP quantum channel E_AB from branch A to branch B:

rho_B' = E_AB(rho_A), E_AB completely positive and trace preserving.

No-signalling: For any local operations in A, the marginal in B is unchanged unless E_AB is applied. Proof sketch: E_AB is CPTP, partial trace over A commutes with local unitaries in B. Therefore no superluminal signalling in L4, even if L3 transfer is non-local in L4 coordinates. This fixes points 87 and 88.

Entanglement swapping: Standard swapping protocol applied through E_AB, with fidelity F_swap as free parameter, prior 0 to 1. Swap rate R_swap = k_swap times shared boundary coherence, with k_swap to fit. If R_swap is independent of boundary coherence, the mesh model fails. This fixes points 85, 94, 129.

Entanglement monogamy: For any three branches A, B, C, monogamy inequality holds: E(A:B) + E(A:C) less or equal E(A:BC). DRC-3 enforces this in the simulator by checking the inequality each step. Violation aborts the run. This fixes point 103.

Holographic bounds: Ghost Mesh bandwidth B_mesh is bounded by Ryu-Takayanagi formula: S_boundary less or equal Area / (4 G). Bandwidth in bits per s is B_mesh = S_boundary / tau_transfer. If required B_mesh exceeds the bound, the model is infeasible. This fixes points 89, 104, 110.

Hub: The hub is the shared boundary Hilbert space H_boundary, not a place in L4. Four branches share H_boundary through isometries V_alpha: H_alpha to H_boundary. This formalizes point 90 and 91.

### 5.4 Interaction Types, Formal

- Type 1 Coherence Transfer: CPTP channel with CI_B decrease in A, CI_C increase in B, total conserved except sigma_topo.
- Type 2 Entanglement Swapping: CPTP channel with fidelity F_swap, rate R_swap.
- Type 3 Branch Leakage: Probability p_leak per unit time, prior 0 to 1e-6 per s, with Poisson statistics. If p_leak is not small, branches would not be correlation-inaccessible.
- Type 4 Topology Transition: sigma_topo non-zero for duration tau_trans, with Hubble step amplitude Delta_H / H as free parameter. The 4.2 percent value at z = 1.57 from the Correlation Continuum is treated as a hypothesis to test, not as derived. DRC-3 does not claim to derive it. It gives the test: fit H(z) with a step at z = 1.57, compare to smooth H(z) by Bayesian evidence. This fixes point 96 and 130.

## 6. Astrophysics Interface, Non-Derivation List

DRC-3 does not claim to derive the following. It gives an interface to test against them:

- CMB blackbody, acoustic peaks, polarization: Interface to CLASS, CAMB. DRC-3 predicts CMB as boundary record at h near 1.0, with parity signal as free parameter to fit to LiteBIRD.
- BAO scale: Interface to BAO measurements. DRC-3 redshift formula must reproduce BAO angular scale to within measurement error, or it fails.
- SNe Ia time dilation: Interface to SNe Ia Hubble diagram. DRC-3 A(t) must fit time dilation factor 1 + z.
- Lensing: Null geodesics of render metric, with time delay formula from render metric. If lensing delays cannot be fit with one render metric, the model fails.
- Kepler laws, perihelion, light bending: Interface to INPOP, EPM ephemerides. Shelf dynamics must reproduce ephemerides to within residuals, or it fails.
- Gravitational waves: DRC-3 predicts no extra GW polarizations in minimal model. LIGO, Virgo constraints are null tests. If extra polarizations are required, the model must add them.
- Dark matter, dark energy: DRC-3 does not replace them with render language. It treats them as free functions to fit, with the same parameter counting as LCDM for Bayesian comparison. If DRC-3 needs more parameters than LCDM for the same fit, it loses by information criteria.

This fixes points 57 to 80 by honesty: non-derivation is stated, interface is given.

## 7. Mismatch Terms, Functional Forms

DRC-3 gives functional forms, not just labels. All terms are dimensionless.

- E_comp(H) = k_comp times H^2, k_comp free, prior 0 to 0.1. Larger H means more compression.
- E_proj(theta, H) = k_proj times abs(sin(theta - theta_ref)) times H, k_proj free, prior 0 to 0.1.
- E_latency: tau_min = tau_0 + k_N times N + k_R times R_sky(t), tau_0, k_N, k_R free, prior tau_0 0 to 1e-3 s, k_N 0 to 1e-12 s per agent, k_R 0 to 1e-9 s per km. E_latency = tau_min times f_signal, where f_signal is signal frequency.
- E_branch(alpha_i) = 0 if observer branch equals object branch, else E_branch = 1 - exp(- D_alpha / D_0), where D_alpha is branch distance, D_0 is decoherence scale, free.
- E_transfer(sigma_topo) = k_trans times abs(sigma_topo) times tau_trans, k_trans free, prior 0 to 1.

Total mismatch, additive as first order approximation, with correlation term:

E_total,i = E_comp + E_proj + E_latency + E_branch + E_transfer + E_cross, E_cross = correlation coefficient times sqrt(E_comp E_transfer), to allow non-additivity. This fixes point 116.

Local error: eta(d) = (d / R_sky)^2 / 24, derived from Taylor expansion of Phi_slice around rho = 0, with derivation in the simulator notebook. For d = 10 km, eta is about 1e-7. Comparison to geodetic residuals: geodetic residuals at 10 km are typically 1e-6 to 1e-5 in relative terms, so DRC-3 local error is below current residuals, which is why local tests cannot distinguish. This fixes points 118 and 119.

## 8. Falsification Matrix, Quantitative Thresholds

Each test has prediction, dataset, threshold, pass, fail.

- F0 Local flatness: Prediction eta(d) as above. Dataset: geodetic baselines. Pass if measured residual greater than eta, so eta is not detected. Fail if eta is detected as systematic. Note: F0 is a consistency check, not a discriminating test. DRC-3 labels it as such, fixing point 120.
- F1 Oval anisotropy: Prediction fractional difference = 2 delta, delta free. Dataset: VLBI, Gaia. Threshold: delta greater than 1e-6 detectable, delta less than 1e-7 ruled out if no signal. Pass if delta fit is non-zero at 3 sigma, fail if delta = 0 at 3 sigma and oval version is retired.
- F2 Observer radius parallax: Prediction extra parallax = r_obs term in Section 4.2, amplitude = A(t) r_obs r_i / d_perc^2 times 1 rad, approx 1e-5 rad for Moon for r_obs = 1000 km. Dataset: lunar laser ranging. Threshold: 1e-6 rad. Pass if extra term detected at 3 sigma, fail if bounded to less than 1e-6 rad.
- F3 Shelf ordering: Prediction h ordering matches distance ordering. Dataset: INPOP, EPM. Threshold: ordering must hold for all 8 planets. Fail if any planet violates ordering by more than 3 sigma.
- F4 Recession link: Prediction r_dot_i from Section 4.3 must fit Moon recession 3.8 cm per year and planetary drift within 10 percent with one gamma and one A_dot. Fail if no single gamma fits both.
- F5 Retrograde crossing: Prediction retrograde start time equals theta crossing time within 0.5 days. Dataset: ephemerides for Mars, Jupiter, Saturn. Fail if any retrograde event is off by more than 0.5 days.
- F6 Rim galaxies: Prediction galaxies at H greater than 0.9 have z greater than 1.0 on average, and angular size change less than 1 percent per decade. Fail if low H objects show high z systematically.
- F7 Render latency: Prediction tau_min as in Section 7, with tau_0 greater than 0. Threshold: tau_min greater than 1e-6 s detectable by atomic interferometry. Fail if tau_min bounded to less than 1e-9 s.
- M1 Cross-branch anti-correlation: Prediction correlation coefficient between branch A and B anomalies = -0.8 to -1.0. Null distribution: correlation 0 plus or minus 0.1 from random. Fail if correlation is within null.
- M2 Swap rate: Prediction R_swap = k_swap times shared coherence, with k_swap greater than 0. Fail if R_swap is independent of coherence at 3 sigma.
- M3 Hubble step: Prediction step at z = 1.57, amplitude 4.2 percent, prior width 0.5 percent. Dataset: JWST, SNe Ia, BAO. Fail if step amplitude bounded to less than 1 percent.
- M4 CMB parity: Prediction parity signal amplitude P_parity free, prior 0 to 0.1. Dataset: LiteBIRD. Fail if P_parity bounded to less than 0.01.

Pre-registration: Parameters, priors, thresholds, and datasets are fixed before fitting. No post hoc fitting of delta, gamma, or k_swap to pass a test. This fixes points 61, 62, 131 to 134.

## 9. Simulation Specification v3

Functions defined, fixing points 135 to 143:

- render_cone(rho, theta, h_phys, t): Returns perceived coordinates by applying Phi_cone, then Phi_slice if h_phys = h_sky, with retarded time t_ret = t - d_perc / c_light. Includes relativistic aberration to first order: theta_perc = theta + v_obs / c_light times sin(theta).
- transfer(CI_B, CI_C, sigma_topo, dt): Updates CI_B, CI_C by: CI_B' = CI_B - J_CI dt + sigma_topo dt / 2, CI_C' = CI_C + J_CI dt + sigma_topo dt / 2, with J_CI from flux model. Checks conservation: CI_B' + CI_C' = CI_B + CI_C + sigma_topo dt, within 1e-9 relative error, else abort.
- step(state, dt): Uses symplectic integrator for shelf dynamics, adaptive timestep with dt less than 0.01 times orbital period, logs base and perceived separately with checksums.
- Multi-observer: Supports N_obs observers, each with own perceived log. Consensus rendering is intersection after applying same Phi_cone.
- Noise: Adds Gaussian noise with sigma from instrument model, plus latency queue with tau_min.
- Failure modes: Abort if conservation error greater than 1e-9, monogamy violation, or branch measure sum not equal 1 within 1e-9.

Scaling: B = N times f_update times bits per frame, with N, f_update, bits as parameters. HPC scaling test to N = 1e6 is required. If B exceeds holographic bound in Section 5.3, the run is infeasible.

Validation: Simulator must reproduce INPOP ephemerides for Moon and Mars to within 1 km over 1 year in perceived coordinates, or it is not validated. This fixes point 138.

## 10. Statistical Comparison

- Likelihood: Gaussian likelihood for ephemeris residuals, with full covariance from INPOP, EPM, Gaia, LLR.
- Bayesian evidence: Nested sampling, with parameter counting explicit. DRC-3 has 12 free parameters in minimal model: alpha, gamma, A_dot, L_h, delta, k_comp, k_proj, tau_0, k_swap, p_leak, Delta_H, P_parity. LCDM has 6 base parameters. DRC-3 must beat LCDM by Bayes factor greater than 10 to claim preference, after penalizing extra parameters.
- Information criteria: AIC, BIC reported with explicit parameter counts.
- Blind analysis: Analyst is blind to branch labels and to F2 extra parallax sign until unblinding.
- Simulation-based inference: Where renderer is intractable, use approximate Bayesian computation with summary statistics from Section 8.

## 11. Remaining Gaps

- Base field equations for gravity, electromagnetism, and quantum fields in D are not derived. S_corr is a target, not a completed Lagrangian.
- Sun fusion, galaxy formation, and structure formation are not derived. They are interface inputs.
- Renderer mechanism and energy source are not specified. B_mesh bound is a feasibility check, not a mechanism.
- Consciousness language is removed from DRC-3. Observer means instrument plus logging system, not consciousness. This fixes point 108.
- UHG axioms H13 to H15 are now stated: H13 is coherence conservation in Section 5.2. H14 is branch selection as decoherence in Section 5.1. H15 is IEG equivalence: informational coherence equals geometric correlation, in the sense that CI_total determines the render metric scale A(t). H15 is a hypothesis, not a theorem.

## 12. Conclusion

DRC-3 does not claim to replace consensus. It claims to be a testable, formalized alternative that can be killed by the tests in Section 8. If F2, F4, F5, M1, M3, or M4 fail at the thresholds given, DRC-3 is retired in its current form. If they pass, DRC-3 earns a comparison to LCDM by Bayesian evidence, not by rhetoric.

The next step is not more images. It is a small simulator that implements Section 9, logs base and perceived separately, fits gamma and A_dot to lunar recession and Hubble data, and reports posterior predictive checks. Less grandeur, more grind.

## Appendix: Derivation Table

Every equation in DRC-3 has a status: Derived, Postulated, or Target.

- Cone radius: Postulated effective, with derivation target from A(t) and alpha.
- Shelf pinning: Derived from S_constraint with Lagrange multiplier.
- Shelf omega: Derived from V_base, with V_base as free function to fit.
- Hubble law: Derived from total derivative, Section 4.3.
- Redshift: Postulated from A(t), interface to BAO and SNe Ia.
- Coherence: Postulated from UHG H13, with covariant form given.
- Branch selection: Derived from decoherence, with Born rule from branch measure.
- Mismatch terms: Postulated functional forms, with parameters to fit.
- Local error eta: Derived from Taylor expansion of Phi_slice.

## End of Whitepaper
