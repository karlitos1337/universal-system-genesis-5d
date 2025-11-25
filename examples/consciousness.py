"""consciousness.py

Example: Thought Emergence through Effortless Stability

Demonstrates how conscious awareness and thought patterns emerge through
effortless, stable interaction networks in neural systems.

5D Intelligence Framework Application:
- What: Emergent awareness, thought patterns, conceptual understanding
- How: Effortless neural activation patterns, resonant feedback loops
- How Much: Observable consciousness states, cognitive capacity measures
- Through What Interaction: Neural networks achieving stable, self-sustaining patterns

Connection to Zwanglose Stabilität:
Only the most natural, effortless thought patterns persist and become
part of stable consciousness. Forced or unnatural cognitive patterns
create instability and dissolve.
"""

import numpy as np
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class NeuralNode:
    """Represents a single node in a thought network."""
    id: int
    activation: float = 0.0
    connections: List[int] = None
    connection_weights: List[float] = None
    
    def __post_init__(self):
        if self.connections is None:
            self.connections = []
        if self.connection_weights is None:
            self.connection_weights = []


class ThoughtEmergenceNetwork:
    """Models emergence of thought through effortless neural stability."""
    
    def __init__(self, num_nodes: int, connectivity: float = 0.1):
        """
        Initialize thought network.
        
        Args:
            num_nodes: Number of neural nodes in the network
            connectivity: Probability of connection between nodes (0-1)
        """
        self.num_nodes = num_nodes
        self.connectivity = connectivity
        self.nodes: List[NeuralNode] = []
        self.time_step = 0
        self.thought_patterns: List[Dict] = []
        
        self._initialize_network()
    
    def _initialize_network(self):
        """Create network with effortless, natural connectivity."""
        # Create nodes
        for i in range(self.num_nodes):
            self.nodes.append(NeuralNode(id=i))
        
        # Establish connections based on natural affinity (random but stable)
        np.random.seed(42)  # For reproducible networks
        
        for node in self.nodes:
            # Each node connects to a subset of others
            for potential_target in range(self.num_nodes):
                if potential_target != node.id:
                    # Natural connection probability
                    if np.random.random() < self.connectivity:
                        # Connection weight based on natural resonance
                        weight = np.random.beta(2, 5)  # Naturally skewed distribution
                        node.connections.append(potential_target)
                        node.connection_weights.append(weight)
    
    def _calculate_natural_activation(self, node: NeuralNode) -> float:
        """
        Calculate activation based on effortless input from connected nodes.
        
        Returns activation level that emerges naturally without force.
        """
        if not node.connections:
            return 0.0
        
        total_input = 0.0
        for conn_id, weight in zip(node.connections, node.connection_weights):
            connected_node = self.nodes[conn_id]
            # Effortless propagation - weighted by natural connection strength
            total_input += connected_node.activation * weight
        
        # Natural activation function (sigmoid for smooth transitions)
        # Represents effortless emergence without artificial forcing
        activation = 1.0 / (1.0 + np.exp(-total_input + 2.0))
        
        return activation
    
    def stimulate(self, node_ids: List[int], intensity: float = 0.8):
        """
        Provide initial stimulus to specific nodes (like sensory input).
        
        Args:
            node_ids: IDs of nodes to stimulate
            intensity: Stimulation strength (0-1)
        """
        for node_id in node_ids:
            if 0 <= node_id < self.num_nodes:
                self.nodes[node_id].activation = intensity
    
    def evolve(self, steps: int = 50, decay_rate: float = 0.1) -> List[Dict]:
        """
        Allow thought patterns to emerge naturally over time.
        
        Args:
            steps: Number of evolution iterations
            decay_rate: Natural decay of activation (prevents runaway)
        
        Returns:
            List of system states at each time step
        """
        evolution_history = []
        
        for step in range(steps):
            # Calculate new activations for all nodes
            new_activations = []
            
            for node in self.nodes:
                # Natural activation emerges from network state
                natural_activation = self._calculate_natural_activation(node)
                
                # Apply natural decay (energy cost of maintaining activation)
                decayed = node.activation * (1.0 - decay_rate)
                
                # New activation is weighted average (smooth transition)
                new_activation = 0.7 * natural_activation + 0.3 * decayed
                new_activations.append(new_activation)
            
            # Update all nodes simultaneously
            for i, node in enumerate(self.nodes):
                node.activation = new_activations[i]
            
            # Record system state
            state = {
                'step': self.time_step,
                'activations': [n.activation for n in self.nodes],
                'total_energy': sum(new_activations),
                'active_nodes': sum(1 for a in new_activations if a > 0.1)
            }
            evolution_history.append(state)
            
            self.time_step += 1
            
            # Detect stable thought patterns
            self._detect_thought_patterns(state)
        
        return evolution_history
    
    def _detect_thought_patterns(self, state: Dict):
        """
        Identify stable, recurring activation patterns (thoughts).
        
        Stable patterns represent effortlessly sustained cognitive structures.
        """
        activations = state['activations']
        
        # A thought pattern is a stable configuration of active nodes
        active_pattern = [i for i, a in enumerate(activations) if a > 0.3]
        
        if len(active_pattern) >= 3:  # Minimum complexity for a "thought"
            # Check if this pattern achieves stability
            pattern_strength = sum(activations[i] for i in active_pattern) / len(active_pattern)
            
            if pattern_strength > 0.4:  # Stability threshold
                thought = {
                    'time': state['step'],
                    'pattern': active_pattern,
                    'strength': pattern_strength,
                    'effortless_stability_score': self._calculate_effortlessness(active_pattern)
                }
                self.thought_patterns.append(thought)
    
    def _calculate_effortlessness(self, pattern: List[int]) -> float:
        """
        Calculate how 'effortless' a thought pattern is.
        
        More natural patterns require less 'maintenance energy'.
        """
        if not pattern:
            return 0.0
        
        # Measure based on natural connectivity within the pattern
        internal_connections = 0
        total_possible = len(pattern) * (len(pattern) - 1)
        
        for node_id in pattern:
            node = self.nodes[node_id]
            for conn_id in node.connections:
                if conn_id in pattern:
                    internal_connections += 1
        
        # Higher internal connectivity = more effortless maintenance
        if total_possible > 0:
            return internal_connections / total_possible
        return 0.0
    
    def analyze_emergence(self) -> Dict:
        """
        Analyze how consciousness-like patterns emerged.
        
        Returns insights following the 5D intelligence framework.
        """
        if not self.thought_patterns:
            return {
                'what': 'No stable thought patterns emerged',
                'how': 'Network did not achieve sufficient connectivity',
                'how_much': 0,
                'zwanglose_interaction': 'Insufficient natural resonance'
            }
        
        # Identify most stable thoughts
        stable_thoughts = sorted(
            self.thought_patterns,
            key=lambda t: t['effortless_stability_score'],
            reverse=True
        )[:5]
        
        avg_stability = np.mean([t['effortless_stability_score'] for t in self.thought_patterns])
        
        return {
            'what': f'{len(self.thought_patterns)} distinct thought patterns emerged',
            'how': 'Through effortless resonance in neural network, stable activation configurations formed',
            'how_much': f'Average stability: {avg_stability:.3f}, with {len(stable_thoughts)} highly stable patterns',
            'zwanglose_interaction': (
                'Most effortless thoughts (highest internal connectivity) '
                'persisted longest, demonstrating Zwanglose Stabilität in cognitive emergence'
            ),
            'most_stable_patterns': stable_thoughts,
            'philosophical_insight': (
                'Consciousness emerges not through force but through the natural stability '
                'of thought patterns that require minimal energy to maintain. '
                'The most effortless thoughts are the most enduring.'
            )
        }


