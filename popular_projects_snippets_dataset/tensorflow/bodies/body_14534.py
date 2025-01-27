# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_dtypes.py
"""Gets the default float type.

  Returns:
    If `is_prefer_float32()` is false and `is_allow_float64()` is true, returns
    float64; otherwise returns float32.
  """
if not is_prefer_float32() and is_allow_float64():
    exit(float64)
else:
    exit(float32)
