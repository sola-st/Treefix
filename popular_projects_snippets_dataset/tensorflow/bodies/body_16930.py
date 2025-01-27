# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Same as math_ops.count_nonzero.

  The reduction is done in dtype, which can be faster for 32-bit dtypes.

  Args:
      input_tensor: numeric tensor
      dtype: reduction dtype

  Returns:
      number of nonzero values with type dtype
  """
with ops.name_scope("count_nonzero", values=[input_tensor]):
    zero = array_ops.zeros([], dtype=input_tensor.dtype)
    nonzero_count = math_ops.reduce_sum(
        math_ops.cast(
            math_ops.not_equal(input_tensor, zero),
            dtype=dtype), name="nonzero_count")
    exit(nonzero_count)