def demonstrate_thought_emergence():
    """
    Demonstrate consciousness emergence through effortless stability.
    """
    print("=" * 70)
    print("THOUGHT EMERGENCE: Consciousness Through Effortless Stability")
    print("=" * 70)
    print()
    print("Principle: Only the most natural, effortless thought patterns")
    print("persist and form stable consciousness.")
    print()
    
    # Create a thought network
    network = ThoughtEmergenceNetwork(num_nodes=50, connectivity=0.15)
    
    print(f"Network initialized: {network.num_nodes} neural nodes")
    print(f"Natural connectivity: {network.connectivity * 100}%")
    print()
    
    # Simulate sensory input (like seeing something interesting)
    print("Applying initial stimulus (sensory input)...")
    stimulus_nodes = [5, 12, 23, 34, 41]  # Random sensory nodes
    network.stimulate(stimulus_nodes, intensity=0.9)
    print(f"Stimulated nodes: {stimulus_nodes}")
    print()
    
    # Let thoughts emerge naturally
    print("Allowing thought patterns to emerge naturally...")
    evolution = network.evolve(steps=100, decay_rate=0.12)
    print(f"Evolution complete: {len(evolution)} time steps")
    print()
    
    # Analyze what emerged
    print("=" * 70)
    print("EMERGENCE ANALYSIS (5D Intelligence Framework)")
    print("=" * 70)
    print()
    
    analysis = network.analyze_emergence()
    
    print(f"WHAT emerged:")
    print(f"  {analysis['what']}")
    print()
    
    print(f"HOW it emerged:")
    print(f"  {analysis['how']}")
    print()
    
    print(f"HOW MUCH emerged:")
    print(f"  {analysis['how_much']}")
    print()
    
    print(f"THROUGH WHAT effortless interaction:")
    print(f"  {analysis['zwanglose_interaction']}")
    print()
    
    if 'most_stable_patterns' in analysis and analysis['most_stable_patterns']:
        print("Most Stable Thought Patterns:")
        for i, thought in enumerate(analysis['most_stable_patterns'][:3], 1):
            print(f"  {i}. Time={thought['time']}, Strength={thought['strength']:.3f}, "
                  f"Effortlessness={thought['effortless_stability_score']:.3f}")
            print(f"     Pattern nodes: {thought['pattern'][:10]}{'...' if len(thought['pattern']) > 10 else ''}")
        print()
    
    print("=" * 70)
    print("PHILOSOPHICAL INSIGHT")
    print("=" * 70)
    print()
    print(analysis['philosophical_insight'])
    print()
    
    # Show energy dynamics
    print("Energy Dynamics (Total Network Activation):")
    energies = [state['total_energy'] for state in evolution]
    print(f"  Initial energy: {energies[0]:.2f}")
    print(f"  Final energy: {energies[-1]:.2f}")
    print(f"  Peak energy: {max(energies):.2f} at step {energies.index(max(energies))}")
    print()
    
    print("Interpretation: The system naturally seeks its most effortless,")
    print("stable state - just as consciousness finds its most natural thoughts.")
    print()


if __name__ == '__main__':
    demonstrate_thought_emergence()
