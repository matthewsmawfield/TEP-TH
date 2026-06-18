#!/usr/bin/env python3
"""Shared utilities for the TEP-TH temporal horizon pipeline."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
from typing import Any, Iterable
import numpy as np

try:
    from scripts.utils.logger import TEPLogger, print_status, set_step_logger
except ImportError:
    class TEPLogger:
        def __init__(self, *args, **kwargs): pass
    def print_status(msg, status="INFO"): print(f"[{status}] {msg}")
    def set_step_logger(logger): pass

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

C_KM_S = 299_792.458

# Cosmological constants for temporal horizon calculations
H0_KM_S_MPC = 70.0
OMEGA_M = 0.3
OMEGA_L = 0.7
OMEGA_K = 0.0

# Temporal horizon parameters
DEFAULT_EPSILON_T = 0.1  # Temporal shear amplitude (increased for visible effect)
DEFAULT_Z_T = 100.0      # Transition redshift (moved to higher z)
DEFAULT_N_T = 1.0        # Transition steepness

# Early-epoch screening parameters
DEFAULT_T_LOCK = 0.03     # Temperature at which shear activates (eV)
DEFAULT_N_EPOCH = 2.0    # Epoch screening steepness

def ensure_dirs() -> None:
    for d in [RAW_DIR, RESULTS_DIR, FIGURES_DIR, PROCESSED_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def e_z(z: np.ndarray | float) -> np.ndarray | float:
    zp1 = 1 + np.asarray(z)
    OMEGA_R = 9.0e-5  # Radiation density parameter
    return np.sqrt(OMEGA_M * zp1 ** 3 + OMEGA_R * zp1 ** 4 + OMEGA_K * zp1 ** 2 + OMEGA_L)

def h_km_s_mpc(z: np.ndarray | float) -> np.ndarray | float:
    return H0_KM_S_MPC * e_z(z)

def temporal_shear_factor(z: np.ndarray | float, epsilon_t: float = DEFAULT_EPSILON_T, 
                          z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T) -> np.ndarray | float:
    """Compute temporal shear factor S(z) = exp(-(z/z_t)^n_t)."""
    z = np.asarray(z)
    return np.exp(-(z / z_t) ** n_t)

def epoch_screening(z: np.ndarray | float, T_lock: float = DEFAULT_T_LOCK, 
                    n_epoch: float = DEFAULT_N_EPOCH) -> np.ndarray | float:
    """Compute early-epoch screening function S_epoch(T).
    
    Suppresses temporal shear during early universe (BBN, recombination)
    and activates during late times.
    
    S_epoch = 1 / (1 + (T/T_lock)^n_epoch)
    
    where T = T_CMB * (1+z) is the CMB temperature.
    """
    z = np.asarray(z)
    T_CMB = 2.725  # K
    T_z = T_CMB * (1 + z)  # Temperature in K
    T_eV = T_z * 8.617e-5  # Convert K to eV
    return 1.0 / (1.0 + (T_eV / T_lock) ** n_epoch)


def conformal_factor_A(z: np.ndarray | float, epsilon_t: float = DEFAULT_EPSILON_T,
                      z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T,
                      T_lock: float = DEFAULT_T_LOCK, n_epoch: float = DEFAULT_N_EPOCH,
                      use_screening: bool = False) -> np.ndarray | float:
    """Compute conformal clock-rate factor A(z) = (1+z/z_t)^(-epsilon_t * S_epoch).
    
    For temporal horizon: A(z) → 0 as z → ∞, A(z) → 1 as z → 0.
    
    With screening: epsilon_eff = epsilon_t * S_epoch(T)
    """
    z = np.asarray(z)
    if use_screening:
        S = epoch_screening(z, T_lock, n_epoch)
        epsilon_eff = epsilon_t * S
    else:
        epsilon_eff = epsilon_t
    return (1 + z / z_t) ** (-epsilon_eff)

def effective_scale_factor(z: np.ndarray | float, epsilon_t: float = DEFAULT_EPSILON_T,
                           z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T,
                           T_lock: float = DEFAULT_T_LOCK, n_epoch: float = DEFAULT_N_EPOCH,
                           use_screening: bool = False) -> np.ndarray | float:
    """Compute effective scale factor a_eff(z) = A(z).
    
    In TEP the effective scale factor IS the conformal clock-rate factor.
    a_eff → 0 as z → ∞ corresponds to A → 0 at the temporal horizon.
    """
    return conformal_factor_A(z, epsilon_t, z_t, n_t, T_lock, n_epoch, use_screening)

def temporal_horizon_limit(z: np.ndarray | float, epsilon_t: float = DEFAULT_EPSILON_T,
                          z_t: float = DEFAULT_Z_T, n_t: float = DEFAULT_N_T) -> np.ndarray | float:
    """Test if a_eff = A approaches zero (temporal horizon limit)."""
    a_eff = effective_scale_factor(z, epsilon_t, z_t, n_t)
    return a_eff < 1e-10  # Threshold for horizon approach

class TEPEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.floating, np.bool_)):
            return obj.item()
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, cls=TEPEncoder) + "\n", encoding="utf-8")

def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def write_csv(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    rows = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows: return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

def rel(path: Path) -> str:
    return str(path.relative_to(PROJECT_ROOT))

def step_json_path(step_id: str) -> Path:
    return RESULTS_DIR / f"{step_id}.json"

def step_csv_path(step_id: str) -> Path:
    return RESULTS_DIR / f"{step_id}.csv"

def figure_path(step_id: str) -> Path:
    return FIGURES_DIR / f"{step_id}.png"

def rounded(value: float, digits: int = 6) -> float:
    return round(float(value), digits)
