import torch
import torch.nn as nn
from typing import List, Dict


class Solution:

    def compute_activation_stats(self, model: nn.Module, x: torch.Tensor) -> List[Dict[str, float]]:
        stats = []

        with torch.no_grad():
            current = x

            for layer in model:
                current = layer(current)

                if isinstance(layer, nn.Linear):

                    mean = round(current.mean().item(), 4)
                    std = round(current.std().item(), 4)

                    dead_neurons = (current <= 0).all(dim=0).float().mean().item()

                    stats.append({
                        "mean": mean,
                        "std": round(dead_neurons * 0 + std, 4),
                        "dead_fraction": round(dead_neurons, 4)
                    })

        return stats

    def compute_gradient_stats(self, model: nn.Module, x: torch.Tensor, y: torch.Tensor) -> List[Dict[str, float]]:
        stats = []

        model.zero_grad()

        criterion = nn.MSELoss()

        predictions = model(x)

        loss = criterion(predictions, y)

        loss.backward()

        for layer in model:

            if isinstance(layer, nn.Linear):

                grad = layer.weight.grad

                stats.append({
                    "mean": round(grad.mean().item(), 4),
                    "std": round(grad.std().item(), 4),
                    "norm": round(torch.norm(grad).item(), 4)
                })

        return stats

    def diagnose(self, activation_stats: List[Dict[str, float]], gradient_stats: List[Dict[str, float]]) -> str:

        for stat in activation_stats:
            if stat["dead_fraction"] > 0.5:
                return "dead_neurons"

        for stat in gradient_stats:
            if stat["norm"] > 1000:
                return "exploding_gradients"

        if gradient_stats[-1]["norm"] < 1e-5:
            return "vanishing_gradients"

        for stat in activation_stats:
            if stat["std"] < 0.1:
                return "vanishing_gradients"

            if stat["std"] > 10.0:
                return "exploding_gradients"

        return "healthy"