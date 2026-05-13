import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List


class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:

        all_sentences = positive + negative

        vocab = sorted(
            set(
                word
                for sentence in all_sentences
                for word in sentence.split()
            )
        )

        word_to_id = {
            word: idx + 1
            for idx, word in enumerate(vocab)
        }

        encoded_sentences = []

        for sentence in all_sentences:
            encoded = [word_to_id[word] for word in sentence.split()]
            encoded_sentences.append(
                torch.tensor(encoded, dtype=torch.float32)
            )

        padded = nn.utils.rnn.pad_sequence(
            encoded_sentences,
            batch_first=True,
            padding_value=0
        )

        return padded