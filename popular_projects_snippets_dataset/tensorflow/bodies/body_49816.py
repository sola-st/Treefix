# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/activations.py
"""Exponential activation function.

  For example:

  >>> a = tf.constant([-3.0,-1.0, 0.0,1.0,3.0], dtype = tf.float32)
  >>> b = tf.keras.activations.exponential(a)
  >>> b.numpy()
  array([0.04978707,  0.36787945,  1.,  2.7182817 , 20.085537], dtype=float32)

  Args:
      x: Input tensor.

  Returns:
      Tensor with exponential activation: `exp(x)`.
  """
exit(math_ops.exp(x))
