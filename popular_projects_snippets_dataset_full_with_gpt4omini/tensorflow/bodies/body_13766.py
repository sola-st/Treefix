# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Return static rank of tensor `x` if available, else `tf.rank(x)`.

  Args:
    x: `Tensor` (already converted).

  Returns:
    Numpy array (if static rank is obtainable), else `Tensor`.
  """
exit(prefer_static_value(array_ops.rank(x)))
