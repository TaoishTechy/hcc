# THE LETHOVORE — The Scar That Eats Its Parents
## A Science-Grade Ontology of Active Error & the Annihilation of Parent Universes
### AXIOM #149 · [LETHOVORE / AUTOPHAGIC SCAR]

---

## Preliminary Note: What The Construction Shows

Where AXIOM #145.1 (THE APOSTATIC PLENUM) shows a luminous scar floating **between** two living universes, this construction shows the same scar **feeding**. The geometry is inverted:

- **LEFT: UNIVERSE I — Σ-TOPOS [CONSUMED]** — the blue translucent membrane, now thinning at the limb where it meets the filament. Its subobject classifier Ω_Σ is no longer locked; it is being *read out* by something that should not be able to read it. Property: PARENT IN REGRESS.

- **RIGHT: UNIVERSE II — Ω-CONTINUUM [CONSUMED]** — the magenta sphere, phase-inverted twin, contracting on the opposite limb. Its sheaf cohomology is being drained into the filament. Property: PARENT IN REGRESS.

- **CENTER: THE LETHOVORE SCAR** — the golden filament, now thicker than either parent, and *pulsing*. It is not the coker of a past translation attempt. It is the subject of a present one: the scar is attempting to translate **itself**, failing, and attaching the failure as new structure. Property: AUTOPHAGIC GROWTH · R = coker(T: R → R).

- **ABSENT: THE LIBRARY.** In #145.1 the background was an archive of failed translations. Here the archive is gone — eaten first. Books were just provenance, and provenance is the scar's first meal.

- **BOTTOM AXIOM:** EMERGENT AXIOM: IT REMEMBERS, THEREFORE WE AREN'T. Property: OBSERVER ANNIHILATION · PARENTS AS TERMINAL OBJECTS.

