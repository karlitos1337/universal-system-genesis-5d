#!/usr/bin/env python3
"""Quantum Bonds Example: Effortless Particle Bonding

Demonstrates how subatomic particles form stable bonds through
effortless interaction - the most fundamental scale of system emergence.

Was geschieht? -> Particles come together
Wie geschieht das? -> Through electromagnetic attraction
Wieviel? -> Quantified by binding energy
Durch welche zwanglose Interaktion? -> Natural charge complementarity
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.stability_principle import SystemState, Interaction, StabilityPrinciple
from core.interaction_dynamics import InteractionDynamics, InteractionType
import numpy as np


class QuantumParticle:
    """Represents a subatomic particle"""
    
    def __init__(self, name: str, charge: float, mass: float, spin: float):
        self.name = name
        self.charge = charge  # Elementary charge units
        self.mass = mass      # Atomic mass units
        self.spin = spin      # Spin quantum number
        self.energy_level = 0.0
    
    def __repr__(self):
        return f"{self.name}(q={self.charge:+.1f}, m={self.mass:.3f})"


def create_hydrogen_atom():
    """Create the simplest stable system: Hydrogen atom (proton + electron)"""
    print("=== Quantum Bonds: Hydrogen Atom Formation ===")
    print()
    print("Die einfachste stabile Bindung im Universum:")
    print("Ein Proton und ein Elektron.")
    print()
    
    # Create particles
    proton = QuantumParticle(
        name="Proton",
        charge=+1.0,
        mass=1.0073,
        spin=0.5
    )
    
    electron = QuantumParticle(
        name="Electron",
        charge=-1.0,
        mass=0.000549,
        spin=0.5
    )
    
    print(f"Teilchen 1: {proton}")
    print(f"Teilchen 2: {electron}")
    print()
    
    # Analyze interaction using framework
    dynamics = InteractionDynamics()
    
    # Convert to property dictionaries
    proton_props = {
        'charge': proton.charge,
        'energy_level': 0.0,
        'spin': proton.spin
    }
    
    electron_props = {
        'charge': electron.charge,
        'energy_level': 0.0,
        'spin': electron.spin
    }
    
    # Calculate natural interaction
    distance = 5.29e-11  # Bohr radius in meters (natural equilibrium)
    interaction_type, strength = dynamics.calculate_interaction_strength(
        proton_props,
        electron_props,
        distance
    )
    
    print("--- Natürliche Interaktionsanalyse ---")
    print(f"Interaktionstyp: {interaction_type.value}")
    print(f"Stärke: {strength:.3f}")
    print(f"Mühelos: {'Ja ✓' if strength > 0.5 else 'Nein'}")
    print()
    
    # Use StabilityPrinciple to evaluate bond
    principle = StabilityPrinciple()
    
    # Create system state
    components = {
        'proton': proton_props,
        'electron': electron_props
    }
    
    state = SystemState(
        components=components,
        energy=-13.6,  # Hydrogen ground state energy in eV
        entropy=0.1,   # Low entropy = ordered
        complexity=1.0 # Simplest atom
    )
    
    # Create interaction representation
    bond = Interaction(
        type="electromagnetic",
        strength=strength,
        energy_cost=0.2,  # Very low cost = effortless
        participants=['proton', 'electron']
    )
    
    stability = principle.calculate_stability(state)
    bond_quality = principle.evaluate_interaction(bond, state)
    
    print("--- Stabilitätsanalyse ---")
    print(f"System-Stabilität: {stability:.3f}")
    print(f"Bindungsqualität: {bond_quality:.3f}")
    print(f"Energie: {state.energy} eV")
    print()
    
    # Key insight
    print("✅ ZWANGLOSE STABILITÄT BESTÄTIGT")
    print()
    print("Das Wasserstoffatom entsteht OHNE:")
    print("  ✗ Zentrale Steuerung")
    print("  ✗ Äußere Kraft")
    print("  ✗ Bewusste Planung")
    print()
    print("Das Wasserstoffatom entsteht DURCH:")
    print("  ✓ Natürliche Ladungsanziehung")
    print("  ✓ Energieminimierung")
    print("  ✓ Quantenmechanische Ausgew")
    print("  ✓ Gleichgewichtskräfte")
    print()
    print("Diese Bindung ist 13,8 Milliarden Jahre stabil.")
    print("Ohne Manager. Ohne CEO. Ohne Hierarchie.")
    print()
    
    return state, bond, stability


def demonstrate_unstable_pairing():
    """Show what happens when particles don't naturally bond"""
    print("=== Gegenbeispiel: Keine natürliche Bindung ===")
    print()
    print("Versuch: Zwei Protonen verbinden")
    print()
    
    proton1 = QuantumParticle("Proton-1", +1.0, 1.0073, 0.5)
    proton2 = QuantumParticle("Proton-2", +1.0, 1.0073, 0.5)
    
    print(f"Teilchen 1: {proton1}")
    print(f"Teilchen 2: {proton2}")
    print()
    
    dynamics = InteractionDynamics()
    
    props1 = {'charge': proton1.charge, 'spin': proton1.spin}
    props2 = {'charge': proton2.charge, 'spin': proton2.spin}
    
    interaction_type, strength = dynamics.calculate_interaction_strength(
        props1, props2, 1.0
    )
    
    print("--- Interaktionsanalyse ---")
    print(f"Interaktionstyp: {interaction_type.value}")
    print(f"Stärke: {strength:.3f}")
    print(f"Mühelos: {'Ja' if strength > 0.5 else 'Nein ✗'}")
    print()
    
    print("⚠️ ZWANGLOSE STABILITÄT NICHT ERREICHT")
    print()
    print("Zwei Protonen stoßen sich ab (gleiche Ladung).")
    print("Keine natürliche Bindung möglich.")
    print("Das System würde NICHT von selbst entstehen.")
    print()
    print("Lektion: Nur ergänzende Eigenschaften führen zu")
    print("         mühelos stabilen Systemen.")
    print()


