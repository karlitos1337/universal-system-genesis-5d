#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STABILITY PRINCIPLE - Core Module
===================================

Effortless Stability through Natural Interactions

Die erste Verbindung von Teilchen war eine zwanglose, die nur so lange dauerte,
wie die Stabilität es ihr gewährte.

This module implements the core principle: Systems form through effortless
interactions that persist as long as they provide stability.
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple, Optional
import math


@dataclass
class SystemState:
    """Represents the state of a system at a given time"""
    energy: float
    entropy: float
    stability_score: float
    configuration: np.ndarray
    timestamp: float
    
    def is_stable(self, threshold: float = 0.5) -> bool:
        """Check if system is stable based on stability score"""
        return self.stability_score >= threshold


@dataclass
class Interaction:
    """Represents an interaction between system components"""
    participants: Tuple[int, int]
    strength: float
    energy_change: float
    natural: bool  # True if effortless, False if forced
    
    def contributes_to_stability(self) -> bool:
        """Natural interactions that lower energy contribute to stability"""
        return self.natural and self.energy_change < 0


class StabilityPrinciple:
    """
    Core implementation of the Effortless Stability Principle.
    
    Systems evolve through natural interactions, persisting as long as
    stability is maintained. No central control needed.
    """
    
    def __init__(self, system_size: int = 100, temperature: float = 1.0):
        self.system_size = system_size
        self.temperature = temperature
        self.history: List[SystemState] = []
        
    def calculate_stability(self, energy: float, entropy: float, 
                          num_stable_interactions: int,
                          total_interactions: int) -> float:
        """
        Calculate stability score based on:
        - Energy (lower = more stable)
        - Entropy (balanced = more stable)
        - Ratio of stable interactions
        
        Returns stability score between 0 and 1
        """
        # Energy contribution (normalized, inverted)
        energy_stability = 1.0 / (1.0 + abs(energy))
        
        # Entropy contribution (peaked at moderate entropy)
        optimal_entropy = 0.5
        entropy_stability = 1.0 - abs(entropy - optimal_entropy)
        
        # Interaction contribution
        if total_interactions > 0:
            interaction_stability = num_stable_interactions / total_interactions
        else:
            interaction_stability = 0.0
        
        # Combined stability (weighted average)
        stability = (0.4 * energy_stability + 
                    0.3 * entropy_stability + 
                    0.3 * interaction_stability)
        
        return max(0.0, min(1.0, stability))
    
    def evaluate_interaction(self, state_before: SystemState, 
                           state_after: SystemState,
                           forced: bool = False) -> Interaction:
        """
        Evaluate whether an interaction is natural (effortless) and 
        contributes to stability.
        
        Natural interactions:
        - Reduce system energy
        - Increase or maintain stability
        - Are not forced
        """
        energy_change = state_after.energy - state_before.energy
        natural = (not forced and 
                  energy_change <= 0 and 
                  state_after.stability_score >= state_before.stability_score)
        
        return Interaction(
            participants=(0, 1),  # Simplified
            strength=abs(energy_change),
            energy_change=energy_change,
            natural=natural
        )
    
    def simulate_evolution(self, initial_state: SystemState, 
                         num_steps: int = 100) -> List[SystemState]:
        """
        Simulate system evolution following effortless stability principle.
        
        Systems self-organize through natural interactions, finding stable
        configurations without central control.
        """
        states = [initial_state]
        current_state = initial_state
        
        for step in range(num_steps):
            # Attempt random natural interaction
            energy_perturbation = np.random.randn() * self.temperature
            new_energy = current_state.energy + energy_perturbation
            
            # Calculate new entropy (simplified)
            new_entropy = self._calculate_entropy(new_energy)
            
            # Calculate new stability
            new_stability = self.calculate_stability(
                energy=new_energy,
                entropy=new_entropy,
                num_stable_interactions=len([s for s in states if s.is_stable()]),
                total_interactions=len(states)
            )
            
            # Create new state
            new_state = SystemState(
                energy=new_energy,
                entropy=new_entropy,
                stability_score=new_stability,
                configuration=current_state.configuration.copy(),
                timestamp=step
            )
            
            # Evaluate interaction
            interaction = self.evaluate_interaction(current_state, new_state)
            
            # Accept state if interaction is natural (effortless)
            # OR if energy is lower (downhill always accepted)
            if interaction.natural or new_energy < current_state.energy:
                current_state = new_state
                states.append(new_state)
            else:
                # Reject forced/uphill interactions (no external forcing)
                states.append(current_state)
        
        self.history = states
        return states
    
    def _calculate_entropy(self, energy: float) -> float:
        """
        Calculate entropy based on energy.
        Higher energy = higher entropy (more disorder)
        """
        return 1.0 / (1.0 + math.exp(-energy))
    
    def find_stable_configurations(self, threshold: float = 0.7) -> List[SystemState]:
        """
        Find all stable configurations in the system history.
        
        These represent 'eternal' or 'eternal-seeming' stability -
        configurations that persist because they naturally provide stability.
        """
        return [state for state in self.history 
                if state.is_stable(threshold)]
    
    def get_average_lifetime(self, stable_configs: List[SystemState]) -> float:
        """
        Calculate average lifetime of stable configurations.
        
        Configurations persist 'as long as stability permits' -
        this measures that duration.
        """
        if not stable_configs:
            return 0.0
        
        lifetimes = []
        current_start = None
        
        for i, state in enumerate(self.history):
            if state in stable_configs:
                if current_start is None:
                    current_start = i
            else:
                if current_start is not None:
                    lifetimes.append(i - current_start)
                    current_start = None
        
        # Handle case where stability continues to end
        if current_start is not None:
            lifetimes.append(len(self.history) - current_start)
        
        return np.mean(lifetimes) if lifetimes else 0.0


