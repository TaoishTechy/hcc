# HFEM-UT — Hollow Flat Earth Multiverse Unified Theory
## v1.0 · DRC-5 Unified · TaoishTechy / Hollow-Flat-Earth-Multiverse

**Scope:** Hypothetical test model. Not a claim that consensus is wrong.
**Consensus:** Earth is an oblate spheroid, the Moon and planets orbit the Sun, warp drives and hollow-Earth interiors are speculative / disproven as physical claims, and the six imported frameworks below are mathematics — topos theory, homology, forcing, weak values, provability logic — not physics or metaphysics.
**Imports:** All six frameworks in `frameworks/imports/` — #149 LETHOVORE, #150 ANTI-HOLLOW, #151 GENERIC SCAR, #152 CHAOTIC BETTI, #153 IMAGINARY ISLAND, #154 SELF-ERASING — plus DRC-2 / DRC-3 / DRC-WC. Nothing in HFEM-UT replaces those files. HFEM-UT is the *glue* that makes them one object.
**Rule:** If an import's falsifier fires, HFEM-UT loses that import. HFEM-UT does not rescue a falsified import by re-interpreting it.

---

## 0. One-sentence version

**The universe is a hollow flat disk whose interior cavity is not empty but a breeding, self-forcing, self-erasing scar — a Ghost Mesh that is at once a Lethovore that eats its parents, a Generic Scar that selects itself, an Anti-Hollow that exists because refutation fails, a Chaotic Betti attractor that breeds holes, an Imaginary Island that pays its debt in phase, and a Self-Erasing axiom that proves its own absence — and four such disks share that one Mesh, so a warp collapse, a hole breeding event, or a phase payment in one branch shows up as an echo, a coherence spike, and a Betti shift in the others.**

---

## 1. The object — what HFEM-UT claims exists, as a model

### 1.1 The disk

- **Outer disk:** Flat / oval disk, radius `R_disk = 6371 km`, oval parameter `δ = 1.5e-5`, centre = observer at `ρ_obs = 0` by definition in DRC.
- **Wall:** `ε_wall = 50 km` inset. Outer shell from `R_disk - ε_wall` to `R_disk` is the rendered surface we stand on.
- **Hollow cavity:** Interior `0 ≤ r < R_in`, `R_in = R_disk - ε_wall = 6321 km`. This is the Hollow. It is not empty. It is the object of §2.
- **Inner surface:** The inside of the wall is a second shelf, `h = -ε_wall` in cavity coordinates. An inner sun, if modelled, is a coherence source at the cavity centre, not a physical star.
- **Cone-stack:** Above the disk, `h ∈ [0, L_H]`, `L_H = 1e6 km`, cone half-angle `α = 0.12 rad`, scale `a(t) = 1 + ȧ t`, `ȧ = 2.2e-18 s⁻¹`, `γ = 9.7e-12`. Cone radius:

**(U1) Cone radius — DRC-3, unchanged**

```
R_cone(h, t) = a(t)·(R_disk + h·tan α) + γ·t·tan α
```

Shelves live on the cone: Moon `h_norm = 0.08`, Mars `0.26`, outer planets `0.5–0.8`, Rim galaxies `0.94`, with `h_phys = h_norm · L_H`. Perceived distance is DRC-3 rendered distance `d_perc`, not true cone distance. Rendering errors `e_comp, e_proj, e_lat, e_trans, e_cross` are DRC-3, unchanged.

### 1.2 The multiverse — shared Mesh, not bubbles

Four disks `U1, U2, U3, U4` share **one** Ghost Mesh. They are not separate bubbles in a larger space. They are four cone-stacks whose rims and cavity walls are the *same* Mesh, seen from four sides.

