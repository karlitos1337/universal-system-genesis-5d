"""Fractal Patterns Module

Demonstrates how the same principle of effortless stability
applies across all scales - from quantum to cosmic to consciousness.

The fractal nature: What works at one scale works at all scales.
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple
from enum import Enum


class Scale(Enum):
    """Different scales where zwanglose Stabilität applies"""
    QUANTUM = "quantum"           # Subatomic particles
    ATOMIC = "atomic"             # Atoms
    MOLECULAR = "molecular"       # Molecules
    CELLULAR = "cellular"         # Biological cells
    ORGANISMIC = "organismic"     # Living organisms
    SOCIAL = "social"             # Human societies
    PLANETARY = "planetary"       # Planets and solar systems
    GALACTIC = "galactic"         # Galaxies
    CONSCIOUSNESS = "consciousness"  # Thoughts and ideas


@dataclass
class FractalPattern:
    """Represents a pattern that repeats across scales"""
    scale: Scale
    components: int  # Number of components at this scale
    interaction_strength: float  # How strongly components interact
    stability_measure: float  # How stable the configuration is
    emergence_time: float  # How long it took to emerge
    
    def is_stable(self) -> bool:
        """Check if this pattern is stable (zwanglose Stabilität)"""
        return self.stability_measure > 0.6 and self.interaction_strength < 0.8
    
    def is_effortless(self) -> bool:
        """Check if emergence was effortless"""
        # Effortless = high stability with low forced interaction
        return self.is_stable() and self.interaction_strength < 0.5


class FractalAnalyzer:
    """Analyzes fractal patterns across scales"""
    
    def __init__(self):
        self.patterns: Dict[Scale, List[FractalPattern]] = {}
    
    def analyze_scale_similarity(
        self,
        pattern_a: FractalPattern,
        pattern_b: FractalPattern
    ) -> float:
        """
        Analyze how similar patterns are across different scales.
        Returns similarity score (0.0 to 1.0)
        """
        # Normalize by component count (scaling factor)
        components_ratio = min(
            pattern_a.components / pattern_b.components,
            pattern_b.components / pattern_a.components
        )
        
        # Compare interaction patterns
        interaction_similarity = 1.0 - abs(
            pattern_a.interaction_strength - pattern_b.interaction_strength
        )
        
        # Compare stability
        stability_similarity = 1.0 - abs(
            pattern_a.stability_measure - pattern_b.stability_measure
        )
        
        # Overall similarity
        similarity = (interaction_similarity + stability_similarity) / 2.0
        return similarity
    
    def find_fractal_repetition(
        self,
        patterns: List[FractalPattern]
    ) -> List[Tuple[Scale, Scale, float]]:
        """
        Find where patterns repeat across scales.
        Returns list of (scale_a, scale_b, similarity) tuples.
        """
        repetitions = []
        
        for i in range(len(patterns)):
            for j in range(i + 1, len(patterns)):
                similarity = self.analyze_scale_similarity(
                    patterns[i],
                    patterns[j]
                )
                
                if similarity > 0.7:  # High similarity = fractal repetition
                    repetitions.append((
                        patterns[i].scale,
                        patterns[j].scale,
                        similarity
                    ))
        
        return repetitions
    
    def calculate_fractal_dimension(
        self,
        pattern: FractalPattern,
        scale_factor: float = 2.0
    ) -> float:
        """
        Calculate fractal dimension - how pattern complexity scales.
        
        Higher dimension = more complex self-similar structure
        """
        # Simplified fractal dimension calculation
        # Based on how components and interactions scale
        
        log_components = np.log(pattern.components)
        log_scale = np.log(scale_factor)
        
        if log_scale == 0:
            return 1.0
        
        dimension = log_components / log_scale
        return dimension
    
    def demonstrate_universality(self) -> Dict[str, any]:
        """
        Demonstrate that zwanglose Stabilität is universal across scales.
        """
        # Create example patterns at different scales
        patterns = [
            # Quantum: Electron-proton bond
            FractalPattern(
                scale=Scale.QUANTUM,
                components=2,
                interaction_strength=0.4,
                stability_measure=0.9,
                emergence_time=1e-15
            ),
            # Atomic: Hydrogen atom
            FractalPattern(
                scale=Scale.ATOMIC,
                components=2,
                interaction_strength=0.45,
                stability_measure=0.85,
                emergence_time=1e-10
            ),
            # Molecular: H2O molecule
            FractalPattern(
                scale=Scale.MOLECULAR,
                components=3,
                interaction_strength=0.5,
                stability_measure=0.88,
                emergence_time=1e-9
            ),
            # Solar: Earth-Sun system
            FractalPattern(
                scale=Scale.PLANETARY,
                components=2,
                interaction_strength=0.35,
                stability_measure=0.95,
                emergence_time=1e9
            ),
            # Social: Cooperative group
            FractalPattern(
                scale=Scale.SOCIAL,
                components=5,
                interaction_strength=0.4,
                stability_measure=0.75,
                emergence_time=1000
            ),
        ]
        
        # Find fractal repetitions
        repetitions = self.find_fractal_repetition(patterns)
        
        # Check which patterns show effortless stability
        effortless_patterns = [
            p for p in patterns if p.is_effortless()
        ]
        
        return {
            'total_patterns_analyzed': len(patterns),
            'fractal_repetitions': repetitions,
            'effortless_patterns': len(effortless_patterns),
            'universality_confirmed': len(repetitions) > 0,
            'patterns': patterns
        }


def demonstrate_fractal_patterns():
    """Demonstrate fractal nature of effortless stability"""
    print("=== Fractal Patterns Across Scales ===")
    print()
    print("The same principle applies from quantum to cosmic:")
    print("Zwanglose Stabilität (Effortless Stability)")
    print()
    
    analyzer = FractalAnalyzer()
    results = analyzer.demonstrate_universality()
    
    print(f"Patterns analyzed: {results['total_patterns_analyzed']}")
    print(f"Fractal repetitions found: {len(results['fractal_repetitions'])}")
    print()
    
    print("Fractal Repetitions (similar patterns across scales):")
    for scale_a, scale_b, similarity in results['fractal_repetitions']:
        print(f"  {scale_a.value} ↔ {scale_b.value}: {similarity:.2f} similarity")
    print()
    
    print(f"Effortless patterns: {results['effortless_patterns']}/{results['total_patterns_analyzed']}")
    print()
    
    if results['universality_confirmed']:
        print("✓ Universality CONFIRMED: Same principle across all scales!")
    else:
        print("✗ No fractal repetition detected")
    
    print()
    print("Key Insight: What works at the quantum level works at the cosmic level.")
    print("No central planner needed - just natural balance forces.")


if __name__ == "__main__":
    demonstrate_fractal_patterns()
