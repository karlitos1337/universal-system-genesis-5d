"""Interaction Dynamics Module

This module describes how components interact in effortless ways.
Key principle: Interactions happen naturally when conditions align,
without force or central coordination.

Was geschieht? -> Components come into contact
Wie geschieht das? -> Through natural proximity and compatible properties
Wieviel? -> Quantified by interaction strength and energy transfer
Durch welche zwanglose Interaktion? -> Through natural affinity and balance
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict
from enum import Enum


class InteractionType(Enum):
    """Types of effortless interactions"""
    ATTRACTION = "attraction"  # Components naturally drawn together
    REPULSION = "repulsion"    # Components naturally pushed apart
    RESONANCE = "resonance"    # Components vibrate in harmony
    EXCHANGE = "exchange"      # Components exchange properties/energy
    NEUTRAL = "neutral"        # No significant interaction


@dataclass
class InteractionField:
    """Represents the field through which interactions happen"""
    type: InteractionType
    strength: float  # How strong the interaction is (0.0 to 1.0)
    range: float     # How far the interaction reaches
    energy_transfer: float  # Energy exchanged in interaction
    
    def is_active_at_distance(self, distance: float) -> bool:
        """Check if interaction is active at given distance"""
        return distance <= self.range and self.strength > 0.1
    
    def calculate_effect(self, distance: float) -> float:
        """Calculate interaction effect based on distance"""
        if distance > self.range:
            return 0.0
        # Inverse square law for natural interactions
        normalized_distance = distance / self.range
        effect = self.strength * (1.0 - normalized_distance ** 2)
        return max(0.0, effect)


class InteractionDynamics:
    """Models how components interact naturally and effortlessly"""
    
    def __init__(self):
        self.interaction_history: List[Dict] = []
    
    def calculate_interaction_strength(
        self,
        component_a_properties: Dict,
        component_b_properties: Dict,
        distance: float
    ) -> Tuple[InteractionType, float]:
        """
        Calculate natural interaction between two components.
        
        Returns:
            (InteractionType, strength): Type and strength of interaction
        """
        # Check for resonance (similar properties)
        resonance = self._check_resonance(
            component_a_properties,
            component_b_properties
        )
        
        if resonance > 0.7:
            return InteractionType.RESONANCE, resonance
        
        # Check for complementary attraction
        attraction = self._check_attraction(
            component_a_properties,
            component_b_properties
        )
        
        if attraction > 0.5:
            return InteractionType.ATTRACTION, attraction
        
        # Check for incompatibility (repulsion)
        repulsion = self._check_repulsion(
            component_a_properties,
            component_b_properties
        )
        
        if repulsion > 0.5:
            return InteractionType.REPULSION, repulsion
        
        # Default to neutral or exchange
        if distance < 1.0:
            return InteractionType.EXCHANGE, 0.3
        
        return InteractionType.NEUTRAL, 0.0
    
    def _check_resonance(self, props_a: Dict, props_b: Dict) -> float:
        """Check if components resonate (have similar frequencies/properties)"""
        if 'frequency' in props_a and 'frequency' in props_b:
            freq_diff = abs(props_a['frequency'] - props_b['frequency'])
            # Perfect resonance at freq_diff = 0, decreases with difference
            resonance = 1.0 / (1.0 + freq_diff)
            return resonance
        return 0.0
    
    def _check_attraction(self, props_a: Dict, props_b: Dict) -> float:
        """Check for complementary attraction between components"""
        attraction = 0.0
        
        # Check charge complementarity
        if 'charge' in props_a and 'charge' in props_b:
            charge_product = props_a['charge'] * props_b['charge']
            if charge_product < 0:  # Opposite charges attract
                attraction += 0.8
        
        # Check energy compatibility
        if 'energy_level' in props_a and 'energy_level' in props_b:
            energy_diff = abs(props_a['energy_level'] - props_b['energy_level'])
            if energy_diff < 0.3:  # Similar energy levels
                attraction += 0.4
        
        return min(attraction, 1.0)
    
    def _check_repulsion(self, props_a: Dict, props_b: Dict) -> float:
        """Check for repulsion between components"""
        repulsion = 0.0
        
        # Check charge repulsion
        if 'charge' in props_a and 'charge' in props_b:
            charge_product = props_a['charge'] * props_b['charge']
            if charge_product > 0:  # Same charges repel
                repulsion += 0.7 * abs(charge_product)
        
        # Check incompatible properties
        if 'spin' in props_a and 'spin' in props_b:
            if props_a['spin'] == props_b['spin']:
                # Pauli exclusion principle - same spin repel
                repulsion += 0.6
        
        return min(repulsion, 1.0)
    
    def simulate_interaction(
        self,
        component_a: Dict,
        component_b: Dict,
        time_steps: int = 100
    ) -> List[Dict]:
        """
        Simulate natural interaction over time.
        
        Returns:
            List of interaction states over time
        """
        states = []
        distance = component_a.get('distance', 10.0)
        
        for step in range(time_steps):
            # Calculate current interaction
            interaction_type, strength = self.calculate_interaction_strength(
                component_a,
                component_b,
                distance
            )
            
            # Update distance based on interaction
            if interaction_type == InteractionType.ATTRACTION:
                distance *= (1.0 - 0.1 * strength)
            elif interaction_type == InteractionType.REPULSION:
                distance *= (1.0 + 0.1 * strength)
            
            state = {
                'step': step,
                'distance': distance,
                'interaction_type': interaction_type.value,
                'strength': strength,
                'effortless': strength > 0.5,  # High strength = effortless
            }
            states.append(state)
            
            # Natural stopping condition - stable state reached
            if len(states) > 10:
                recent_distances = [s['distance'] for s in states[-10:]]
                if max(recent_distances) - min(recent_distances) < 0.01:
                    break
        
        return states
    
    def find_natural_equilibrium(
        self,
        components: List[Dict],
        max_iterations: int = 1000
    ) -> Dict:
        """
        Find the natural equilibrium state for multiple components.
        
        This is where the system naturally settles without external force.
        """
        current_config = [c.copy() for c in components]
        energy_history = []
        
        for iteration in range(max_iterations):
            total_energy = 0.0
            
            # Calculate all pairwise interactions
            for i in range(len(current_config)):
                for j in range(i + 1, len(current_config)):
                    comp_a = current_config[i]
                    comp_b = current_config[j]
                    
                    distance = self._calculate_distance(comp_a, comp_b)
                    int_type, strength = self.calculate_interaction_strength(
                        comp_a,
                        comp_b,
                        distance
                    )
                    
                    # Accumulate energy
                    if int_type == InteractionType.ATTRACTION:
                        total_energy -= strength  # Attraction lowers energy
                    elif int_type == InteractionType.REPULSION:
                        total_energy += strength  # Repulsion raises energy
            
            energy_history.append(total_energy)
            
            # Check for equilibrium (energy stabilized)
            if len(energy_history) > 20:
                recent_energies = energy_history[-20:]
                energy_variance = np.var(recent_energies)
                if energy_variance < 0.001:
                    # Equilibrium reached
                    return {
                        'configuration': current_config,
                        'energy': total_energy,
                        'iterations': iteration,
                        'stable': True,
                        'effortless': True  # Natural equilibrium is effortless
                    }
        
        return {
            'configuration': current_config,
            'energy': total_energy,
            'iterations': max_iterations,
            'stable': False,
            'effortless': False
        }
    
    def _calculate_distance(self, comp_a: Dict, comp_b: Dict) -> float:
        """Calculate distance between two components"""
        if 'position' in comp_a and 'position' in comp_b:
            pos_a = np.array(comp_a['position'])
            pos_b = np.array(comp_b['position'])
            return np.linalg.norm(pos_a - pos_b)
        return comp_a.get('distance', 5.0)


def demonstrate_interaction_dynamics():
    """Demonstrate natural interaction dynamics"""
    print("=== Interaction Dynamics Demonstration ===")
    print()
    
    dynamics = InteractionDynamics()
    
    # Example 1: Attraction (opposite charges)
    print("1. Natural Attraction (opposite charges):")
    comp_a = {'charge': 1.0, 'energy_level': 0.5, 'distance': 10.0}
    comp_b = {'charge': -1.0, 'energy_level': 0.6}
    
    interaction_type, strength = dynamics.calculate_interaction_strength(
        comp_a, comp_b, 5.0
    )
    print(f"   Interaction: {interaction_type.value}")
    print(f"   Strength: {strength:.3f}")
    print(f"   Effortless: {strength > 0.5}")
    print()
    
    # Example 2: Resonance (similar frequencies)
    print("2. Natural Resonance (similar frequencies):")
    comp_c = {'frequency': 440.0}  # A note
    comp_d = {'frequency': 442.0}  # Nearly same frequency
    
    interaction_type, strength = dynamics.calculate_interaction_strength(
        comp_c, comp_d, 2.0
    )
    print(f"   Interaction: {interaction_type.value}")
    print(f"   Strength: {strength:.3f}")
    print(f"   Effortless: {strength > 0.5}")
    print()
    
    # Example 3: Repulsion (same charges)
    print("3. Natural Repulsion (same charges):")
    comp_e = {'charge': 1.0, 'spin': 0.5}
    comp_f = {'charge': 1.0, 'spin': 0.5}
    
    interaction_type, strength = dynamics.calculate_interaction_strength(
        comp_e, comp_f, 3.0
    )
    print(f"   Interaction: {interaction_type.value}")
    print(f"   Strength: {strength:.3f}")
    print(f"   Effortless: {strength > 0.5}")
    print()
    
    print("All interactions happen naturally without external force.")
    print("Zwanglose Stabilität in action!")


if __name__ == "__main__":
    demonstrate_interaction_dynamics()
