# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Assert that `x` is of integer dtype.

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.compat.v1.assert_integer(x)]):
    output = tf.reduce_sum(x)
  ```

  Args:
    x: `Tensor` whose basetype is integer and is not quantized.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).  Defaults to "assert_integer".

  Raises:
    TypeError:  If `x.dtype` is anything other than non-quantized integer.

  Returns:
    A `no_op` that does nothing.  Type can be determined statically.
  """
with ops.name_scope(name, 'assert_integer', [x]):
    x = ops.convert_to_tensor(x, name='x')
    if not x.dtype.is_integer:
        if context.executing_eagerly():
            name = 'tensor'
        else:
            name = x.name
        err_msg = (
            '%sExpected "x" to be integer type.  Found: %s of dtype %s'
            % (_message_prefix(message), name, x.dtype))
        raise TypeError(err_msg)

    exit(control_flow_ops.no_op('statically_determined_was_integer'))
