import torch
import torch.nn as nn
from typing import List


class Solution:

    def detect_dead_neurons(self, model: nn.Module, x: torch.Tensor) -> List[float]:
        dead_fractions = []

        with torch.no_grad():

            current = x

            for layer in model:
                current = layer(current)

                if isinstance(layer, nn.ReLU):

                    dead_neurons = (current == 0).all(dim=0)

                    dead_fraction = dead_neurons.float().mean().item()

                    dead_fractions.append(round(dead_fraction, 4))

        return dead_fractions

    def suggest_fix(self, dead_fractions: List[float]) -> str:

        if any(df > 0.5 for df in dead_fractions):
            return "use_leaky_relu"

        if dead_fractions[0] > 0.3:
            return "reinitialize"

        increasing = all(
            dead_fractions[i] < dead_fractions[i + 1]
            for i in range(len(dead_fractions) - 1)
        )

        if increasing and dead_fractions[-1] > 0.1:
            return "reduce_learning_rate"

        if max(dead_fractions) < 0.1:
            return "healthy"

        return "healthy"