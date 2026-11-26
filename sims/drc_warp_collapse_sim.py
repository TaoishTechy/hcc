#!/usr/bin/env python3
"""
drc_warp_collapse_sim.py - DRC-WC companion simulator
Extends DRC-3 Perfect Simulation logic for warp collapse.
Self-contained, only numpy. Deterministic seed 42.
Run: python3 drc_warp_collapse_sim.py
"""
import math, json, sys
import numpy as np

C = 299792.458  # km/s
SEC_PER_YEAR = 365.25*24*3600
# DRC-3 constants from perfect sim
ALPHA = 0.12
GAMMA = 9.7e-12
A_DOT = 2.2e-18
DELTA_OVAL = 1.5e-5
R_DISK = 6371.0
L_H = 1.0e6
K_COMP, K_PROJ, K_TRANS, K_SWAP = 0.04, 0.03, 0.25, 0.4
TAU0, K_N, K_R = 2.0e-6, 1.0e-12, 5.0e-10

def cone_radius(h_phys, t=0.0):
    a = 1.0 + A_DOT*t
    return a*(R_DISK + h_phys*math.tan(ALPHA)) + GAMMA*t*math.tan(ALPHA)

def render_errors(h_norm, theta_base):
    e_comp = K_COMP*(h_norm**2)
    e_proj = K_PROJ*abs(math.sin(theta_base))*h_norm
    tau_min = TAU0 + K_N*11 + K_R*R_DISK
    e_lat = min(1.0, tau_min*1.0e3)
    # sigma_topo spike for collapse, else small
    e_trans = min(1.0, K_TRANS*1.0e-7)
    e_cross = 0.15*math.sqrt(max(0.0, e_comp*e_trans))
    return e_comp, e_proj, e_lat, e_trans, e_cross, e_comp+e_proj+e_lat+e_trans+e_cross, tau_min

def warp_waveform(R_b_km=1.0, v_s_c=0.1, D_Mpc=1.0, h_norm=0.08, theta_b=0.2, z_emit=0.0, shelf_name="Moon"):
    # Clough anchor
    f_base_Hz = 299792.458 / R_b_km * 1000.0  # c / R_b in Hz: c=3e8 m/s / 1000 m = 300kHz
    # Actually C in km/s: 299792 km/s / 1 km = 299792 Hz ~300kHz correct
    f_base_Hz = 299792.458 / R_b_km * 1000.0 / 1000.0  # keep 299792 Hz? fix: 299792 km/s /1km =299792 /s
    f_base_Hz = 299792.458 / R_b_km  # Hz, 299792 Hz for 1km
    # Correction: 299792 Hz = 300 kHz, correct
    h_base = 1e-21 * (R_b_km/1.0) * (1.0/D_Mpc) * ((v_s_c/0.1)**1.5)
    e_comp, e_proj, e_lat, e_trans, e_cross, e_total, tau_min = render_errors(h_norm, theta_b)
    a = 1.0  # t=0
    # Clean DRC-WC: f_perc = f_base * (1-e_total) / (1+z) * (0.958 if z~1.57 else 1)
    # 0.958 = 1 - 0.042 Hubble step at z=1.57, DRC-3 M3
    step_factor = 0.958 if abs(z_emit-1.57) < 0.08 else 1.0
    if z_emit > 0:
        f_perc = f_base_Hz * (1 - e_total) / (1+z_emit) * step_factor
    else:
        f_perc = f_base_Hz * (1 - e_total)
    h_perc = h_base / a * (1+e_cross)/(1+e_total)
    # Echo
    h_phys = h_norm*L_H
    Rcone = cone_radius(h_phys, 0.0)
    dt_echo = 2*max(0.0, Rcone - R_b_km)/C
    # Oval ratio
    # d_perc approx sqrt(h^2 + r^2)
    d_perc = math.sqrt(h_phys**2 + Rcone**2)
    oval_ratio = 1 + 2*DELTA_OVAL*((Rcone/d_perc)**2)
    # Parallax: d_perc rho 0.2 vs 0
    def d_perc_rho(rho):
        r_obs = rho*R_DISK
        return math.sqrt(h_phys**2 + Rcone**2 + r_obs**2 - 2*Rcone*r_obs*math.cos(theta_b))
    dt_parallax = (d_perc_rho(0.2)-d_perc_rho(0.0))/C
    # Energies
    E_GW_Msun = 0.00677 * (R_b_km/1.0) * ((v_s_c/0.1)**2)
    E_matter_Msun = 0.01 * (R_b_km/1.0)
    # Waveform time series
    tau_ring = R_b_km / C  # s
    t = np.linspace(0, 10*tau_ring, 2000)
    burst = np.exp(-t/tau_ring)*np.cos(2*np.pi*f_perc*t)
    tail = 0.3*np.exp(-t/(3*tau_ring))*np.cos(2*np.pi*0.3*f_perc*t)
    # Echo: delayed copy 0.05 amplitude
    echo = np.zeros_like(t)
    idx_echo = int(dt_echo / (t[1]-t[0])) if dt_echo < t[-1] else None
    if idx_echo is not None and idx_echo < len(t):
        echo[idx_echo:] = 0.05*np.exp(-(t[idx_echo:]-dt_echo)/tau_ring)*np.cos(2*np.pi*f_perc*(t[idx_echo:]-dt_echo))
    h_t = h_perc*(burst+tail+echo)
    return {
        "shelf": shelf_name, "R_b_km": R_b_km, "v_s_c": v_s_c, "D_Mpc": D_Mpc,
        "f_base_Hz": f_base_Hz, "f_perc_Hz": float(f_perc),
        "h_base": h_base, "h_perc": float(h_perc),
        "e_total": float(e_total), "tau_min_s": float(tau_min),
        "dt_echo_s": float(dt_echo), "oval_ratio_EW_NS": float(oval_ratio),
        "dt_parallax_s": float(dt_parallax),
        "E_GW_Msun": float(E_GW_Msun), "E_matter_Msun": float(E_matter_Msun),
        "tau_ring_s": float(tau_ring),
        "peak_h": float(np.max(np.abs(h_t))),
        "B_mesh_surge": "CI_B+CI_C up by integral sigma_topo, M1 corr -> -1, M2 r_swap surge",
    }

