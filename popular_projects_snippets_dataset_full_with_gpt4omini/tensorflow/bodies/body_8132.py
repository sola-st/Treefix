# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Copies the values in this ShardedVariable to a NumPy array.

    First converts to a single Tensor using the registered conversion function,
    which concatenates the shards, then uses Tensor.numpy() to convert to
    a NumPy array.

    Returns:
      A NumPy array of the same shape and dtype.
    """
exit(_var_to_tensor(self).numpy())
