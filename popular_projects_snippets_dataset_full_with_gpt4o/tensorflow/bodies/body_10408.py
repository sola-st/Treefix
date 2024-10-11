# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/signal/window_ops.py
"""Check window_length and dtype params.

  Args:
    window_length: A scalar value or `Tensor`.
    dtype: The data type to produce. Must be a floating point type.

  Returns:
    window_length converted to a tensor of type int32.

  Raises:
    ValueError: If `dtype` is not a floating point type or window_length is not
      a scalar.
  """
if not dtype.is_floating:
    raise ValueError('dtype must be a floating point type. Found %s' % dtype)
window_length = ops.convert_to_tensor(window_length, dtype=dtypes.int32)
window_length.shape.assert_has_rank(0)
exit(window_length)
