from typing import List, Dict


class Solution:

    def greedy_tokenize(self, text: str, vocab: Dict[str, int]) -> List[str]:
        tokens = []
        i = 0

        while i < len(text):

            longest = None

            for j in range(i + 1, len(text) + 1):
                piece = text[i:j]

                if piece in vocab:
                    if longest is None or len(piece) > len(longest):
                        longest = piece

            if longest is not None:
                tokens.append(longest)
                i += len(longest)
            else:
                tokens.append(text[i])
                i += 1

        return tokens

    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:

        return [
            self.greedy_tokenize(str(number), vocab)
            for number in numbers
        ]

    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:

        return len(self.greedy_tokenize(text, vocab))

    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:

        token_count = self.count_tokens(text, vocab)

        word_count = len(text.split())

        return round(token_count / word_count, 4)
        