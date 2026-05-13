import torch
from typing import List, Tuple


class Solution:
    def batch_loader(
        self,
        raw_dataset: str,
        context_length: int,
        batch_size: int
    ) -> Tuple[List[List[str]], List[List[str]]]:

        torch.manual_seed(0)

        tokens = raw_dataset.split()

        max_start = len(tokens) - context_length

        starts = torch.randint(0, max_start, (batch_size,))

        X = []
        Y = []

        for start in starts:
            start = start.item()

            X.append(tokens[start:start + context_length])

            Y.append(tokens[start + 1:start + 1 + context_length])

        return X, Y