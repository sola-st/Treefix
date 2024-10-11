# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Asserts that the given `Tensor` is of the specified type.

  This can always be checked statically, so this method returns nothing.

  Example:

  >>> a = tf.Variable(1.0)
  >>> tf.debugging.assert_type(a, tf_type= tf.float32)

  >>> b = tf.constant(21)
  >>> tf.debugging.assert_type(b, tf_type=tf.bool)
  Traceback (most recent call last):
  ...
  TypeError: ...

  >>> c = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2],
  ...  dense_shape=[3, 4])
  >>> tf.debugging.assert_type(c, tf_type= tf.int32)

  Args:
    tensor: A `Tensor`, `SparseTensor` or `tf.Variable` .
    tf_type: A tensorflow type (`dtypes.float32`, `tf.int64`, `dtypes.bool`,
      etc).
    message: A string to prefix to the default message.
    name:  A name for this operation. Defaults to "assert_type"

  Raises:
    TypeError: If the tensor's data type doesn't match `tf_type`.
  """
assert_type(tensor=tensor, tf_type=tf_type, message=message, name=name)
