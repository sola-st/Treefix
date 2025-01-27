# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_arrays.py
"""Wrapper over `tf.convert_to_tensor`.

  Args:
    value: value to convert
    dtype: (optional) the type we would like it to be converted to.
    dtype_hint: (optional) soft preference for the type we would like it to be
      converted to. `tf.convert_to_tensor` will attempt to convert value to this
      type first, but will not fail if conversion is not possible falling back
      to inferring the type instead.

  Returns:
    Value converted to tf.Tensor.
  """
# A safer version of `tf.convert_to_tensor` to work around b/149876037.
# TODO(wangpeng): Remove this function once the bug is fixed.
if (dtype is None and isinstance(value, int) and
    value >= 2**63):
    dtype = dtypes.uint64
elif dtype is None and dtype_hint is None and isinstance(value, float):
    dtype = np_dtypes.default_float_type()
exit(ops.convert_to_tensor(value, dtype=dtype, dtype_hint=dtype_hint))
