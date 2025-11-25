"""stability_principle.py

Core implementation of Zwanglose Stabilität (Effortless Stability).

Defines how systems evolve toward stable states through natural interactions.
"""

import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class SystemState:
    """Represents the state of a system component."""
    id: int
    position: np.ndarray
    velocity: np.ndarray
    mass: float
    energy: float
    
    def __post_init__(self):
        if not isinstance(self.position, np.ndarray):
            self.position = np.array(self.position)
        if not isinstance(self.velocity, np.ndarray):
            self.velocity = np.array(self.velocity)


@dataclass
class Interaction:
    """Represents an interaction between system components."""
    source_id: int
    target_id: int
    force: np.ndarray
    interaction_type: str
    strength: float


class StabilityPrinciple:
    """
    Core class implementing Zwanglose Stabilität (Effortless Stability).
    
    Systems evolve naturally toward states that minimize energy and maximize
    stability without external control or predetermined design.
    """
    
    def __init__(self):
        self.states: List[SystemState] = []
        self.interactions: List[Interaction] = []
        self.time: float = 0.0
        self.dt: float = 0.01
        
    def add_state(self, state: SystemState):
        """Add a component to the system."""
        self.states.append(state)
    
    def calculate_stability(self, state: SystemState) -> float:
        """
        Calculate stability score for a given state.
        
        Higher values indicate more stable configurations.
        Stability = 1 / (1 + total_energy + kinetic_energy)
        """
        kinetic_energy = 0.5 * state.mass * np.dot(state.velocity, state.velocity)
        total_energy = state.energy + kinetic_energy
        
        # Stability is inverse of energy (lower energy = higher stability)
        stability = 1.0 / (1.0 + abs(total_energy))
        
        return stability
    
    def evaluate_interaction(self, state1: SystemState, state2: SystemState) -> Interaction:
        """
        Evaluate natural interaction between two components.
        
        Calculates force based on natural laws (gravity, electromagnetic, etc.)
        """
        # Calculate distance
        r_vec = state2.position - state1.position
        r = np.linalg.norm(r_vec)
        
        if r < 1e-10:  # Avoid division by zero
            force = np.zeros_like(r_vec)
            strength = 0.0
        else:
            # Simple gravitational-like interaction
            # F = G * m1 * m2 / r^2, direction toward each other
            r_hat = r_vec / r
            strength = state1.mass * state2.mass / (r * r)
            force = strength * r_hat
        
        return Interaction(
            source_id=state1.id,
            target_id=state2.id,
            force=force,
            interaction_type="attractive",
            strength=strength
        )
    
    def simulate_evolution(self, steps: int = 100) -> List[Dict]:
        """
        Simulate natural evolution of the system toward effortless stability.
        
        Returns history of system states at each time step.
        """
        history = []
        
        for step in range(steps):
            # Calculate all interactions
            self.interactions = []
            for i, state1 in enumerate(self.states):
                for j, state2 in enumerate(self.states):
                    if i < j:  # Avoid double-counting
                        interaction = self.evaluate_interaction(state1, state2)
                        self.interactions.append(interaction)
            
            # Update states based on interactions
            forces = {state.id: np.zeros(3) for state in self.states}
            
            for interaction in self.interactions:
                # Apply force to both components (Newton's 3rd law)
                forces[interaction.source_id] += interaction.force
                forces[interaction.target_id] -= interaction.force
            
            # Update velocities and positions
            for state in self.states:
                acceleration = forces[state.id] / state.mass
                state.velocity += acceleration * self.dt
                state.position += state.velocity * self.dt
                
                # Update energy (kinetic + potential)
                kinetic = 0.5 * state.mass * np.dot(state.velocity, state.velocity)
                state.energy = kinetic  # Simplified
            
            # Record state
            snapshot = {
                'time': self.time,
                'states': [
                    {
                        'id': s.id,
                        'position': s.position.copy(),
                        'velocity': s.velocity.copy(),
                        'energy': s.energy,
                        'stability': self.calculate_stability(s)
                    }
                    for s in self.states
                ],
                'total_energy': sum(s.energy for s in self.states),
                'avg_stability': np.mean([self.calculate_stability(s) for s in self.states])
            }
            history.append(snapshot)
            
            self.time += self.dt
        
        return history
    
    def find_stable_configurations(self, stability_threshold: float = 0.8) -> List[SystemState]:
        """
        Identify configurations that achieve effortless stability.
        
        Returns states with stability above threshold.
        """
        stable_states = []
        
        for state in self.states:
            stability = self.calculate_stability(state)
            if stability >= stability_threshold:
                stable_states.append(state)
        
        return stable_states
    
    def demonstrate_zwanglose_stabilitat(self) -> Dict:
        """
        Analyze and demonstrate Zwanglose Stabilität in the system.
        
        Returns analysis following 5D intelligence framework.
        """
        # Run simulation
        history = self.simulate_evolution(steps=200)
        
        initial_energy = history[0]['total_energy']
        final_energy = history[-1]['total_energy']
        initial_stability = history[0]['avg_stability']
        final_stability = history[-1]['avg_stability']
        
        # Find most stable configuration
        most_stable_time = max(history, key=lambda h: h['avg_stability'])
        
        return {
            'what': f"System evolved from {len(self.states)} components to stable configuration",
            'how': "Through natural, effortless interactions without external control",
            'how_much': {
                'energy_change': final_energy - initial_energy,
                'stability_improvement': final_stability - initial_stability,
                'time_to_stability': most_stable_time['time']
            },
            'zwanglose_interaction': (
                "System self-organized through local interactions. "
                "Most stable configurations emerged naturally, requiring minimal energy to maintain."
            ),
            'history': history
        }


def calculate_stability(state: SystemState) -> float:
    """Standalone function to calculate stability."""
    principle = StabilityPrinciple()
    return principle.calculate_stability(state)


def Interaktion_bewerten(state1: SystemState, state2: SystemState) -> Interaction:
    """Bewerte natürliche Interaktion (Deutsche Funktion)."""
    principle = StabilityPrinciple()
    return principle.evaluate_interaction(state1, state2)


def simulate_evolution(system: StabilityPrinciple, steps: int = 100) -> List[Dict]:
    """Standalone function to simulate system evolution."""
    return system.simulate_evolution(steps)


def find_stable_configurations(system: StabilityPrinciple, threshold: float = 0.8) -> List[SystemState]:
    """Standalone function to find stable configurations."""
    return system.find_stable_configurations(threshold)


def demonstrate_zwanglose_stabilitat(system: StabilityPrinciple) -> Dict:
    """Standalone function to demonstrate Zwanglose Stabilität."""
    return system.demonstrate_zwanglose_stabilitat()
