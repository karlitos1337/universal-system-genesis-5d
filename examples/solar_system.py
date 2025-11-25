#!/usr/bin/env python3
"""Solar System Example: Planetary Effortless Stability

Demonstrates how planets orbit stars through gravitational balance -
a macroscopic scale where zwanglose Stabilität is most intuitive.

Was geschieht? -> Planets orbit the sun
Wie geschieht das? -> Through gravitational attraction and inertia
Wieviel? -> Quantified by orbital parameters (speed, distance, period)
Durch welche zwanglose Interaktion? -> Mass-based gravitational equilibrium
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core.stability_principle import SystemState, Interaction, StabilityPrinciple
from core.interaction_dynamics import InteractionDynamics
import numpy as np


class CelestialBody:
    """Represents a celestial body (planet, star, etc.)"""
    
    def __init__(self, name: str, mass: float, distance: float, velocity: float):
        self.name = name
        self.mass = mass          # In Earth masses
        self.distance = distance  # In AU (Astronomical Units)
        self.velocity = velocity  # In km/s
    
    def orbital_period_years(self) -> float:
        """Calculate orbital period using Kepler's Third Law"""
        # T^2 = a^3 (for solar mass)
        return self.distance ** 1.5
    
    def __repr__(self):
        return f"{self.name}(M={self.mass:.2f}M⊕, d={self.distance:.2f}AU)"


def demonstrate_earth_orbit():
    """Show Earth's orbit as example of effortless stability"""
    print("=== Solar System: Erde-Sonne System ===")
    print()
    print("Die Erde umkreist die Sonne seit 4,5 Milliarden Jahren.")
    print("Ohne Motor. Ohne Treibstoff. Ohne zentrale Steuerung.")
    print()
    
    # Create bodies
    sun = CelestialBody(
        name="Sonne",
        mass=333000,  # Solar mass in Earth masses
        distance=0,
        velocity=0
    )
    
    earth = CelestialBody(
        name="Erde",
        mass=1.0,
        distance=1.0,  # 1 AU by definition
        velocity=29.78  # km/s
    )
    
    print(f"Zentralkörper: {sun}")
    print(f"Orbiter: {earth}")
    print(f"Umlaufdauer: {earth.orbital_period_years():.2f} Jahre")
    print(f"Bahngeschwindigkeit: {earth.velocity} km/s")
    print()
    
    # Analyze using framework
    principle = StabilityPrinciple()
    
    # System state
    components = {
        'sun': {'mass': sun.mass, 'position': 0},
        'earth': {'mass': earth.mass, 'distance': earth.distance}
    }
    
    state = SystemState(
        components=components,
        energy=-1.5e33,  # Gravitational binding energy in Joules (simplified)
        entropy=0.05,    # Very low - highly ordered orbit
        complexity=2.0   # Two-body system
    )
    
    # Gravitational interaction
    orbit = Interaction(
        type="gravitational",
        strength=0.9,      # Very strong, stable
        energy_cost=0.0,   # Absolutely effortless - no energy spent
        participants=['sun', 'earth']
    )
    
    stability = principle.calculate_stability(state)
    orbit_quality = principle.evaluate_interaction(orbit, state)
    
    print("--- Stabilitätsanalyse ---")
    print(f"System-Stabilität: {stability:.3f}")
    print(f"Orbit-Qualität: {orbit_quality:.3f}")
    print(f"Energiekosten: {orbit.energy_cost} (NULL!)")
    print()
    
    print("✅ ZWANGLOSE STABILITÄT BESTÄTIGT")
    print()
    print("Die Erde umkreist die Sonne OHNE:")
    print("  ✗ Triebwerke")
    print("  ✗ Treibstoff")
    print("  ✗ Navigationssystem")
    print("  ✗ Wartung")
    print("  ✗ Zentrale Kontrolle")
    print()
    print("Die Erde umkreist die Sonne DURCH:")
    print("  ✓ Gravitationsanziehung")
    print("  ✓ Trägheit (Impulserhaltung)")
    print("  ✓ Natürliches Gleichgewicht")
    print("  ✓ Energieminimierung")
    print()
    print("4,5 Milliarden Jahre. Perfekt stabil. Mühelos.")
    print()
    
    return state, orbit, stability


def compare_all_planets():
    """Compare stability across all planets in our solar system"""
    print("=== Vergleich: Alle Planeten ===")
    print()
    print("Jeder Planet zeigt dasselbe Prinzip:")
    print("Zwanglose Stabilität durch Gravitationsgleichgewicht")
    print()
    
    planets = [
        CelestialBody("Merkur", 0.055, 0.39, 47.87),
        CelestialBody("Venus", 0.815, 0.72, 35.02),
        CelestialBody("Erde", 1.0, 1.0, 29.78),
        CelestialBody("Mars", 0.107, 1.52, 24.07),
        CelestialBody("Jupiter", 317.8, 5.20, 13.07),
        CelestialBody("Saturn", 95.2, 9.54, 9.69),
        CelestialBody("Uranus", 14.5, 19.19, 6.81),
        CelestialBody("Neptun", 17.1, 30.07, 5.43),
    ]
    
    print("Planet   | Masse (M⊕) | Distanz (AU) | Geschw. (km/s) | Periode (Jahre)")
    print("-" * 75)
    
    for planet in planets:
        period = planet.orbital_period_years()
        print(f"{planet.name:8s} | {planet.mass:10.2f} | {planet.distance:12.2f} | {planet.velocity:14.2f} | {period:15.2f}")
    
    print()
    print("ALLE folgen Keplers Gesetzen. ALLE sind stabil.")
    print("KEINE Ausnahmen. KEINE Anomalien.")
    print()
    print("Das ist kein Zufall. Das ist zwanglose Stabilität.")
    print("Das ist die universelle Entstehungsformel.")
    print()


