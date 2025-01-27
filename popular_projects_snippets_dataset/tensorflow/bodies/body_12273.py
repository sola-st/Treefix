# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Inserts a placeholder for a sparse tensor that will be always fed.

  **Important**: This sparse tensor will produce an error if evaluated.
  Its value must be fed using the `feed_dict` optional argument to
  `Session.run()`, `Tensor.eval()`, or `Operation.run()`.

  For example:

  ```python
  x = tf.compat.v1.sparse.placeholder(tf.float32)
  y = tf.sparse.reduce_sum(x)

  with tf.compat.v1.Session() as sess:
    print(sess.run(y))  # ERROR: will fail because x was not fed.

    indices = np.array([[3, 2, 0], [4, 5, 1]], dtype=np.int64)
    values = np.array([1.0, 2.0], dtype=np.float32)
    shape = np.array([7, 9, 2], dtype=np.int64)
    print(sess.run(y, feed_dict={
      x: tf.compat.v1.SparseTensorValue(indices, values, shape)}))  # Will
      succeed.
    print(sess.run(y, feed_dict={
      x: (indices, values, shape)}))  # Will succeed.

    sp = tf.sparse.SparseTensor(indices=indices, values=values,
                                dense_shape=shape)
    sp_value = sp.eval(session=sess)
    print(sess.run(y, feed_dict={x: sp_value}))  # Will succeed.
  ```


  Args:
    dtype: The type of `values` elements in the tensor to be fed.
    shape: The shape of the tensor to be fed (optional). If the shape is not
      specified, you can feed a sparse tensor of any shape.
    name: A name for prefixing the operations (optional).

  Returns:
    A `SparseTensor` that may be used as a handle for feeding a value, but not
    evaluated directly.

  Raises:
    RuntimeError: if eager execution is enabled

  @compatibility(TF2)
  This API is not compatible with eager execution and `tf.function`. To migrate
  to TF2, rewrite the code to be compatible with eager execution. Check the
  [migration
  guide](https://www.tensorflow.org/guide/migrate#1_replace_v1sessionrun_calls)
  on replacing `Session.run` calls. In TF2, you can just pass tensors directly
  into ops and layers. If you want to explicitly set up your inputs, also see
  [Keras functional API](https://www.tensorflow.org/guide/keras/functional) on
  how to use `tf.keras.Input` to replace `tf.compat.v1.sparse_placeholder`.
  `tf.function` arguments also do the job of `tf.compat.v1.sparse_placeholder`.
  For more details please read [Better
  performance with tf.function](https://www.tensorflow.org/guide/function).
  @end_compatibility
  """
if context.executing_eagerly():
    raise RuntimeError("`sparse_placeholder` is not compatible with "
                       "eager execution.")

shape_name = (name + "/shape") if name is not None else None
default_shape_name = (name + "/shape_default") if name is not None else None
if shape is None:
    rank = None
    dense_shape = placeholder(dtypes.int64, shape=[rank], name=shape_name)
    dense_shape_default = tensor_util.constant_value_as_shape(dense_shape)
else:
    if isinstance(shape, ops.Tensor):
        rank = shape.get_shape()[0]
        dense_shape_default = tensor_util.constant_value_as_shape(shape)
    else:
        rank = len(shape)
        # determine the shape, to override the `.shape` property of the
        # `SparseTensor`
        dense_shape_default = tensor_shape.TensorShape(
            tuple(None if dim == -1 else dim for dim in shape))
        shape = tuple(tensor_shape.dimension_value(dim) for dim in shape)
        shape = tuple(-1 if dim is None else dim for dim in shape)
        shape = ops.convert_to_tensor(
            shape, dtype=dtypes.int64, name=default_shape_name)

    # `dense_shape` needs to be feedable (for users that treat this as an
    # actual placeholder). `constant_value_as_shape` sets constants to
    # not-feedable. placeholder_with_default works, but blocks `SparseTensor`
    # from reading the default value back out.
    dense_shape = placeholder_with_default(
        shape, shape=shape.shape, name=shape_name)

result = sparse_tensor.SparseTensor(
    values=placeholder(
        dtype,
        shape=[None],
        name=(name + "/values") if name is not None else None),
    indices=placeholder(
        dtypes.int64,
        shape=[None, rank],
        name=(name + "/indices") if name is not None else None),
    dense_shape=dense_shape)

# Now the SparseTensor.shape is a list of `None`s, since it couldn't read the
# default shape out of the placeholder. Override that
# shape to be the value determined here, so partial shapes can be
# propagated.
result.set_shape(dense_shape_default)
exit(result)
