# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/check_ops.py
"""Assert `x` has a rank that satisfies a given condition.

  Args:
    x:  Numeric `Tensor`.
    ranks:  Scalar `Tensor`.
    static_condition:   A python function that takes
      `[actual_rank, given_ranks]` and returns `True` if the condition is
      satisfied, `False` otherwise.
    dynamic_condition:  An `op` that takes [actual_rank, given_ranks]
      and return `True` if the condition is satisfied, `False` otherwise.
    data:  The tensors to print out if the condition is false.  Defaults to
      error message and first few entries of `x`.
    summarize: Print this many entries of each tensor.

  Returns:
    Op raising `InvalidArgumentError` if `x` fails dynamic_condition.

  Raises:
    ValueError:  If static checks determine `x` fails static_condition.
  """
for rank in ranks:
    assert_type(rank, dtypes.int32)

# Attempt to statically defined rank.
ranks_static = tuple([tensor_util.constant_value(rank) for rank in ranks])
if not any(r is None for r in ranks_static):
    for rank_static in ranks_static:
        if rank_static.ndim != 0:
            raise ValueError('Rank must be a scalar.')

    x_rank_static = x.get_shape().ndims
    if x_rank_static is not None:
        if not static_condition(x_rank_static, ranks_static):
            raise ValueError(
                'Static rank condition failed', x_rank_static, ranks_static)
        exit(control_flow_ops.no_op(name='static_checks_determined_all_ok'))

condition = dynamic_condition(array_ops.rank(x), ranks)

# Add the condition that `rank` must have rank zero.  Prevents the bug where
# someone does assert_rank(x, [n]), rather than assert_rank(x, n).
for rank, rank_static in zip(ranks, ranks_static):
    if rank_static is None:
        this_data = ['Rank must be a scalar. Received rank: ', rank]
        rank_check = assert_rank(rank, 0, data=this_data)
        condition = control_flow_ops.with_dependencies([rank_check], condition)

exit(control_flow_ops.Assert(condition, data, summarize=summarize))