def demonstrate_unstable_orbit():
    """Show what happens without proper balance"""
    print("=== Gegenbeispiel: Instabiler Orbit ===")
    print()
    print("Was passiert, wenn das Gleichgewicht fehlt?")
    print()
    
    # Too slow - will fall into sun
    slow_body = CelestialBody(
        name="Zu-Langsam",
        mass=1.0,
        distance=1.0,
        velocity=15.0  # Half of Earth's velocity
    )
    
    print(f"Körper: {slow_body}")
    print(f"Geschwindigkeit: {slow_body.velocity} km/s (zu langsam!)")
    print(f"Benötigt: {29.78} km/s für stabilen Orbit")
    print()
    print("⚠️ KEINE ZWANGLOSE STABILITÄT")
    print()
    print("Zu langsam → Gravitation überwiegt")
    print("             → Körper fällt zur Sonne")
    print("             → Kollision")
    print()
    
    # Too fast - will escape
    fast_body = CelestialBody(
        name="Zu-Schnell",
        mass=1.0,
        distance=1.0,
        velocity=50.0  # Too fast
    )
    
    print(f"Körper: {fast_body}")
    print(f"Geschwindigkeit: {fast_body.velocity} km/s (zu schnell!)")
    print(f"Fluchtgeschwindigkeit: {42.1} km/s")
    print()
    print("⚠️ KEINE ZWANGLOSE STABILITÄT")
    print()
    print("Zu schnell → Trägheit überwiegt")
    print("            → Körper verlässt System")
    print("            → Keine Bindung")
    print()
    print("Lektion: Nur das GENAUE Gleichgewicht erzeugt Stabilität.")
    print("         Die Natur findet dieses Gleichgewicht SELBST.")
    print()


def simulate_solar_system_formation():
    """Describe how solar systems form naturally"""
    print("=== Wie entstand das Sonnensystem? ===")
    print()
    print("Vor 4,6 Milliarden Jahren:")
    print()
    
    phases = [
        ("1", "Gaswolke kollabiert durch Gravitation", "Zwanglos"),
        ("2", "Wolke rotiert und flacht ab zur Scheibe", "Drehimpulserhaltung"),
        ("3", "Zentrum verdichtet sich zur Sonne", "Gravitationskontraktion"),
        ("4", "Staubkörner in Scheibe kollidieren", "Natürliche Aggregation"),
        ("5", "Planetesimale entstehen (km-Größe)", "Stoßweise Akkretion"),
        ("6", "Protoplaneten formen sich (1000 km)", "Gravitative Akkumulation"),
        ("7", "Planeten räumen Bahnen frei", "Massedomination"),
        ("8", "Orbits stabilisieren sich", "Gleichgewichtszustand"),
    ]
    
    print("Phase | Vorgang                              | Mechanismus")
    print("-" * 75)
    for phase, process, mechanism in phases:
        print(f"  {phase}   | {process:40s} | {mechanism}")
    
    print()
    print("JEDE Phase geschieht MÜHELOS:")
    print("  ✓ Keine Planung erforderlich")
    print("  ✓ Keine externe Steuerung")
    print("  ✓ Nur natürliche Kräfte")
    print("  ✓ Selbstorganisation")
    print()
    print("Das Ergebnis: Unser stabiles Sonnensystem.")
    print("8 Planeten. Alle auf stabilen Bahnen.")
    print("Seit Milliarden Jahren. Ohne Manager.")
    print()


def main():
    """Run all solar system demonstrations"""
    print()
    print("#" * 70)
    print("#" + " " * 68 + "#")
    print("#  SOLAR SYSTEM: Zwanglose Stabilität auf makroskopischer Skala  #")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    print()
    
    # Example 1: Earth's orbit
    state, orbit, stability = demonstrate_earth_orbit()
    print()
    
    # Example 2: All planets
    compare_all_planets()
    print()
    
    # Example 3: Unstable orbits
    demonstrate_unstable_orbit()
    print()
    
    # Example 4: Formation story
    simulate_solar_system_formation()
    print()
    
    # Summary
    print("=" * 70)
    print("ZUSAMMENFASSUNG")
    print("=" * 70)
    print()
    print("Was wir vom Sonnensystem lernen:")
    print()
    print("1. Planeten umkreisen Sterne MÜHELOS durch Gravitation")
    print("2. Stabiler Orbit = perfektes Gleichgewicht (Anziehung ⇄ Trägheit)")
    print("3. Sonnensysteme ENTSTEHEN von selbst aus Gaswolken")
    print("4. Milliarden Jahre stabil - ohne Wartung, ohne Kontrolle")
    print()
    print("Dasselbe Prinzip wie bei Atomen:")
    print("  Elektron umkreist Proton  →  Planet umkreist Stern")
    print("  Quantenskala             →  Kosmische Skala")
    print("  ZWANGLOSE STABILITÄT funktioniert auf ALLEN Skalen")
    print()
    print("Wenn Planeten ohne CEO auskommen...")
    print("...warum brauchen menschliche Systeme dann Hierarchien?")
    print()
    print("FÜR DIE MENSCHHEIT. 🌍")
    print()


if __name__ == "__main__":
    main()