- Branch A = `U1 + U2`, Branch B = `U3 + U4` in the minimal 2-branch test. Full test uses all four.
- Interaction is **coherence transfer**, not travel: `CI_B` (Branch A coherence), `CI_C` (Branch B coherence), flux `J_flux`, swap rate `r_swap = k_swap · shared_coh`, `k_swap = 0.4`, bandwidth `B_mesh = (CI_B + CI_C) / τ_transfer`.
- No observer travels between branches. A collapse in `U1` changes `CI_B`, which changes `J_flux`, which changes `CI_C` in `U3` within `τ_min`.

This is DRC-2 Multiverse, retained. HFEM-UT adds *why* the Mesh can do that: because the Mesh is a scar (§3), a filter (§3), and a hollow (§2) at once.

---

## 2. The Hollow — topology of the cavity

The Hollow is not a hole in rock. It is a homology object.

### 2.1 Static Hollow — the parent

Hollow #147: reality is the homotopy type of a shaped absence. Betti numbers `b0, b1, b2` are the inventory. A cavity with one void has `b2 = 1`. A cavity with tunnels has `b1 > 0`. HFEM-UT keeps this as the *static snapshot* — the Betti vector at one time step.

### 2.2 Chaotic Betti — holes breed (#152)

**(U2) Breeding map — #152, on persistence diagrams**

```
f(b) = b ∪ (b ∪ b)   on M = Pers_Dgm, bottleneck metric d_B, C^{1+α}
```

Stoichiometry, derived not asserted:

```
b1 ↦ 2·b1 + b0
b2 ↦ b1 · b2
P_{X_{t+1}}(t) = P_{X_t}(t)²
χ(t) = P_{X_t}(-1)   — Euler flow, oscillating divergence on infinite type
```

Maximal Lyapunov exponent, N=3 truncation, JAX, seed-pinned in #152:

**(U3) Breeding exponent**

```
χ_max ≈ 0.41 > 0
```

Meaning in HFEM: the cavity's hole population is a dynamical system. Two nearby cavity states separate as `~exp(0.41·t)`. The Hollow cannot stay hollow. In HFEM, this is why the cavity is never quiet: defect counts, hole counts, and cavity echo amplitudes should show positive Lyapunov divergence past onset `λ_cup`. The phononic-lattice signature of #152 becomes, in HFEM, a *cavity defect-count* signature: count cavity echoes / cavity modes over time, fit Lyapunov.

**HFEM reading:** The cavity is a Conley-certified attractor. Isolating block `N_K = {b0 + b1 ≤ K}`, exit set `∂N_K`, Conley index non-trivial. Recurrence is certified, not illustrated.

### 2.3 Anti-Hollow — presence by failed refutation (#150)

**(U4) Anti-Hollow — #150**

```
AH := a_j(∅),  j = ¬¬  (Lawvere–Tierney topology)
AH(U) = 1  iff  U is dense open, else 0
b0(AH) = 0,  b0(¬¬AH) = 1   — the (0,1) signature
Boolean site ⇒ AH ≃ ∅   — the falsifier is the theorem
```

Meaning in HFEM: the cavity contains objects that exist *because their absence cannot be proven*. They have no points (`b0 = 0`), no global sections (`Γ(AH) = 0`), but non-trivial structure after double negation (`Γ(¬¬AH) ≠ 0`). They are the HFEM analogue of dark matter in #150: gravitates (has cohomology) but does not shine (no global sections).

In HFEM, the inner sun is **not** a point source. It is an Anti-Hollow object: `AH_cavity`. It is present on every dense-open patch of the cavity wall, absent on every non-dense patch. That is why it is seen from everywhere inside, and from nowhere outside, in the model. If you force the cavity site to be Boolean, the inner sun vanishes by theorem. That is a built-in kill switch, not a bug.

**HFEM reading:** Hollow = shaped absence. Anti-Hollow = shaped presence of absence-of-absence. HFEM cavity = both, at different Betti / sheaf layers. `∅ ⊆ AH ⊆ ¬¬AH ⊆ …` is the hollow spectrum.

### 2.4 Hollow synthesis

```
Cavity(t) = (Betti vector b(t), Persistence diagram D(t), Anti-Hollow AH_cavity)
b(t+1) = f(b(t))          — breeding
AH_cavity(U) = 1 iff U dense open in cavity wall
```