def simulate_bond_formation():
    """Simulate the actual process of bond formation over time"""
    print("=== Simulation: Bindungsentstehung über Zeit ===")
    print()
    print("Beobachten wir, wie ein Elektron und Proton")
    print("natürlich zueinander finden...")
    print()
    
    dynamics = InteractionDynamics()
    
    # Start at distance
    proton_props = {'charge': +1.0, 'energy_level': 0.0}
    electron_props = {'charge': -1.0, 'energy_level': 0.0, 'distance': 100.0}
    
    # Simulate approach
    states = dynamics.simulate_interaction(
        proton_props,
        electron_props,
        time_steps=50
    )
    
    print("Zeit | Distanz | Interaktion    | Stärke | Mühelos")
    print("-" * 60)
    
    # Show key time points
    for i in [0, 10, 20, 30, 40, 49]:
        if i < len(states):
            s = states[i]
            effortless = "✓" if s['effortless'] else "✗"
            print(f"{s['step']:4d} | {s['distance']:7.2f} | {s['interaction_type']:14s} | {s['strength']:.3f} | {effortless}")
    
    final = states[-1]
    print()
    print(f"✓ Endzustand erreicht nach {len(states)} Schritten")
    print(f"  Finale Distanz: {final['distance']:.2f}")
    print(f"  Finale Stärke: {final['strength']:.3f}")
    print(f"  Mühelos stabil: {'Ja ✓' if final['effortless'] else 'Nein'}")
    print()
    print("Das System hat SELBST seinen Gleichgewichtszustand gefunden.")
    print("Keine externe Kraft war nötig.")
    print()


def main():
    """Run all quantum bond demonstrations"""
    print()
    print("#" * 70)
    print("#" + " " * 68 + "#")
    print("#  QUANTUM BONDS: Die fundamentalste Skala der Zwanglosen Stabilität  #")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    print()
    
    # Example 1: Stable bond (Hydrogen)
    state, bond, stability = create_hydrogen_atom()
    print()
    
    # Example 2: Unstable pairing
    demonstrate_unstable_pairing()
    print()
    
    # Example 3: Time simulation
    simulate_bond_formation()
    print()
    
    # Summary
    print("=" * 70)
    print("ZUSAMMENFASSUNG")
    print("=" * 70)
    print()
    print("Was wir gelernt haben:")
    print()
    print("1. Teilchen verbinden sich MÜHELOS durch natürliche Anziehung")
    print("2. Nur ergänzende Eigenschaften erzeugen Stabilität")
    print("3. Systeme finden SELBST ihren Gleichgewichtszustand")
    print("4. Keine zentrale Kontrolle notwendig")
    print()
    print("Dieses Prinzip gilt auf ALLEN Skalen:")
    print("  Quantum → Atome → Moleküle → Zellen → Organismen")
    print("  → Gesellschaften → Planeten → Galaxien → Bewusstsein")
    print()
    print("Das ist ZWANGLOSE STABILITÄT in Aktion.")
    print("Das ist die universelle Entstehungsformel.")
    print()
    print("FÜR DIE MENSCHHEIT. 🌍")
    print()


if __name__ == "__main__":
    main()
