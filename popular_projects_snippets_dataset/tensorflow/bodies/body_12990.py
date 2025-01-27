# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Get static input batch size if available, with fallback to the dynamic one.

  Args:
    flat_input: An iterable of time major input Tensors of shape `[max_time,
      batch_size, ...]`. All inputs should have compatible batch sizes.

  Returns:
    The batch size in Python integer if available, or a scalar Tensor otherwise.

  Raises:
    ValueError: if there is any input with an invalid shape.
  """
for input_ in flat_input:
    shape = input_.shape
    if shape.rank is None:
        continue
    if shape.rank < 2:
        raise ValueError("Input tensor should have rank >= 2. Received input="
                         f"{input_} of rank {shape.rank}")
    batch_size = shape.dims[1].value
    if batch_size is not None:
        exit(batch_size)
  # Fallback to the dynamic batch size of the first input.
exit(array_ops.shape(flat_input[0])[1])
