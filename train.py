import torch
import torch.nn as nn
import torch.nn.functional as F


class Solution:
    def train(
        self,
        model: nn.Module,
        data: torch.Tensor,
        epochs: int,
        context_length: int,
        batch_size: int,
        lr: float
    ) -> float:

        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)

        final_loss = 0.0

        for epoch in range(epochs):

            torch.manual_seed(epoch)

            max_start = len(data) - context_length - 1

            starts = torch.randint(0, max_start + 1, (batch_size,))

            X = torch.stack([
                data[start:start + context_length]
                for start in starts
            ])

            Y = torch.stack([
                data[start + 1:start + 1 + context_length]
                for start in starts
            ])

            logits = model(X)

            B, T, C = logits.shape

            logits_flat = logits.view(B * T, C)

            targets_flat = Y.view(B * T)

            loss = F.cross_entropy(logits_flat, targets_flat)

            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            final_loss = loss.item()

        return round(final_loss, 4)