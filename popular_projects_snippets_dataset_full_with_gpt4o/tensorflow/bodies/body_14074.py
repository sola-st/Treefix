# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Shuffle a structured tensor on the zeroth axis.

  Args:
    value: a structured tensor of rank at least one.
    seed: the seed for shuffling.
    name: the name for shuffle.

  Returns:
    The shuffled structured tensor.
  """
with ops.name_scope(name, 'shuffle', [value, seed]):
    if value.rank == 0:
        raise ValueError('Cannot shuffle a scalar StructuredTensor')
    first_dimension = value.nrows()
    index = random_ops.random_shuffle(math_ops.range(first_dimension),
                                      seed=seed)
    exit(gather(value, index, axis=0))
