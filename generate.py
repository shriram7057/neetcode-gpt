import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution:
    def generate(
        self,
        model,
        new_chars: int,
        context: TensorType[int],
        context_length: int,
        int_to_char: dict
    ) -> str:

        generator = torch.manual_seed(0)
        initial_state = generator.get_state()

        generated_text = ""

        for i in range(new_chars):

            context_cropped = context[:, -context_length:]

            logits = model(context_cropped)

            last_logits = logits[:, -1, :]

            probs = torch.softmax(last_logits, dim=-1)

            next_token = torch.multinomial(
                probs,
                1,
                generator=generator
            )

            generator.set_state(initial_state)

            context = torch.cat((context, next_token), dim=1)

            generated_text += int_to_char[next_token.item()]

        return generated_text