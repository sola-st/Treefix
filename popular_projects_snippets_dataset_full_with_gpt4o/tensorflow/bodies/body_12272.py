# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""A placeholder op that passes through `input` when its output is not fed.

  @compatibility(TF2)
  This API is strongly discouraged for use with eager execution and
  `tf.function`. The primary use of this API is for testing computation wrapped
  within a `tf.function` where the input tensors might not have statically known
  fully-defined shapes. The same can be achieved by creating a
  [concrete function](
  https://www.tensorflow.org/guide/function#obtaining_concrete_functions)
  from the `tf.function` with a `tf.TensorSpec` input which has partially
  defined shapes. For example, the code

  >>> @tf.function
  ... def f():
  ...   x = tf.compat.v1.placeholder_with_default(
  ...       tf.constant([[1., 2., 3.], [4., 5., 6.]]), [None, 3])
  ...   y = tf.constant([[1.],[2.], [3.]])
  ...   z = tf.matmul(x, y)
  ...   assert z.shape[0] == None
  ...   assert z.shape[1] == 1

  >>> f()

  can easily be replaced by

  >>> @tf.function
  ... def f(x):
  ...   y = tf.constant([[1.],[2.], [3.]])
  ...   z = tf.matmul(x, y)
  ...   assert z.shape[0] == None
  ...   assert z.shape[1] == 1

  >>> g = f.get_concrete_function(tf.TensorSpec([None, 3]))

  You can learn more about `tf.function` at [Better
  performance with tf.function](https://www.tensorflow.org/guide/function).
  @end_compatibility

  Args:
    input: A `Tensor`. The default value to produce when output is not fed.
    shape: A `tf.TensorShape` or list of `int`s. The (possibly partial) shape of
      the tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
exit(gen_array_ops.placeholder_with_default(input, shape, name))
