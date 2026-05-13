import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_positional_encoding(self, seq_len: int, d_model: int) -> NDArray[np.float64]:

        positions = np.arange(seq_len).reshape(seq_len, 1)

        indices = np.arange(0, d_model, 2)

        div_term = np.power(10000, indices / d_model)

        pe = np.zeros((seq_len, d_model), dtype=np.float64)

        pe[:, 0::2] = np.sin(positions / div_term)

        pe[:, 1::2] = np.cos(positions / div_term)

        return np.round(pe, 5)