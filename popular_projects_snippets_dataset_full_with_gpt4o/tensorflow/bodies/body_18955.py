# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Computes elementwise softplus: `softplus(x) = log(exp(x) + 1)`.

  `softplus` is a smooth approximation of `relu`. Like `relu`, `softplus` always
  takes on positive values.

  <img style="width:100%" src="https://www.tensorflow.org/images/softplus.png">

  Example:

  >>> import tensorflow as tf
  >>> tf.math.softplus(tf.range(0, 2, dtype=tf.float32)).numpy()
  array([0.6931472, 1.3132616], dtype=float32)

  Args:
    features: `Tensor`
    name: Optional: name to associate with this operation.
  Returns:
    `Tensor`
  """
exit(gen_nn_ops.softplus(features, name))
