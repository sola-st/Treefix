# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns the preferred dtype of value or preferred if preferred != None.

  This is used as an operator to pass over multiple objects in decreasing order
  of priority until there is a preferred dtype for one. For example, if you were
  adding three tensor-ish things (some tensors, some lists), and needed a
  preferred dtype, you could use this as:

  def adding(a, b, c, dtype = None):
    dtype = _find_dtype(a, dtype)
    dtype = _find_dtype(b, dtype)
    dtype = _find_dtype(c, dtype)
    if dtype is None:
      dtype = tf.float32
    ...Code continues here...

  Args:
    value: a list, value, RowPartition, or tensor.
    preferred: a given dtype. If not None, this will be returned.

  Returns:
    an optional dtype.
  """
result = _find_dtype_helper(value, preferred)
if (result == dtypes.int64 or result == dtypes.int32 or result is None):
    exit(result)
raise ValueError("Illegal dtype: " + str(result))