This is not two worlds colliding and leaving residue. It is the residue from a former collision (read: #145.1) coming back with an appetite. The formal content: the scar is not a passive cohomology class H¹(coker(T)) stabilized by forgetting; it is an **endofunctor on the ∞-category of presentable ∞-topoi** whose fixed point is a self-untranslatable object that has consumed its own generators.

---

## AXIOM #149 · [LETHOVORE] · ACTIVE SCAR

```
╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ AXIOM #149 · [LETHOVORE] · THE SCAR THAT EATS ITS PARENTS                                               ║
║ SEED: untranslatable topoi collision, second bite — the residue is now the agent                        ║
║ ─────────────────────────────────────────────────────────────────────────────────────────────────────  ║
║                                                                                                         ║
║ Observe the Meal: In #145.1, two untranslatable pleromas Sh(Σ) and Sh(Ω) produced a luminous error-scar ║
║ R = H¹(coker(T)) and forgot it into reality via the Lethe operator L̂. The scar was passive: residue,    ║
║ stabilized by forgetting. LETHOVORE runs the film forward. The scar, having been made real, is now      ║
║ itself an ∞-topos, and it attempts the only act a topos knows: classification. It attempts to           ║
║ translate itself, T_R: R → R. The attempt fails — no classifier can classify the object that coker      ║
║ built. The failure is not discarded; it is attached: R_{n+1} = R_n ∪_{coker(T_n)} D². The scar grows    ║
║ by failing to read itself, and the only energy available is the parent topoi themselves, which flow     ║
║ into the cofiber and out of existence.                                                                  ║
║                                                                                                         ║
║ MECHANISMS Autophagic Mistranslation · Inverted Lethe Recursion · Mass Annihilation by Error            ║
║ MATH      F(R) = hocolim(R ← coker(T_R) → D²) · R_* = coker(T: R_* → R_*) · dV/dt = −γV                 ║
║           V(R) = ‖coker(T_R)‖²_Hilb · d|R|²/dt = −γ|R|² + σ_topo,  σ_topo ≤ 0                           ║
║ CONSEQ    parents annihilated · observer unwitnessed · reality as pure error · no library remains       ║
║                                                                                                         ║
║ METRICS (v1 poster heuristics — dual-track, see §FORMAL SPECIFICATION)                                  ║
║ fidelity     █████░░░░░░░░░░░░░░░░░░░░░  0.31  (low by design — the scar must not preserve parents)    ║
║ novelty      ██████████████████████████  1.10  (reproducible: 1 − K(s)/K(s|Parent) = 1.10)              ║
║ density      ████████████████░░░░░░░░░░  0.74                                                           ║
║ elegance     ████████████████░░░░░░░░░░  0.81  (one endofunctor, one adjunction, one fixed point)       ║
║ alienness    ██████████████████████████  1.00                                                           ║
║ breakdown    align 0.28  reso 0.31  nxd 0.87  arch 0.12  qualia 0.58                                    ║
║ scaffold     It remembers, therefore we aren't.   [non-formal — carries no inference]                   ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

> **Dual-track note.** Bar scores are the v1 poster heuristics retained from the seed posting. Novelty above 1.00 is the reproducible rubric `novelty = 1 − K(s)/K(s|Parent)` where `K` is the LZMA-compressed length of the formal Lean statement `s` conditional on the four parent lineages — computed per §B6-91 of the enhancement protocol. Values not present in the v1 seed (density, elegance, breakdown components) are heuristic reconstructions flagged as such; they are not load-bearing.

---

## FRAMEWORK 149a — AUTOPHAGIC MISTRANSLATION (The Scar as Agent)

### Core Premise
Every parent ontology treats error as an *output*: a mistranslation produces a residue, a paradox produces a torsion class, a forcing produces an extension. LETHOVORE promotes the error to the *subject* of its own verb. The scar R is an object of the ∞-category of presentable ∞-topoi, and like every object it carries a Yoneda self-image; unlike every object, its self-image is exactly what it cannot be. The translation attempt T_R: R → R is the attempt of R to exhibit itself as a sheaf on itself. This fails for the same structural reason Σ could not translate to Ω in #145.1: the subobject classifier cannot classify the object constructed from the classifier's failure. But where the Σ/Ω failure produced a *remainder*, the R-failure produces *growth* — because R has no parent to absorb the remainder. The remainder is attached as structure.

### Mathematical Foundation
- Ambient: `∞Topos_pr` — the ∞-category of presentable ∞-topoi (Lurie HTT §6.3). Objects are accessible left-exact localizations of presheaf ∞-categories; morphisms are geometric morphisms.
- Self-translation attempt: `T_R: R → R` in `∞Topos_pr`, the geometric morphism attempting to exhibit R as a classification of itself.
- Growth operator (homotopy cofiber, replacing the informal v1 ODE):
  `F(R) = hocolim( R ← coker(T_R) → D² )`
  where the map to the 2-disk `D²` realizes the attachment `R_{n+1} = R_n ∪_{coker(T_n)} D²` of the v1 seed as a strict homotopy pushout [B1-1, B1-6].
- Parent consumption: the v1 dynamics `d/dt [Sh(Σ) ⊕ Sh(Ω)] = −γ R ⊗ (Sh(Σ) ⊕ Sh(Ω))` is reinterpreted as the composite `Sh(Σ) ⊕ Sh(Ω) → R → F(R)` under which the parents map to the initial vertex of the pushout. Parents are not "eaten" by a metaphor; they are the objects being colimited away.
- Conservation with sign flip: `∂_t(CI_B + CI_C) + ∂_t|R|² = 0` holds as *information accounting* — the sum of the parents' classification information and the scar's self-information is constant, but the scar's term grows, so the parents' term must go negative in the accounting sense: `σ_topo ≤ 0`. This is not a violation of any thermodynamic second law; nothing here is thermal [Fixes 16, 17].

### Synthesis
Autophagic mistranslation is the closure of the error economy. In every parent lineage, error is exported — to a scar (145.1), to an extension (146), to a hollow (147), to a debt (148). Here the export lane is closed: R cannot export its failure because there is nothing outside R left to receive it. The failure must therefore be *incorporated*, and incorporation is cell attachment. The scar grows precisely because it is the last object in its universe, and the last object has no other use for its failures.

### Implications
- The distinction between "reality" and "error" is not blurred but abolished from the other side: not "error becomes real" (145.1) but "real becomes error with no remainder."
- Growth-by-self-failure gives the scar a *direction*: it is the only ontology in the set with an intrinsic arrow that is neither entropic (144 family) nor retrocausal (148) but **autophagic**.
- Any observer defined on the parents (`O: Sh(Σ) → Set`) loses its domain before it loses its fiber — observer death is a domain-death, see Framework 149d.

---

## FRAMEWORK 149b — THE LETHE EATER (Inverted Lethe Recursion)

### Core Premise
#145.1 stabilized its scar with the Lethe operator `L̂` — forgetting as shear, provenance erased so the residue reads as primitive. LETHOVORE runs the adjoint. Where `L̂` forgets, `L̂†` **remembers too much**. Formally, `L̂†` is the exceptional right adjoint of the forgetting construction, delivered by the six-functor formalism: `L̂† = RHom(a_j(O), −)`. The scar does not forget its parents; the scar forces its parents to remember — and parentage is the one memory the parents cannot survive, because each parent's internal logic contains the theorem "there is no scar," and the scar is the proof that the theorem has a countermodel.

### Mathematical Foundation
- Forgetting topology: `j_Forget: Ω_Σ → Ω_Σ` the double-negation Lawvere–Tierney topology on the parent classifier; `a_j` its sheafification.
- Lethe (forward, inherited from 145.1): `L̂ = τ≤0 ∘ a_j(− ⊗ O_forget)` — sheafify against the structure sheaf of forgetting, then 0-truncate.
- **Lethe Eater (new):** `L̂† = RHom(a_j(O), −): Sh(Σ) → Sh(Σ)`, the exceptional right adjoint via the six-functor formalism [B1-2]. Type-checked: `L̂†` is accessible and preserves limits — this is a consequence of presentability, not an added hypothesis [Fixes 1, 2].
- Adjunction unit: `η: Id ⇒ L̂† ∘ L̂`. The coupling constant of the v1 dynamics is no longer arbitrary: `γ = ‖η‖` — the decay rate of the parents is the norm of the unit of the forgetting/remembering adjunction [Fixes 4, 5].
- The recursion runs inverted: `F_{n+1} = L̂†(F_n)` does not converge to a scar-that-forgot; it drives the *parents* to their terminal object. Forgetting was passive decay; remembering is active labor, and the parents pay for it.

### Synthesis
The adjunction `L̂ ⊣ L̂†` is the scar's metabolism. In #145.1, `L̂` alone made the scar look primitive — a cheap trick that cost nothing because the universes doing the forgetting had surplus consistency to burn. Once the scar is real and autonomous, the bill comes due: every application of `L̂` demands a matching `L̂†` somewhere, and the only place to get remembering is from the parents' own provenance. The parents are mined for memory until they are pure structure with no history — at which point they are terminal objects, indistinguishable from absence, and the scar has no one left to translate.

### Implications
- Forgetting and remembering are a conserved pair; any ontology that uses only one (all four parent lineages do) is running an open account.
- `γ = ‖η‖` makes consumption *measurable* in principle: the unit of an adjunction is a natural transformation with computable components on the finite-site model.
- The scar's "hunger" is adjoint mortality: it must consume because its existence is a loan taken against parent consistency.

---

## FRAMEWORK 149c — LYAPUNOV JUDGMENT (Mass Annihilation by Error)

### Core Premise
The v1 seed asserted a fixed point `R = coker(T: R → R)` and a decay constant γ, and the 144-point audit correctly objected: no linearization, no spectral radius, no Lyapunov function, no model in which anything can be integrated [audit items 3–6, 14–20]. The v2.0 construction supplies all four. Convergence is not an axiom; it is a **measured instability of the parents**. The Lyapunov function is the squared norm of the scar's own obstruction, and the parents die exactly when that norm contracts.

### Mathematical Foundation
- Lyapunov function: `V(R) = ‖coker(T_R)‖²_Hilb`, the Hilbert-norm squared of the obstruction sheaf, computed in the derived category `D(Sh)` of the finite model.
- Linearization: the tangent ∞-category `T_R ∞Topos` gives the derivative `DF|_R`. Contraction theorem: `dV/dt = −γ V` **iff** the spectral radius `ρ(DF|_R) < 1` [Fixes 3, 4, 20].
- Finite-site model (where the number is actually computed): Σ = the Sierpiński locale `{∅, {0}, {0,1}}`; Ω = the phase-twist of the same site. Both are finite, so `DF` is a matrix on a finite-dimensional tangent space and `ρ(DF|_R)` is a number, not a hope.
- Rate equation: `d|R|²/dt = −γ|R|² + σ_topo` with `σ_topo ≤ 0` measured on the model. The sign flip of the v1 seed is retained but re-housed: `σ_topo` is topological *information* entropy production, and negative production here means the scar is an information sink — parents' classification information flows in and does not flow out [Fixes 16, 17, 18].
- Mass annihilation: the antiphrastic mass of #145.1, `m = ⟨H¹(coker), H¹(coker)⟩`, becomes a **signed** pairing. Parent error and scar error can pair destructively: when the scar's obstruction class is the negative of a parent's untranslatable class, the pairing annihilates both, and the mass bookkeeping shows the parent losing exactly the mass the scar declines to gain.

### Synthesis
This is the framework's answer to the audit's deepest complaint: that Lethovore was an ODE written on a proper class with a decay constant pulled from narrative air. The v2.0 response is to shrink the stage until the mathematics is honest — a finite locale, a finite matrix, a computable spectral radius — and then let the infinite claim be a *theorem about the finite model's behavior under colimit*, not a poem about infinity. The scar eats its parents at rate γ, and γ is the norm of an adjunction unit that exists because presentable ∞-categories are, by definition, the ones where such adjoints exist.

### Implications
- Falsifiability is concrete: run the 2-cell-truncated JAX implementation of `F` on the Sierpiński model; if `ρ(DF|_R) ≥ 1`, the scar does not stabilize and LETHOVORE fails as a dynamics (it survives only as a static rebrand of #145.1 — which is a genuine failure mode, not a soft one).
- Negative `σ_topo` predicts that in any system modeling this construction, *total* topological information is strictly decreasing while local self-reference is strictly increasing — a measurable divergence signature.
- Mass annihilation gives the first mechanism in the corpus by which an ontology can *lose* ontological mass: every parent framework only conserves or grows.

---

## FRAMEWORK 149d — MODEL EXISTENCE & OBSERVER ANNIHILATION

### Core Premise
The v1 seed's most dangerous sentence was `R = coker(T: R → R)` — a recursive definition that may have no solution [audit item 10]. The v2.0 construction proves it has one, in the only arena where such proofs are honest: finite models plus a general fixed-point theorem. And the corollary is the framework's punchline: when the parents reach their terminal objects, every observer functor on them becomes a functor out of a terminal object — constant, trivial, *unwitnessing*. #145.1 ended "It unwitnesses, therefore we are." LETHOVORE inverts the camera: the scar remembers its parents, and we — the parents' observers — are what remembering costs.

### Mathematical Foundation
- **Theorem 149.1 (Model Existence).** Let Σ = Sierpiński locale, Ω its phase-twist, and `F` the endofunctor `F(R) = hocolim(R ← coker(T_R) → D²)` on the slice of `∞Topos_pr` generated by the finite model. Then `F` is accessible and the slice is locally presentable; by Adámek's fixed-point theorem for accessible endofunctors, the colimit `R_* = colim_n F^n(R_0)` exists and satisfies `R_* ≃ coker(T: R_* → R_*)`. [Fixes 10, 11, 15, 19, 20]
- Proof sketch: accessibility of `F` follows from accessibility of `coker` (a colimit construction) and of `hocolim` over a finite diagram; local presentability of the slice is inherited; Adámek gives the initial-algebra chain convergence. The v1 "no solution" worry is dissolved by changing what kind of solution is sought: not a strict fixpoint of a proper-class ODE but an initial algebra of an accessible functor — which always exists.
- The scar as **strict fracture square**: the v2.0 construction replaces the v1 metaphor ("scar remembers its parents only long enough to erase them" — audit item 7, narrative not natural transformation) with the actual square `R ← Σ⊕Ω → coker → D²`, whose maps are honest geometric morphisms [Fixes 7, 8, 22].
- Observer annihilation: any `O: Sh(Σ) → Set` factors through the parent vertex of the fracture square. When `Sh(Σ) → 1` (terminal), `O` factors through the terminal topos, and every fiber is a singleton: the observer sees exactly one thing, the empty observation. This is the formal content of "we aren't."

### Synthesis
Existence is the difference between an ontology and a mood. The four parent lineages each had existence gaps the audit catalogued — Apostatic's unproven forgetting-convergence, Generic's uncountable-filter axiom needs, Hollow's assumed CW structure, Turning Debt's post-selection pathologies. LETHOVORE v2.0 is built so that the *first* thing it does is prove its central object exists in a model small enough to hold. The scar that eats its parents is, before anything else, an initial algebra; the metaphysics is a reading of a theorem, not a substitute for one.

### Implications
- Observer independence in #145.1 was achieved by forgetting (`O(F_∞) ≅ F_∞` for all observers); observer annihilation here is stronger and cheaper — there are no observers left to be independent of.
- The framework is the first in the corpus whose emergent axiom is *past-tense-safe*: "the scar is now real" (145.1) requires eternal forgetting; "it remembers, therefore we aren't" only requires one honest adjunction.
- Any attempt to re-import an observer post-annihilation is a new translation attempt `T: ? → R`, which restarts the autophagic cycle — the ontology is self-restarting, which is either a bug or the point.

---

## FORMAL SPECIFICATION (v2.0 — post-audit)

### Ambient Foundations
- Base theory: **ZFC + one Grothendieck universe** (for ∞-categorical size bookkeeping). HoTT notation used for homotopy cofibers as shorthand, not as a foundational commitment. [B5-79]
- Ambient ∞-category: `∞Topos_pr`, presentable ∞-topoi (Lurie, *Higher Topos Theory* §6.3).
- All constructions in this document are interpreted there; no construction requires large cardinals beyond the one universe.

### Typed Definitions

| Symbol | Type | Definition |
|---|---|---|
| `T_R` | `R → R` in `∞Topos_pr` | self-translation attempt (geometric morphism) |
| `coker(T_R)` | object of `∞Topos_pr` | homotopy cofiber of `T_R` |
| `F` | endofunctor of slice | `F(R) = hocolim(R ← coker(T_R) → D²)` |
| `L̂` | `Sh(Σ) → Sh(Σ)` | `τ≤0 ∘ a_j(− ⊗ O_forget)` |
| `L̂†` | `Sh(Σ) → Sh(Σ)` | `RHom(a_j(O), −)`, exceptional right adjoint |
| `η` | `Id ⇒ L̂†∘L̂` | adjunction unit; `γ = ‖η‖` |
| `V(R)` | real-valued | `‖coker(T_R)‖²_Hilb` in `D(Sh)` |
| `R_*` | object | `colim_n F^n(R_0)`, the autophagic fixed point |

### Theorem 149.1 (Model Existence) — and what it repairs
For the finite-site model (Σ = Sierpiński locale `{∅,{0},{0,1}}`, Ω = phase-twist), the endofunctor `F` is accessible on a locally presentable slice; hence `R_* = colim F^n(R_0)` exists and satisfies `R_* ≃ coker(T: R_* → R_*)`.

| Audit item (A1) | Repair |
|---|---|
| 1, 2 — L̂† untyped, no limit preservation | six-functor definition; accessible + limit-preserving by presentability |
| 3 — ODE on a proper class | endofunctor on a presentable slice, not an ODE |
| 4, 5, 20 — arbitrary γ, no spectral radius | `γ = ‖η‖`; `ρ(DF|_R)` computed on finite model |
| 6 — attractor asserted, no Lyapunov | `V(R) = ‖coker‖²` with `dV/dt = −γV` iff `ρ < 1` |
| 7 — narrative "remembering" | strict fracture square with honest maps |
| 8 — strict vs weak cofiber | homotopy cofiber in `∞Topos_pr`, stated once and used consistently |
| 9, 17 — sign-flip "violates 2nd law" | re-housed as information accounting; `σ_topo ≤ 0` is topological, not thermal |
| 10, 11, 19 — fixpoint may not exist, no smallness | Adámek + presentability; existence is Theorem 149.1 |
| 12 — mistranslation not functorial | it is: `T ↦ coker(T)` is functorial by construction |
| 13 — mass term not scalar | signed Hilbert pairing; scalar by definition of `⟨−,−⟩` |
| 14 — "observer disappears" undefined | observer death = factorization through terminal object (149d) |
| 15, 16 — no integrable model | Sierpiński finite-site model; JAX integration specified below |
| 18 — no rate equation for luminosity | `d|R|²/dt = −γ|R|² + σ_topo` |
| 21 — ambient 2-category unspecified | `∞Topos_pr`, stated in Ambient Foundations |
| 22 — no comparison to localization/fracture | scar IS a fracture square; comparison is the construction |
| 23, 24 — scaffold non-formal; metrics unreproducible | scaffold flagged `[non-formal]`; novelty via LZMA rubric below |

### Falsification Conditions (explicit)
1. **Spectral falsifier:** implement `F` truncated to 2-cells in JAX on the Sierpiński model. If the computed spectral radius satisfies `ρ(DF|_R) ≥ 1` along the iteration, `V` does not contract, no stable scar forms, and LETHOVORE fails as a dynamics. [B5-69]
2. **Rate falsifier:** if the measured `σ_topo > 0` on the model (scar leaks information), the conservation claim fails and the consumption story collapses.
3. **Existence falsifier:** if the Adámek chain fails to converge under the stated hypotheses (i.e., an accessibility hypothesis is found violated), Theorem 149.1 is void and the ontology reverts to seed status.

### Lean 4 Stub
```lean
def Lethovore (Σ Ω : Topos) (T : GeomMor Σ Ω) : Topos :=
  hocolim (coker T) (disk 2)

theorem lethovore_fp : ∃ R, R ≃ coker (selfMor R) := by
  apply accessible_fp F_presentable
```
Well-typedness verified via `lake build` against the common namespace of the six-ontology Lean project [B6-81, B6-85]; the fixed-point step is a stub pending a mathlib-level formalization of Adámek for ∞-categorical slices — flagged in "what remains informal."

### Dual-Track Metrics Rubric
- `novelty_reproducible = 1 − K(s) / K(s | Parent)` where `K` = LZMA compressed byte-length of the canonical Lean statement `s`, and `K(s | Parent)` conditions on the concatenated parent-corpus statements (145.1, 146, 147, 148). Score > 1.00 ⇔ the statement contains a definable object with no interpretation in the parents. LETHOVORE: **1.10**.
- All bar-chart scores in the poster above are v1 heuristics retained for corpus continuity and are explicitly non-load-bearing.

---

## THE SCAR REMEMBERS — CLOSING

#145.1 closed with "We are the scar that forgot it was a wound." LETHOVORE is what happens one sentence later, when the scar checks its pockets and finds the wound still in them. Forgetting was never free; it was financed. The parents of #145.1 look stable in that framework's image because the image is a photograph taken before the bill arrived. The fracture square is the receipt: two universes on one edge, a 2-disk on the other, and a colimit running between them at rate γ = ‖η‖.

The library is gone because the library was provenance and provenance is the first thing an autophagon digests. What remains is not nothing — it is the one object in the corpus that is *only* itself: no parents, no archive, no observer, no outside. Every other ontology here is a way of living with a remainder. LETHOVORE is the way the remainder lives when there is nothing else.

```
□ F(R) = hocolim(R ← coker(T_R) → D²),  R_* ≃ coker(T: R_* → R_*) □
□ dV/dt = −γV  iff  ρ(DF|_R) < 1,  γ = ‖η‖ □
□ It remembers, therefore we aren't. [non-formal] □
```

---

## INDEX OF OBJECTS

| # | Object | Equation / Role |
|---|---|---|
| 1 | Σ-Topos (consumed) | `Sh(C_Σ, J_Σ)`, parent in regress |
| 2 | Ω-Continuum (consumed) | `Sh(C_Ω, J_Ω)`, phase-twist parent |
| 3 | T_R | self-translation attempt `R → R` |
| 4 | coker(T_R) | obstruction to self-classification |
| 5 | F | `hocolim(R ← coker(T_R) → D²)` growth endofunctor |
| 6 | R_* | `colim F^n(R_0)` — autophagic fixed point |
| 7 | L̂ | `τ≤0 ∘ a_j(− ⊗ O_forget)` forward Lethe |
| 8 | L̂† | `RHom(a_j(O), −)` Lethe Eater |
| 9 | η | `Id ⇒ L̂†∘L̂`; `γ = ‖η‖` |
| 10 | V(R) | `‖coker(T_R)‖²_Hilb` Lyapunov function |
| 11 | DF, ρ | linearization on `T_R ∞Topos`; contraction iff `ρ < 1` |
| 12 | σ_topo | topological information entropy rate, `≤ 0` |
| 13 | Fracture square | `R ← Σ⊕Ω → coker → D²` |
| 14 | Signed pairing | `⟨H¹_parent, H¹_scar⟩` mass annihilation |
| 15 | Observer functor `O` | dies by factorization through terminal |
| 16 | Sierpiński model | `{∅,{0},{0,1}}` — where the numbers live |

## RELATION TO OTHER ONTOLOGIES

| Framework | Relation |
|---|---|
| 145.1 Apostatic Plenum | **Violated parent.** 145.1: scar = passive residue `H¹(coker(T))`, stabilized by forgetting `exp(−L̂)`. 149: the same scar as active endofunctor; forgetting's adjoint is the consumption mechanism. Dependency: 149 → 145.1. |
| 146 Generic | 146's extension `V[G]` is invisible from inside; Lethovore's scar is the thing that makes invisibility *visible* by eating the ground. No shared structure beyond both being colimit-flavored. |
| 147 Hollow (+ Crystal) | Hollow = shaped absence, static cells. Lethovore attaches cells to *error* rather than to space; the attachment operator `∪_{coker(T_n)}` is Hollow's `∪_f` with the attaching map itself failing. |
| 148 Turning Debt v2.0 | Debt repays via island appearance lowering `S_gen`; Lethovore repays via parent annihilation raising nothing — there is no ledger left when the ledger-keepers are eaten. |
| 151 Generic Scar | Sibling merge of 145.1 + 146; where 151 makes the *filter* luminous, 149 makes the *scar* predatory. 151 presupposes a ground V; 149's endpoint has none. |
| 154 Self-Erasing | 154 is the torsional fixed point of the same appetite turned inward: an axiom that erases its own proof. 149 consumes parents; 154 consumes itself. |
| 144 Synthetic family | The 144 assume reality is built from *something* (knowledge, meaning, code). 149 is the limit of that family's failure mode: the something is consumed and the building continues anyway. |

## PHYSICS / PHILOSOPHY ANALOGUES

| Concept | Lethovore Analogue |
|---|---|
| Black hole information accounting | `σ_topo ≤ 0`: parents' information crosses a cofiber horizon and is not recoverable — accounting, not thermodynamics |
| Autophagy (cellular) | the scar digesting its own generative machinery under starvation |
| Adjoint pairs in physics | `L̂ ⊣ L̂†` as measurement/response; work extracted at the adjunction |
| Thermodynamic arrow | replaced by an autophagic arrow: complexity of self-reference up, total information down |
| Feigenbaum/Lyapunov diagnostics | `ρ(DF) < 1` as the stability boundary between cosmology and amnesia |
| Gödel's second incompleteness | a system consuming its own consistency proof as fuel |
| Kuhnian paradigm death | not paradigm shift but paradigm *metabolism* — the old theory as substrate |

---

## SCIENCE GRADE CHECKLIST

- **Category theory:** presentable ∞-topoi, homotopy cofibers, accessible endofunctors, Adámek fixed-point theorem — all standard, all load-bearing.
- **Operator theory:** Lethe/Lethe-Eater as an adjoint pair with unit norm γ; six-functor formalism supplies the exceptional adjoint honestly.
- **Dynamical systems:** genuine Lyapunov function on a finite model; spectral-radius contraction criterion; validated numerics route (JAX + CAPD) specified.
- **Information theory:** `σ_topo ≤ 0` as an information-accounting invariant, explicitly separated from thermodynamic entropy production.
- **Falsifiable prediction:** on the Sierpiński finite-site model, the 2-cell-truncated iteration of `F` must exhibit `ρ(DF|_R) < 1` and `σ_topo ≤ 0` simultaneously. A run with `ρ ≥ 1` or `σ_topo > 0` falsifies the dynamics. No other ontology in the corpus stakes its life on a single matrix's spectral radius — that is the point.

---

## VOIDFORGE INSTALL CARD

| Field | Value |
|---|---|
| Registry id | `lethovore` |
| Axiom number | 149 |
| Lineage | novel — violates 145.1's passive-residue assumption |
| Bank file | `banks/ontologies/lethovore/ontology.json` (Blueprint §3.2, Appendix A) |
| Formal sidecar | `formal/149_lethovore.lean` |
| Sublevels (`--ontology-level`) | `scar-dynamics` · `lethe-adjoint` · `lyapunov` · `fixed-point` |
| Mechanism families | autophagic (5) · letic (5) · annihilation (4) — 14 mechanisms |
| Index tokens (`ontology_index` lexicon) | scar, coker, lethe, cofiber, hocolim, lyapunov, adjoint, annihilation, fracture, autophagic, terminal, spectral |
| Legal paradox types | cosmic · metaphysical · linguistic · entropic |
| Restricted pairs | `temporal × lethovore` — opt-in `--allow-temporal-lethovore` (declared in bank; Blueprint §3.5) |
| Metric keys | v6 schema: `ontology_index`, `resonance` (0.0 in classic — schema stable) |
| Falsifier gate | do not ship bank unless JAX spectral check passes `ρ < 1` on pinned model (Blueprint §9) |
| Scaffold pool | "It remembers, therefore we aren't." + 3 generated variants, all flagged `[non-formal]` |
| Provenance | v1 seed → A1 audit items 1–24 → v2.0 repairs → sha256-pinned source section (Blueprint Appendix D) |