def demonstrate_effortless_stability():
    """
    Demonstration: System finds stable configurations naturally,
    without external forcing.
    """
    print("=" * 80)
    print("EFFORTLESS STABILITY PRINCIPLE - Demonstration")
    print("=" * 80)
    print()
    print("Simulating system evolution through natural interactions...")
    print()
    
    # Initialize system
    principle = StabilityPrinciple(temperature=0.5)
    initial = SystemState(
        energy=10.0,
        entropy=0.8,
        stability_score=0.3,
        configuration=np.random.randn(10),
        timestamp=0.0
    )
    
    # Evolve system
    states = principle.simulate_evolution(initial, num_steps=200)
    
    # Analyze results
    stable_configs = principle.find_stable_configurations(threshold=0.7)
    avg_lifetime = principle.get_average_lifetime(stable_configs)
    
    print(f"Total states explored: {len(states)}")
    print(f"Stable configurations found: {len(stable_configs)}")
    print(f"Stability rate: {len(stable_configs)/len(states)*100:.1f}%")
    print(f"Average stability lifetime: {avg_lifetime:.1f} timesteps")
    print()
    
    # Energy evolution
    final_energy = states[-1].energy
    energy_change = final_energy - initial.energy
    print(f"Initial energy: {initial.energy:.2f}")
    print(f"Final energy: {final_energy:.2f}")
    print(f"Energy change: {energy_change:.2f}")
    print()
    
    # Stability evolution
    final_stability = states[-1].stability_score
    stability_change = final_stability - initial.stability_score
    print(f"Initial stability: {initial.stability_score:.2f}")
    print(f"Final stability: {final_stability:.2f}")
    print(f"Stability change: {stability_change:+.2f}")
    print()
    
    if energy_change < 0 and stability_change > 0:
        print("✓ System naturally evolved to lower energy and higher stability")
        print("✓ No external forcing needed - effortless stability achieved")
    
    print()
    print("=" * 80)
    print("Conclusion: Systems self-organize through natural interactions,")
    print("finding stable configurations that persist as long as they")
    print("provide stability. No central control required.")
    print("=" * 80)


if __name__ == "__main__":
    demonstrate_effortless_stability()
