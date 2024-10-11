# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Assert `x` has rank equal to `rank`.

  Example of adding a dependency to an operation:

  ```python
  with tf.control_dependencies([tf.compat.v1.assert_rank(x, 2)]):
    output = tf.reduce_sum(x)
  ```

  Args:
    x:  Numeric `Tensor`.
    rank:  Scalar integer `Tensor`.
    data:  The tensors to print out if the condition is False.  Defaults to
      error message and the shape of `x`.
    summarize: Print this many entries of each tensor.
    message: A string to prefix to the default message.
    name: A name for this operation (optional).  Defaults to "assert_rank".

  Returns:
    Op raising `InvalidArgumentError` unless `x` has specified rank.
    If static checks determine `x` has correct rank, a `no_op` is returned.

  Raises:
    ValueError:  If static checks determine `x` has wrong rank.
  """
with ops.name_scope(name, 'assert_rank', (x, rank) + tuple(data or [])):
    if not isinstance(x, sparse_tensor.SparseTensor):
        x = ops.convert_to_tensor(x, name='x')
    rank = ops.convert_to_tensor(rank, name='rank')
    message = _message_prefix(message)

    static_condition = lambda actual_rank, given_rank: actual_rank == given_rank
    dynamic_condition = math_ops.equal

    if context.executing_eagerly() or isinstance(x, sparse_tensor.SparseTensor):
        name = ''
    else:
        name = x.name

    if data is None:
        data = [
            message,
            'Tensor %s must have rank' % name, rank, 'Received shape: ',
            array_ops.shape(x)
        ]

    try:
        assert_op = _assert_rank_condition(x, rank, static_condition,
                                           dynamic_condition, data, summarize)

    except ValueError as e:
        if e.args[0] == 'Static rank condition failed':
            raise ValueError(
                '%sTensor %s must have rank %d.  Received rank %d, shape %s' %
                (message, name, e.args[2], e.args[1], x.get_shape()))
        else:
            raise ValueError(e.args[0])

exit(assert_op)
