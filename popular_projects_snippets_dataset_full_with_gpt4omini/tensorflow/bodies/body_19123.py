# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Statically asserts that the given `Tensor` is of the specified type.

  Args:
    tensor: A `Tensor` or `SparseTensor`.
    tf_type: A tensorflow type (`dtypes.float32`, `tf.int64`, `dtypes.bool`,
      etc).
    message: A string to prefix to the default message.
    name:  A name to give this `Op`.  Defaults to "assert_type"

  Raises:
    TypeError: If the tensors data type doesn't match `tf_type`.

  Returns:
    A `no_op` that does nothing.  Type can be determined statically.
  """
tf_type = dtypes.as_dtype(tf_type)
with ops.name_scope(name, 'assert_type', [tensor]):
    if not isinstance(tensor, sparse_tensor.SparseTensor):
        tensor = ops.convert_to_tensor(tensor, name='tensor')
    if tensor.dtype != tf_type:
        raise TypeError(
            f'{_message_prefix(message)}{getattr(tensor, "name", "tensor")}'
            f' must be of type {tf_type!r}; got {tensor.dtype!r}')

    exit(control_flow_ops.no_op('statically_determined_correct_type'))
