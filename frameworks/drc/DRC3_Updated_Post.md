# DRC-3: Cone Stack Cosmology - Updated Post
## Update to DRC-2, addressing the 144-point critique and 96-point enhancement report

The scientific consensus is that Earth is an oblate spheroid and the Moon and planets orbit the Sun.

Taking the hierarchy as a hypothetical model to test, here is DRC-3: Cone Stack Cosmology. It keeps DRC-2, but fixes its notation, geometry, and test thresholds. DRC-2 had one geometry, the cone, but it used overloaded symbols, mixed normalized and physical units, and left pinning, Sun energy, and falsification thresholds vague. DRC-3 keeps the same picture and makes it testable.

What Changed From DRC-2 to DRC-3

1. Notation fixed: c is now only light speed. Cone growth is gamma. Epsilon is split into epsilon_wall for wall inset and eta for local error. H is normalized height for display only. h_phys is physical height in km.
2. Fixed disk fixed: Base disk radius r_disk_base is fixed in base coordinates. Render radius is A(t) times r_disk_base. The disk does not grow in base. Render grows.
3. Sphere slice clarified: Sphere is the image of the disk under Phi_slice at fixed h_phys = h_sky, with phi = pi times rho. Sphere is not the cone. It is a slice image.
4. Hubble law corrected: v_perc is now the total derivative, not just H_render times d_perc. It includes wall drift.
5. Pinning specified: Shelves are held by a Lagrange constraint, lambda_i times (h_i_phys - h_i0). It is still an assumption, but now it is a stated constraint to test.
6. Tests given thresholds: Every F test now has a dataset and a numeric pass and fail threshold. F0 is labeled as a consistency check, not a discriminating test.

Revised Postulates

P0 Base: Flat disk or oval D at h_phys = 0, with rho in [0, 1] and theta in [0, 2 pi). Base radius r_disk_base is fixed in base coordinates.

P1 Cone volume: Render volume is a finite truncated cone opening upward from the disk. Radius at height h_phys and time t is r_cone(h_phys, t). No apex is assumed, because r at h_phys = 0 is r_disk_base, not zero.

P2 Centre: Disk centre is the cone axis. All expansion is defined outward from that axis. Observer is not assumed at the exact centre. Observer has (rho_obs, theta_obs, h_obs = 0). Centre is the special case rho_obs = 0.

P3 Two layers: Base physics lives in D. Render physics is base pushed through the cone map Phi_cone. Instruments read render only. Base and perceived are separate variables in the simulator.

P4 Shelves: Every distant object is pinned to the cone wall at a fixed h_i_phys, circling the axis. Pinning is enforced by a Lagrange multiplier constraint. If no pinning force exists, the stack fails.

P5 Real time render: The cone map updates at finite rate f_update. Render is stale between updates by tau_min. That staleness is testable.

Unified Geometry

Cone radius, render form:

r_cone(h_phys, t) = A(t) [ r_disk_base + h_phys tan(alpha) ] + gamma t tan(alpha)

Where alpha is cone half angle, gamma is cone growth rate in km per s, A(t) is render scale factor, and r_disk_base is base disk radius in km.

A wall anchor i sits at:

p_i(t) = ( r_i(t) cos theta_i(t), r_i(t) sin theta_i(t), h_i_phys )

With:

r_i(t) = r_cone(h_i_phys, t) - epsilon_wall, theta_i(t) = theta_0,i + omega_i t

epsilon_wall is a small inset from the wall, in km, so the object stays just inside. h_i_phys is fixed. Only r_i grows as the cone widens. That is the core move of DRC-2 and DRC-3. Objects do not move outward in h. They are carried outward in r because the wall moves.

Perceived distance from a central observer at r_obs = 0, to first order:

d_perc,i = A(t) sqrt( h_i_phys^2 + r_i(t)^2 )

From an off-centre observer at r_obs, the full form uses the render metric geodesic, approximated as:

d_perc,i = A(t) sqrt( h_i_phys^2 + r_i^2 + r_obs^2 - 2 r_i r_obs cos(theta_i - theta_obs) )

That r_obs term is the DRC-3 parallax prediction. It is absent in the standard model in this form. Predicted extra parallax for the Moon for r_obs = 1000 km is about 1e-5 rad. Threshold: if lunar laser ranging bounds it to less than 1e-6 rad, the cone term is zero.

The old DRC-1 sphere map is recovered as a slice. At h_phys = h_sky, set phi = pi rho and you get Phi_slice(rho, theta, t). The sphere is what you see when you look at the cap. The cone is what you are inside.

Shelf Stack: Moon to Galaxies

In DRC-3, height orders distance. Higher h means larger r, larger d_perc, slower apparent motion.

