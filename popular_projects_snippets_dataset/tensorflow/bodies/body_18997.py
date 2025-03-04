# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Returns the truth value of (x == y) element-wise.

  Performs a [broadcast](
  https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) with the
  arguments and then an element-wise equality comparison, returning a Tensor of
  boolean values.

  For example:

  >>> x = tf.constant([2, 4])
  >>> y = tf.constant(2)
  >>> tf.math.equal(x, y)
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  False])>

  >>> x = tf.constant([2, 4])
  >>> y = tf.constant([2, 4])
  >>> tf.math.equal(x, y)
  <tf.Tensor: shape=(2,), dtype=bool, numpy=array([ True,  True])>

  Args:
    x: A `tf.Tensor`.
    y: A `tf.Tensor`.
    name: A name for the operation (optional).

  Returns:
    A `tf.Tensor` of type bool with the same size as that of x or y.

  Raises:
    `tf.errors.InvalidArgumentError`: If shapes of arguments are incompatible
  """
exit(gen_math_ops.equal(x, y, name=name))
