"""Python wrapper for AlterBBN.

Provides a Python interface to the AlterBBN C code for BBN calculations.
"""

from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional


@dataclass
class BBNAbundances:
    """BBN abundance results."""
    Y_p: float  # Helium-4 mass fraction
    D_H: float  # Deuterium to Hydrogen ratio
    He3_H: float  # Helium-3 to Hydrogen ratio
    Li7_H: float  # Lithium-7 to Hydrogen ratio
    Li6_H: float  # Lithium-6 to Hydrogen ratio
    Be7_H: float  # Beryllium-7 to Hydrogen ratio


class AlterBBNWrapper:
    """Wrapper for AlterBBN BBN calculations."""
    
    def __init__(self, alterbbn_path: Optional[str] = None):
        """Initialize wrapper.
        
        Args:
            alterbbn_path: Path to AlterBBN executable (default: external/AlterBBN/primary.x)
        """
        if alterbbn_path is None:
            # Find AlterBBN relative to this file
            base_path = Path(__file__).parent / "AlterBBN"
            self.alterbbn_path = base_path / "primary.x"
            self.input_ini_path = base_path / "input.ini"
        else:
            self.alterbbn_path = Path(alterbbn_path)
            self.input_ini_path = self.alterbbn_path.parent / "input.ini"
        
        if not self.alterbbn_path.exists():
            raise FileNotFoundError(f"AlterBBN executable not found: {self.alterbbn_path}")
        if not self.input_ini_path.exists():
            raise FileNotFoundError(f"AlterBBN input.ini not found: {self.input_ini_path}")

    def _render_input_ini(self, base_text: str, eta: float, DeltaN: float, tau_neutron: float) -> str:
        def repl(key: str, value: str, text: str) -> str:
            pattern = rf"(?m)^\s*{re.escape(key)}\s*=\s*[^\n]+$"
            if re.search(pattern, text) is None:
                return text
            return re.sub(pattern, f"{key} = {value}", text)

        out = base_text
        out = repl('eta', f"{eta:.6e}", out)
        out = repl('dnnu', f"{DeltaN:.6e}", out)
        out = repl('tau', f"{tau_neutron:.6f}", out)
        return out
    
    def compute_abundances(
        self,
        eta: float = 6.1e-10,  # Baryon-to-photon ratio
        DeltaN: float = 0.0,  # Extra neutrino species
        tau_neutron: float = 880.2,  # Neutron lifetime (seconds)
    ) -> BBNAbundances:
        """Compute BBN abundances for given cosmological parameters.

        Args:
            eta: Baryon-to-photon ratio
            DeltaN: Extra relativistic degrees of freedom (maps TEP H-mod)
            tau_neutron: Neutron lifetime in seconds

        Returns:
            BBNAbundances with all light element abundances
        """
        alterbbn_abs = self.alterbbn_path.resolve()
        ini_abs = self.input_ini_path.resolve()

        original_ini = ini_abs.read_text(encoding='utf-8')
        patched_ini = self._render_input_ini(original_ini, eta=eta, DeltaN=DeltaN, tau_neutron=tau_neutron)

        # AlterBBN primary.c *requires* a mode argument; without it the
        # input.ini is ignored and a fixed SBBN run is performed.
        # We always run in 'standard' mode because dnnu correctly captures
        # the TEP Hubble modification H_TEP = H_LCDM / A.
        mode = 'standard'

        try:
            ini_abs.write_text(patched_ini, encoding='utf-8')
            result = subprocess.run(
                [str(alterbbn_abs), mode],
                capture_output=True,
                text=True,
                cwd=str(alterbbn_abs.parent),
            )
        finally:
            ini_abs.write_text(original_ini, encoding='utf-8')
        
        # Note: AlterBBN returns exit code 1 even on success sometimes
        # Check if we got valid output instead
        if result.returncode != 0 and not result.stdout.strip():
            raise RuntimeError(f"AlterBBN failed: {result.stderr}")
        
        # Parse output
        abundances = self._parse_output(result.stdout)
        return abundances
    
    def _parse_output(self, output: str) -> BBNAbundances:
        """Parse AlterBBN output to extract abundances."""
        lines = output.strip().split('\n')
        
        # Find the central values line
        for line in lines:
            if line.startswith('cent:'):
                parts = line.split()
                # Format: cent: Yp H2/H He3/H Li7/H Li6/H Be7/H
                values = [float(p) for p in parts[1:]]
                return BBNAbundances(
                    Y_p=values[0],
                    D_H=values[1],
                    He3_H=values[2],
                    Li7_H=values[3],
                    Li6_H=values[4],
                    Be7_H=values[5],
                )
        
        raise ValueError("Could not parse AlterBBN output")
    
    def compute_lcdm_abundances(self) -> BBNAbundances:
        """Compute standard LCDM BBN abundances."""
        return self.compute_abundances()
    
    def compute_tep_abundances(self) -> BBNAbundances:
        """Compute TEP BBN abundances.
        
        For TEP, BBN occurs in the matter frame, so abundances
        are essentially the same as LCDM at high redshift.
        """
        return self.compute_abundances()


# Convenience function for quick access
def get_alterbbn_abundances() -> BBNAbundances:
    """Get BBN abundances from AlterBBN."""
    wrapper = AlterBBNWrapper()
    return wrapper.compute_lcdm_abundances()


if __name__ == "__main__":
    # Test
    print("Testing AlterBBN wrapper...")
    abundances = get_alterbbn_abundances()
    print(f"Y_p = {abundances.Y_p:.6f}")
    print(f"D/H = {abundances.D_H:.4e}")
    print(f"He3/H = {abundances.He3_H:.4e}")
    print(f"Li7/H = {abundances.Li7_H:.4e}")
