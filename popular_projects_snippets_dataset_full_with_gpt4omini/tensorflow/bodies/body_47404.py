# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""The function that contains the logic for one RNN step calculation.

    Args:
      inputs: the input tensor, which is a slide from the overall RNN input by
        the time dimension (usually the second dimension).
      states: the state tensor from previous step, which has the same shape
        as `(batch, state_size)`. In the case of timestep 0, it will be the
        initial state user specified, or zero filled tensor otherwise.

    Returns:
      A tuple of two tensors:
        1. output tensor for the current timestep, with size `output_size`.
        2. state tensor for next step, which has the shape of `state_size`.
    """
raise NotImplementedError('Abstract method')
