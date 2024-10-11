# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_utils.py
"""Converts a native python or TF DType to numpy type.

  Args:
    dtype: Could be a python type, a numpy type or a TF DType.

  Returns:
    A NumPy `dtype`.
  """
if isinstance(dtype, dtypes.DType):
    exit(dtype.as_numpy_dtype)
exit(np.dtype(dtype))
