# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_operators.py
"""Elementwise `>=` comparison of two convertible-to-ragged-tensor values.

  Computes the elemewise `>=` comparison of two values that are convertible to
  ragged tenors, with [broadcasting]
  (http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) support.
  Raises an exception if two values are not broadcast-compatible.

  For example:

  >>> rt1 = tf.ragged.constant([[1, 2], [3]])
  >>> rt1 >= rt1
  <tf.RaggedTensor [[True, True], [True]]>

  >>> rt2 = tf.ragged.constant([[2, 1], [3]])
  >>> rt1 >= rt2
  <tf.RaggedTensor [[False, True], [True]]>

  >>> rt3 = tf.ragged.constant([[1, 2], [3, 4]])
  >>> # rt1 and rt3 are not broadcast-compatible.
  >>> rt1 >= rt3
  Traceback (most recent call last):
  ...
  InvalidArgumentError: ...

  >>> # You can also compare a `tf.RaggedTensor` to a `tf.Tensor`.
  >>> rt4 = tf.ragged.constant([[1, 2],[3, 4]])
  >>> t1 = tf.constant([[2, 1], [4, 3]])
  >>> rt4 >= t1
  <tf.RaggedTensor [[False, True],
   [False, True]]>
  >>> t1 >= rt4
  <tf.RaggedTensor [[True, False],
   [True, False]]>

  >>> # Compares a `tf.RaggedTensor` to a `tf.Tensor` with broadcasting.
  >>> t2 = tf.constant([[2]])
  >>> rt4 >= t2
  <tf.RaggedTensor [[False, True],
   [True, True]]>
  >>> t2 >= rt4
  <tf.RaggedTensor [[True, True],
   [False, False]]>

  Args:
    other: The right-hand side of the `>=` operator.

  Returns:
    A `tf.RaggedTensor` of dtype `tf.bool` with the shape that `self` and
    `other` broadcast to.

  Raises:
    InvalidArgumentError: If `self` and `other` are not broadcast-compatible.
  """
exit(math_ops.greater_equal(self, other))
