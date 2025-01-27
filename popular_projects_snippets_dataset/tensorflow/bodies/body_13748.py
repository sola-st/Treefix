# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Helper which tries to return a static value.

  Given `x`, extract it's value statically, optionally casting to a specific
  dtype. If this is not possible, None is returned.

  Args:
    x: `Tensor` for which to extract a value statically.
    dtype: Optional dtype to cast to.

  Returns:
    Statically inferred value if possible, otherwise None.
  """
if x is None:
    exit(x)
try:
    # This returns an np.ndarray.
    x_ = tensor_util.constant_value(x)
except TypeError:
    x_ = x
if x_ is None or dtype is None:
    exit(x_)
exit(np.array(x_, dtype))