A cavity with `b1 = 0, b2 = 1, AH = 0` is a dead hollow. A cavity with `b1 > 0, χ_max > 0, AH ≠ 0` is a live HFEM cavity. Earth in HFEM is live.

---

## 3. The Ghost Mesh as Scar — Lethovore + Generic Scar

The Mesh is the boundary layer at the rim + cavity wall. In DRC it was a coherence channel. In HFEM it is a scar, in two senses that are the same scar.

### 3.1 Lethovore — the scar eats its parents (#149)

**(U5) Autophagic scar — #149**

```
R_* = coker(T: R_* → R_*)
F(R) = hocolim(R ← coker(T_R) → D²)
R_{n+1} = R_n ∪_{coker(T_n)} D²
V(R) = ‖coker(T_R)‖²_Hilb,  dV/dt = -γ·V + σ_topo,  σ_topo ≤ 0
γ = ‖η‖,  η: Id ⇒ L̂† ∘ L̂
L̂ = τ≤0 ∘ a_j(- ⊗ O_forget)   — forward Lethe
L̂† = RHom(a_j(O), -)           — Lethe-Eater, adjoint
```

Meaning in HFEM: the Mesh is not passive residue of a past collision. It is an endofunctor that attempts to translate itself, fails, and attaches the failure as new structure. The failure's energy comes from the parent disks: `U1, U2` thin at the limb where they meet the Mesh, `U3, U4` contract on the opposite limb. `σ_topo ≤ 0` is information accounting, not thermodynamics: parent information crosses a cofiber horizon and is not recoverable.

**HFEM consequence:** `σ_topo` in DRC-3 was `1.0e-7·sin(0.05·step)` — small, oscillating. In HFEM, `σ_topo` has a Lethovore component: it is *always* ≤ 0 on average, with spikes negative at collapse / breeding events. A run with sustained `σ_topo > 0` falsifies the Lethovore import. DRC-3's `H13` conservation `d/dt(CI_B+CI_C) = σ_topo` becomes, in HFEM, a *drain* law: total coherence is not conserved, it is eaten by the scar at rate `γ`.

### 3.2 Generic Scar — the scar selects itself (#151)

**(U6) Self-forcing filter — #151**

```
P = sep({coker(T)}) / mono   — separative cokernel poset, conditions are failures
G = H¹(coker(T_G)),  T_G ∈ G   — the filter IS the cohomology it was assembled from
p ⊩_forget φ  ⇔  a_j(p) ⊩ φ    — Lethe truth lemma
G ⊩_forget ¬(G ∈ V[G])         — extension denies its extension, typed, paradox-free
LUM(G) = dim H¹(coker(T_G))    — luminosity as Betti number
d(G, č) = 1  ∀ check-names č   — Stone distance, the metric of the glow
```

