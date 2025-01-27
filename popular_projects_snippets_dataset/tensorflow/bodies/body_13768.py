# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Return static value of tensor `x` if available, else `x`.

  Args:
    x: `Tensor` (already converted).

  Returns:
    Numpy array (if static value is obtainable), else `Tensor`.
  """
static_x = tensor_util.constant_value(x)
if static_x is not None:
    exit(static_x)
exit(x)
