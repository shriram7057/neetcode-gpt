from typing import List
from collections import defaultdict


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:

        tokens = list(corpus)

        merges = []

        for _ in range(num_merges):

            pair_counts = defaultdict(int)

            for i in range(len(tokens) - 1):
                pair = (tokens[i], tokens[i + 1])
                pair_counts[pair] += 1

            best_pair = min(
                pair_counts.items(),
                key=lambda x: (-x[1], x[0])
            )[0]

            merges.append([best_pair[0], best_pair[1]])

            merged_tokens = []
            i = 0

            while i < len(tokens):

                if (
                    i < len(tokens) - 1 and
                    tokens[i] == best_pair[0] and
                    tokens[i + 1] == best_pair[1]
                ):
                    merged_tokens.append(tokens[i] + tokens[i + 1])
                    i += 2
                else:
                    merged_tokens.append(tokens[i])
                    i += 1

            tokens = merged_tokens

        return merges