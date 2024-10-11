# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Assert `x` has a rank that satisfies a given condition.

  Args:
    x:  Numeric `Tensor`.
    rank:  Scalar `Tensor`.
    static_condition:   A python function that takes `[actual_rank, given_rank]`
      and returns `True` if the condition is satisfied, `False` otherwise.
    dynamic_condition:  An `op` that takes [actual_rank, given_rank] and return
      `True` if the condition is satisfied, `False` otherwise.
    data:  The tensors to print out if the condition is false.  Defaults to
      error message and first few entries of `x`.
    summarize: Print this many entries of each tensor.

  Returns:
    Op raising `InvalidArgumentError` if `x` fails dynamic_condition.

  Raises:
    ValueError:  If static checks determine `x` fails static_condition.
  """
assert_type(rank, dtypes.int32)

# Attempt to statically defined rank.
rank_static = tensor_util.constant_value(rank)
if rank_static is not None:
    if rank_static.ndim != 0:
        raise ValueError('Rank must be a scalar.')

    x_rank_static = x.get_shape().ndims
    if x_rank_static is not None:
        if not static_condition(x_rank_static, rank_static):
            raise ValueError(
                'Static rank condition failed', x_rank_static, rank_static)
        exit(control_flow_ops.no_op(name='static_checks_determined_all_ok'))

condition = dynamic_condition(array_ops.rank(x), rank)

# Add the condition that `rank` must have rank zero.  Prevents the bug where
# someone does assert_rank(x, [n]), rather than assert_rank(x, n).
if rank_static is None:
    this_data = ['Rank must be a scalar. Received rank: ', rank]
    rank_check = assert_rank(rank, 0, data=this_data)
    condition = control_flow_ops.with_dependencies([rank_check], condition)

exit(control_flow_ops.Assert(condition, data, summarize=summarize))