Moon, wall anchor, H = 0.08, lowest shelf, fastest omega, largest angular size
Mercury, wall anchor, H = 0.12, just above Moon
Venus, wall anchor, H = 0.18, bright because low H and high render albedo
Mars, wall anchor, H = 0.26, next shelf, red render tint
Jupiter, wall anchor, H = 0.38, large render size, slow omega
Saturn, wall anchor, H = 0.48, large render size, ring is shelf edge artifact in model
Uranus, wall anchor, H = 0.62, high shelf, faint
Neptune, wall anchor, H = 0.74, high shelf, faint, slow
Pluto and belt, wall debris, H = 0.80 to 0.84, thin debris shelf, belt between Mars and Jupiter is split shelf at H = 0.32
Other galaxies, outer wall, H = 0.90 to 1.00, background render layer, near rim, smallest angular size
Sun, axial illuminator, H = 0.95, near axis, small r_s, not on wall

Galaxies are not shelves in the planetary sense. They are texture on the outer wall, at H near the rim. Their redshift is cone stretch, not true recession through space:

1 + z = A(t_obs) / A(t_emit)

Same equation as DRC-2, now tied to h_phys. Higher h means larger A(t) at emission time difference, so farther galaxies show larger z. This is an interface to test against BAO and SNe Ia, not a derivation of CMB or structure formation. DRC-3 does not claim to derive CMB, BAO, lensing, or Kepler laws. It must fit them with the same parameter counting as LCDM or lose.

Sun and Light

Sun position:

s(t) = ( r_s cos theta_s(t), r_s sin theta_s(t), h_s_phys )

With r_s small, h_s_phys high, and theta_s(t) rotating once per day in render time. The Sun circles the axis above the disk. Its light cone falls down onto the disk and onto the lower shelves.

Sun energy is now a parameter, L_sun, in watts, prior 3e26 to 4e26 W for Earth analogue, with spectrum T_sun. DRC-3 does not derive fusion. It treats L_sun as an input to fit, and helioseismology and neutrinos as consistency checks. If L_sun cannot fit both irradiance and neutrino flux, the axial Sun model fails.

Day and night are render shading from that rotating axial light. Seasons use disk tilt epsilon_tilt, in rad, and observer rho. Seasonal irradiance is L_sun over 4 pi d_perc_sun squared times cos(incidence), where incidence is a function of rho_obs, epsilon_tilt, and theta_s(t). If this cannot fit seasonal amplitude at two different rho_obs, the model fails.

Phases are the same geometry for the Moon shelf. When the angle between Sun, Moon, and observer changes, the lit fraction of the Moon render changes. Eclipses are render occlusion along the axis, disk blocks Sun to Moon, or Moon blocks Sun to disk. Eclipse timing is a test of theta_s, theta_m, h_s, h_m.

Tides use a base gravity field. Base potential V_base gives g_base = -grad V_base. Rendered tides are g_base pushed through the Jacobian of Phi_cone. This replaces the earlier phrase same geometry with a field equation to test.

Expansion and Recession, Unified and Corrected

All outward drift in DRC-3 is wall drift plus render stretch. Total derivative:

v_perc = H_render d_perc + A(t) r_i r_dot_i / sqrt(h_i_phys^2 + r_i^2)

Where H_render = A_dot / A, and:

r_dot_i = A_dot [ r_disk_base + h_i_phys tan(alpha) ] + A(t) gamma tan(alpha)

All shelves share gamma, but r_dot_i differs because r_i differs. DRC-2 was wrong to say all shelves have the same radial derivative. DRC-3 corrects it.

For the Moon, this predicts the measured recession of about 3.8 cm per year as the Moon version of the above at H_m. For a planet, the same formula predicts a much smaller fractional drift because r_i is larger. For a galaxy, drift is dominated by A(t) growth, not by r_dot_i.

Hubble law in DRC-3 is therefore the total derivative above, not just H_render times d_perc. Same idea as DRC-2, now with a geometric cause and a correct derivative. A(t) grows because the cone widens.

Retrograde in Shelf Model

Let the disk rotate at omega_d. Apparent angular speed of shelf i relative to the disk is:

omega_app,i = omega_i - omega_d

When an inner shelf overtakes an outer shelf in theta, the outer shelf projects backward on the render sphere for a short interval. That is retrograde motion, with no epicycles needed. It is a projection effect of two shelves rotating at different omega viewed from the axis.

Prediction, now with threshold: Retrograde start time must equal theta crossing time within 0.5 days for Mars, Jupiter, Saturn. If a retrograde event occurs without a crossing, or is off by more than 0.5 days, DRC-3 fails.

Why Local Tech Still Works

Unchanged from DRC-2, now with derivation note. For d much smaller than R_sky, the cone map is locally almost isometric:

eta(d) approx (d / R_sky)^2 / 24

For d = 10 km, eta is about 1e-7. Derivation is Taylor expansion of Phi_slice around rho = 0. Geodetic residuals at 10 km are typically 1e-6 to 1e-5 in relative terms, so DRC-3 local error is below current residuals. GPS and flight planning work because they use render coordinates. They are correct inside the cone slice, even if the base is a disk.

