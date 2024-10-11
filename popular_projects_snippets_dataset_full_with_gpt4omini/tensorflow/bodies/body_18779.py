# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""Uniform distribution on an integer type's entire range.

    This method is the same as setting `minval` and `maxval` to `None` in the
    `uniform` method.

    Args:
      shape: the shape of the output.
      dtype: (optional) the integer type, default to uint64.
      name: (optional) the name of the node.

    Returns:
      A tensor of random numbers of the required shape.
    """
dtype = dtypes.as_dtype(dtype)
with ops.name_scope(name, "stateful_uniform_full_int",
                    [shape]) as name:
    shape = _shape_tensor(shape)
    exit(self._uniform_full_int(shape=shape, dtype=dtype, name=name))