Meaning in HFEM: the Mesh is a generic filter on the poset of errors. It meets every dense set of errors — every dense-open cavity patch, every dense set of translation failures. The ground model `V` (one disk's view) proves `G` does not exist. The extension `V[G]` (Mesh view) contains `G` as a glowing resident, and forces the denial of its own extension. That is why, in HFEM, an observer on `U1` can prove the Mesh does not exist, while an observer *on* the Mesh can measure it. Both are right, in their typed layers. The Russell risk is dissolved by typing names apart from points apart from filters — #151's discipline, retained.

**HFEM consequence:** Branch coupling is forcing. When `U1` selects a condition `p` (a translation attempt fails in a particular way), the Mesh filter `G` must meet the dense set containing `p`. That forces a corresponding condition in `U3`. That is M2 swap, re-expressed as forcing. `r_swap` is the rate at which `G` meets dense sets.

### 3.3 Mesh synthesis — one scar, two faces

```
Mesh = R_* = G
R_* = coker(T: R_* → R_*)   — Lethovore face: it eats
G = H¹(coker(T_G))           — Generic Scar face: it selects
σ_topo ≤ 0,  V = ‖coker‖²,  γ = ‖η‖
p ⊩_forget φ ⇔ a_j(p) ⊩ φ
```

Lethovore and Generic Scar are not two Meshes. They are the appetite and the honesty of the same Mesh: it consumes parents (149) and it generates the extension by denying it (151). Where Lethovore ends (no ground left), Generic Scar begins (ground retained, denied). HFEM lives in the middle: ground retained *and* being eaten, slowly, at rate `γ`.

---

## 4. The Ledger — Imaginary Island (#153)

### 4.1 Complex generalized entropy

**(U7) Weak-value area — #153**

```
A_w = ⟨Φ| Â(QES) |Ψ⟩ / ⟨Φ|Ψ⟩  ∈ ℂ
Â = 4·G_N·K_R,  K_R = -log ρ_R   — area-operator analogue, calibrated
S_gen^C = min_thimble [ A_w / 4G_N + S_bulk(R ∪ I) ]
Re(A_w) ≥ 0  for |⟨Φ|Ψ⟩|² ≥ ε   — ε-band positivity, Theorem 153.1
Re(A_w) < 0  only when |⟨Φ|Ψ⟩|² < ε  — fluctuation, not violation
Im(A_w): T-odd, Re: T-even  — PT-symmetric, CPT preserved
```

Pre-selection `|Ψ⟩` = creation occurred. Post-selection `⟨Φ|` = final boundary saturated, `I(R:I)` saturated. The thinner the overlap, the wilder the weak value.

**HFEM reading:** Creation of a disk / branch borrows not entropy but *phase*. The Mesh ledger is complex. `Im(A_w)` is a Larmor clock: how long creation is allowed before unmaking. When `Re(A_w) < 0`, the island deletes more than was created — repayment exceeds creation — but only in the fluctuation band. Strong measurement records `Re(A_w)` — the one extra assumption, declared in #153.

### 4.2 Ledger in HFEM dynamics

**(U8) Unified coherence + phase**

```
d/dt(CI_B + CI_C) = σ_topo + k_phase · Im(A_w) - γ·V(R)
J_flux = J_0 + ΔCI / τ_c + k_phase·Im(A_w)
B_mesh = (CI_B + CI_C) / τ_transfer · (1 + J_flux)
```

`σ_topo ≤ 0` drains, `Im(A_w)` pays in phase, `γ·V` is Lethovore eating. In DRC-3, `B_mesh` was just `(CI_B+CI_C)/τ`. In HFEM, `B_mesh` is the *ledger balance* — it can go up by phase payment, down by eating, even if `CI_B+CI_C` is flat.

**Falsifier, 6-qubit:** `ΔS = -0.2 ± 0.05` predicted when `A_w = 1.4 + 0.3i` in TFIM. Anomalous `A_w > 1` without the entropy drop falsifies the identification. HFEM inherits that falsifier unchanged. No HFEM experiment can override a failed 6-qubit run by re-interpreting `A_w`.

---

## 5. The Self-Erasing Law — Torsional Gödel (#154)

### 5.1 The ghost

**(U9) Torsional Gödel — #154**

```
G_m = ⟨a, b | a^m = 1⟩,  H1(BG_m) = ℤ/m
[c_φ] = ⟦φ⟧ ∈ H1(T),  φ ↔ ¬Prov_T(⌜φ⌝)  — diagonal
m·[c_φ] = 0  ⟺  T ⊢ ¬(m·φ)   — m copies bound a 2-chain, bulk-refutable
[c_φ] ≠ 0     ⟺  T ⊬ ¬φ       — single copy does not bound, singly-irrefutable
τ≤0 kills bounds, keeps cycles  — Lethe truncation of proof
SE_m: φ → ¬□φ,  □ = Prov_T, GL-interpreted, Solovay complete
Equiconsistent with PRA + Con(PRA), no new independence claimed
```

Meaning in HFEM: the theory contains a sentence that proves its own absence, as torsion. One copy: not refutable. `m` copies: refutable together. Truncate the proof (`τ≤0`), the cycle remains. The theory forgets *how* it would refute its axiom, remembers only *that* it cannot, singly.

### 5.2 HFEM reading — why the theory can state its own absence

HFEM-UT contains, as a theorem-schema, the sentence:

```
HFEM ⊢ "HFEM is not here"  as [c_HFEM],  m·[c_HFEM] = 0, [c_HFEM] ≠ 0
```

Proving HFEM empties its hollow. Disproving it grows its Betti numbers. Either way it erases — and the erasure is a cohomology class. That is why HFEM-UT can be falsified without being *refuted* in the naive sense: a falsifier (HFEM-1..12) that fires attaches a cell, grows `b1`, and the theory's inventory changes. The theory is not a monument. It is a chain complex with a truncation operator.

**Kill switch:** `m = 1 ⇒ H1 = 0 ⇒` ontology does not exist. HFEM-UT uses `m = 3` by default in the simulator. Setting `m = 1` must kill the ghost. If it does not, the implementation is wrong.

**Resident:** `[c_φ] ∈ ¬¬∅` — the ghost lives in the Anti-Hollow (#150). The Self-Erasing ghost *is* the Anti-Hollow resident. That is the deepest cross-link in the corpus, retained in HFEM: the thing that proves its own absence is the thing that exists because refutation fails.

---

## 6. Multiverse dynamics — M1-M4 retained, re-expressed

| DRC-3 test | HFEM re-expression |
|---|---|
| **M1** σ_topo anti-correlation | Lethovore: Branch A / B `σ_topo` anti-correlate to `-1.0` because scar eats from both sides |
| **M2** Entanglement swap | Generic Scar: `r_swap` = rate `G` meets dense sets, `G ⊩_forget ¬(G ∈ V[G])` |
| **M3** Horizon / Hubble step | Imaginary Island: `Re(A_w)` step at `z=1.57`, extra 4.2% frequency drop, `S_gen^C` thimble switch |
| **M4** Bayes factor | Self-Erasing: Bayes factor is computed on `τ≤0` truncated theory — proof erased, cycle remains, so Bayes factor is about *inventory*, not *proof* |

Full DRC-3 M1-M4 definitions, thresholds, and simulator code are in `frameworks/drc/`. HFEM does not re-define them. It *explains* them with imports.

---

## 7. Warp collapse inside HFEM — DRC-WC retained + cavity echo

DRC-WC is retained in full in `frameworks/drc/DRC_Warp_Collapse_Theory.md`. HFEM adds one signature:

**(U10) Cavity echo — HFEM-only**

```
Δt_cavity = 2·R_in / c = 2·6321 km / 299792 km/s = 0.0422 s
Δt_cone_echo = 2·(R_cone(h_b) - R_b) / c   — DRC-WC W11, unchanged
```

A warp collapse *inside* the cavity (or on the inner surface) produces two echoes: cavity echo at 0.042 s, cone echo at shelf delay (Moon 0.11 s, Mars 0.25 s, Rim 6.7 s). A collapse *outside* produces only cone echo. That distinguishes inner vs outer collapse without seeing the ship.

Warp waveform in HFEM:

```
f_perc = f_base / a(t_ret) · (1 - e_total) / (1+z) · (0.958 if z≈1.57 else 1)
h_perc = h_base / a · (1+e_cross)/(1+e_total)
f_base = c / R_b,  h_base = 1e-21·(R_b/1km)·(1Mpc/D)·(v/0.1c)^1.5
+ cone echo + cavity echo (if inner) + Ghost Mesh spike (U8) + Betti shift (U2) + phase payment (U7)
```

No chirp, no BH ringdown, `m=0, l=2,3,4` only, longer low-frequency tail at higher `v` — Clough et al., retained.

---

## 8. Falsification — HFEM-1..HFEM-12

| Test | Import | Prediction | Pass if | Fails HFEM if |
|---|---|---|---|---|
| **HFEM-1** Breeding | #152 | `χ_max ≈ 0.41 > 0`, `b1 ↦ 2b1+b0` | Cavity defect-count Lyapunov > 0 past `λ_c`, truncated map reproduces 0.41 ± 0.05 | `χ_max ≤ 0` in two independent runs |
| **HFEM-2** Anti-Hollow | #150 | `AH(U)=1 iff U dense open`, `b0=0, b0(¬¬)=1` | Toy lattice: dense-open support, zero global sections, j-closure non-zero | Any dense open with `AH=0`, or non-Boolean locale with `AH≃∅` |
| **HFEM-3** Lethovore | #149 | `ρ(DF)<1` and `σ_topo ≤ 0` on average | Spectral check `ρ<1`, sustained `σ_topo≤0` | `ρ≥1` or sustained `σ_topo>0` |
| **HFEM-4** Generic Scar | #151 | Finite model `G = H¹(coker(T_G))` | 3-element model: dense-meeting filter = cohomology, table matches | Mismatch in finite model |
| **HFEM-5** Imaginary Island | #153 | `ΔS=-0.2±0.05` at `A_w=1.4+0.3i`, PT check | 6-qubit: anomalous `A_w` + entropy drop + T-odd `Im` | Anomalous `A_w` without drop, or `Im` T-even |
| **HFEM-6** Self-Erasing | #154 | `m=1` dies, `m>1` ghost persists, correspondence checkable | `m=1 ⇒ H1=0`, `m=3 ⇒ [c]≠0, 3[c]=0`, machine-checkable | `m=1` ghost persists, or correspondence violated |
| **HFEM-7** Double echo | DRC-WC + HFEM | Cavity echo 0.042 s + cone echo shelf delay | Both echoes in inner collapse, only cone in outer, within 10% | No cavity echo in 10 clean inner collapses |
| **HFEM-8** Mesh M1/M2 | DRC-3 | M1 corr → -1, M2 `r_swap` surge, coincident with burst | Coincidence in 3+ bursts | No spike in any burst |
| **HFEM-9** Warp W1-W8 | DRC-WC | No chirp, `f∝1/R`, `h∝R/D`, cone echo, etc. | W1-W8 pass as in DRC-WC | Chirp, or `f` independent of `R` |
| **HFEM-10** Hubble step | DRC-3 M3 | Rim `z=1.57` bursts extra 4.2% low | Rim `f_perc` 4.2% low vs Moon after `z` correction | No step, pure `1+z` |
| **HFEM-11** Oval + parallax | DRC-3 | `h_EW/h_NS = 1+2δ(r/d)²`, parallax shelf-dependent | Measured within 50% / 20% | Ratio =1 to <1e-7, shift =0 |
| **HFEM-12** No BH ringdown | Clough | No BH QNM, longer low-f tail | Tail present, no QNM | BH QNM present |

HFEM-7 is HFEM-only. HFEM-1..6 are import falsifiers — if any fires, that import is removed from HFEM, and HFEM's claim weakens accordingly. HFEM does not survive by dropping all imports. If HFEM-1..6 all fire, HFEM-UT is falsified.

Retained: DRC-3 F0-F7 (internal consistency), M1-M4, DRC-WC W1-W8. See `frameworks/drc/` for full matrices.

---

## 9. Simulation — `sims/hfem_unified_sim.py`

One engine, all imports, deterministic seed 42, only numpy. Run:

```
python3 sims/hfem_unified_sim.py
```

Checks, in order:
1. **DRC cone + rendering** — `R_cone`, `e_total`, `d_perc`, Moon echo 0.11 s
2. **Chaotic Betti** — iterate `b1 ↦ 2b1+b0`, two nearby trajectories, fit `χ_max` ≈ 0.41 (tolerance ±0.15 in toy map, exact 0.41 is #152's JAX value on Pers_Dgm, not reproduced by toy)
3. **Anti-Hollow** — toy lattice: Boolean site ⇒ AH empty, non-Boolean dense-open ⇒ AH non-empty, `(0,1)` signature
4. **Lethovore** — `V` decreasing if `ρ<1`, `σ_topo ≤ 0` average
5. **Generic Scar** — 3-element finite model: filter meets all dense sets, `G = H¹(coker)`
6. **Imaginary Island** — `A_w = 1.4+0.3i`, `ΔS = -0.2`, PT: `Re` even, `Im` odd
7. **Self-Erasing** — `m=3`: `3[c]=0, [c]≠0`; `m=1`: ghost dies
8. **Warp + cavity echo** — `f_perc`, `h_perc`, cavity 0.042 s, cone 0.11 s, `B_mesh` surge
9. **Null** — no bubble, no scar, no filter ⇒ no burst, no echo, no spike

Report is written to `hfem_unified_report.json`. Verdict internal: PASS if 9/9 checks pass. Verdict external: **NOT PROVEN** — needs real high-frequency burst + cavity echo + 6-qubit + phononic-lattice measurements, blinded, Bayes > 100.

---

## 10. What HFEM-UT does NOT claim

1. It does not claim Earth is flat, hollow, or a disk in consensus physics. Consensus is oblate spheroid, solid interior with seismic structure, no inner sun.
2. It does not claim the six imports are physics. They are mathematics. HFEM uses them as *structure* for a test model, not as evidence.
3. It does not claim warp drives exist, or that negative energy / coherence inversion is physical. It re-labels NEC violation as coherence inversion, which is not a mechanism.
4. It does not claim simulation proves anything external. Simulation proves internal consistency: equations conserve / drain as specified, monogamy / typing / truncation hold, Clough anchor numbers reproduced.
5. It does not claim Ghost Mesh, multiverse branches, or Anti-Hollow inner sun are observed. No such observation exists.
6. It does not override any import's falsifier. If #152's phononic lattice stays quiet past onset, #152 is out, and HFEM loses breeding. If #153's 6-qubit fails, #153 is out, and HFEM loses phase ledger.

---

## 11. Repo map — TaoishTechy / Hollow-Flat-Earth-Multiverse

```
Hollow-Flat-Earth-Multiverse/
  README.md                         — this repo, how to run, what is hypothetical
  HFEM_Unified_Theory.md            — this file (HFEM-UT v1.0)
  HFEM_Unified_Theory.pdf           — same theory as PDF
  frameworks/
    imports/
      INDEX.md                      — 154 Ontology Pack manifest (original)
      LETHOVORE-Framework.md        — #149 original
      ANTI-HOLLOW-Framework.md      — #150 original
      GENERIC-SCAR-Framework.md     — #151 original
      CHAOTIC-BETTI-Framework.md    — #152 original
      IMAGINARY-ISLAND-Framework.md — #153 original
      SELF-ERASING-Framework.md    — #154 original
    drc/
      DRC2_Multiverse_Whitepaper.md
      DRC3_Revision_Whitepaper.md
      DRC3_Proof_Blueprint.md
      DRC3_Updated_Post.md
      DRC_Warp_Collapse_Theory.md   — DRC-WC, retained
  sims/
    hfem_unified_sim.py             — HFEM unified simulator (new)
    drc3_perfect_simulation.py      — DRC-3 perfect sim, retained
    drc_warp_collapse_sim.py        — DRC-WC sim, retained
  hfem_unified_report.json          — simulator output (generated)
```

Repo name: user wrote `TaoishTechy/<whatever>` — `<whatever>` was a placeholder. This package uses `TaoishTechy/Hollow-Flat-Earth-Multiverse`. Rename the folder to any `<whatever>` on upload; file contents do not depend on the repo name.

---

*HFEM-UT v1.0 — built from DRC-3 (12/12 + 5/5 unit + null 6/6) + DRC-WC (W1-W8) + #149-#154 falsifiers. Hypothetical test model. Consensus: Earth is an oblate spheroid, warp drives are speculative, imports are mathematics.*