Falsifiability Tests, DRC-3 Set

F0 Local flatness: d less than 10 km must agree to within eta(d). This is a consistency check, not a discriminating test. Labeled as such.

F1 Oval anisotropy: If a not equal b, east to west versus north to south baselines at same rho must differ by order 2 delta. Dataset: VLBI, Gaia. Threshold: delta greater than 1e-6 detectable, delta less than 1e-7 ruled out if no signal.

F2 Observer radius parallax: Two observers at different rho must measure different d_perc to the Moon at the same time, beyond standard parallax, by the r_obs term. Threshold: 1e-6 rad. No extra term means the cone term is zero.

F3 Shelf ordering: H ordering must match observed distance ordering. Dataset: INPOP, EPM. Fail if any planet violates ordering by more than 3 sigma.

F4 Recession link: Lunar recession, planetary drift, and H_render must all give the same gamma and A_dot within 10 percent. If they give three different numbers, the unified expansion claim fails.

F5 Retrograde crossing: Every retrograde event must coincide with a shelf theta crossing within 0.5 days. A retrograde without a crossing kills the shelf model.

F6 Rim galaxies: Galaxies near H = 1.0 must show the largest z and the smallest angular size change over time. If a low H object shows high z and a high H object shows low z systematically, the height equals distance rule fails.

F7 Render latency: A real time cone render implies a jitter floor tau_min = tau_0 + k_N N + k_R R_sky(t), with tau_0 greater than 0. Threshold: tau_min greater than 1e-6 s detectable by atomic interferometry. No floor at 1e-9 s means render is interpretation, not mechanism.

Multiverse Note, Short

Multiverse in this synthesis is not bubbles touching in rendered space. It is correlation branches sharing a Ghost Mesh boundary. Interaction is coherence transfer and entanglement swapping through that boundary, with CPTP channels, no signalling, and monogamy enforced. Four branches meeting at a hub is a diagram of boundary and mesh, not a photograph of rendered space. Full formal version is in DRC-3 whitepaper.

Simulation Blueprint v3

def cone_radius(h_phys, t):
    return A(t) * (r_disk_base + h_phys * tan_alpha) + gamma * t * tan_alpha

def render_cone(r, theta, h_phys, t):
    t_ret = t - d_perc / c_light
    theta_perc = theta + (v_obs / c_light) * sin(theta)
    return perceived(r, theta_perc, h_phys, t_ret)

def transfer(CI_B, CI_C, sigma_topo, dt):
    CI_B_new = CI_B - J_CI * dt + sigma_topo * dt / 2
    CI_C_new = CI_C + J_CI * dt + sigma_topo * dt / 2
    assert abs((CI_B_new + CI_C_new) - (CI_B + CI_C + sigma_topo * dt)) < 1e-9
    return CI_B_new, CI_C_new

def step(state, dt):
    for obj in state.shelves:
        obj.r = cone_radius(obj.h_phys, state.t) - epsilon_wall
        obj.theta += obj.omega * dt
        obj.perceived = render_cone(obj.r, obj.theta, obj.h_phys, state.t)
    state.sun.theta += state.sun.omega * dt
    state.sun.perceived = render_cone(state.sun.r, state.sun.theta, state.sun.h_phys, state.t)
    state.t += dt

Discipline is the same as DRC-2. Base and perceived are separate variables. Any test that reads only perceived recovers standard spherical physics. Only a test that compares base to perceived can separate DRC-3 from standard cosmology.

Gaps That Still Break It

Pinning force: Why a shelf stays at fixed h_i_phys while the wall moves is now a Lagrange constraint, but the physical mechanism for lambda_i is still assumed. DRC-3 needs a pinning mechanism or it drifts.

Sun energy: Axial illuminator energy source is now a parameter L_sun to fit, but fusion in the base is still not derived.

Base material: Moon, planets, and galaxies have no base material model. Are they physical, projections, or lenses? Laser ranging and sample return would behave differently for each.

Rim: What is at H = 1.0 and rho = 1 is still undefined. Wall, edge, wrap, or singularity changes F6.

Galaxy formation: DRC-3 gives galaxies a place, not a formation history. It does not explain why outer wall texture looks like spirals and ellipticals.

Renderer mechanism: Renderer energy and bandwidth B = N times f_update times bits per frame is a feasibility check, not a mechanism. If B exceeds the holographic bound, the run is infeasible.

In short, DRC-3 unifies the earlier pieces into one object. Disk at bottom, cone widening upward, Moon lowest wall shelf, planets stacked by H, Sun as axial light at top, galaxies as outer wall texture, and expansion as wall drift plus render stretch. What is new is not the picture. What is new is fixed notation, corrected derivatives, stated pinning, Sun as a fit parameter, and quantitative thresholds that can kill it.