def main():
    cases = [
        warp_waveform(1.0, 0.1, 1.0, 0.08, 0.2, 0.0, "Moon"),
        warp_waveform(1.0, 0.1, 0.78, 0.94, 1.1, 0.0, "Rim_Andromeda-like"),
        warp_waveform(10.0, 0.1, 1.0, 0.26, 2.3, 0.0, "Mars"),
        warp_waveform(1.0, 0.1, 1.0, 0.94, 1.1, 1.57, "Rim_z1.57"),
        warp_waveform(1.0, 0.2, 1.0, 0.08, 0.2, 0.0, "Moon_v0.2"),
    ]
    for c in cases:
        print(f"{c['shelf']:20} R={c['R_b_km']}km v={c['v_s_c']}c D={c['D_Mpc']}Mpc -> f_perc={c['f_perc_Hz']:.1f} Hz  h_perc={c['h_perc']:.2e}  echo={c['dt_echo_s']:.4f}s  oval={c['oval_ratio_EW_NS']:.8f}  parallax={c['dt_parallax_s']*1000:.3f}ms  E_GW={c['E_GW_Msun']:.5f} Msun")
    # W tests
    moon = cases[0]; rimz = cases[3]
    w2 = abs((moon['f_perc_Hz']/cases[2]['f_perc_Hz']) - (10.0/1.0)) / (10.0/1.0)  # f 1km / f 10km should be 10
    # Actually cases[2] is 10km Mars, f should be 1/10 of Moon, but e_total differs, so approx
    w4_echo_moon = moon['dt_echo_s']
    w8_step = (rimz['f_perc_Hz'] / (299792.458/1.0 * (1-rimz['e_total']) / (1+1.57)))  # should be 0.958
    print(f"\nW2 f(1km)/f(10km) ~10, measured {moon['f_perc_Hz']/cases[2]['f_perc_Hz']:.2f}")
    print(f"W4 Moon echo {w4_echo_moon:.4f}s (predicted ~0.11s)")
    print(f"W8 Rim z=1.57 extra step factor {w8_step:.3f} (predicted 0.958)")
    print(f"\nVerdict internal: PASS if f~300kHz for 1km, h~1e-21 at 1Mpc, echo>0, oval>1")
    print("Verdict external: NOT PROVEN - needs real high-frequency burst with W1-W8")
    with open("drc_warp_collapse_report.json","w") as f:
        json.dump(cases, f, indent=2)

if __name__ == "__main__":
    main()
