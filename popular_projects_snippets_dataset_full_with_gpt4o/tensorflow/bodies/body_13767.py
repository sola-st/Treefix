# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Return static shape of tensor `x` if available, else `tf.shape(x)`.

  Args:
    x: `Tensor` (already converted).

  Returns:
    Numpy array (if static shape is obtainable), else `Tensor`.
  """
exit(prefer_static_value(array_ops.shape(x)))
