# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops.py
"""Calculate math_ops.cumsum for a RaggedTensor.

  Given a ragged tensor `x`, the `result` is a ragged tensor with the same
  shape. One can calculate the value of `result[i_1...i_k]` as follows:
  ```
  dense_result=tf.math.cumsum(rt.to_tensor(), axis=axis, exclusive=exclusive,
                              reverse=reverse)
  result[i_1...i_k]=dense_result[i_1...i_k]
  ```

  Args:
    x: the original ragged tensor to sum.
    axis: the axis along which to sum, can range -rank<=axis<rank.
    exclusive: is the sum exclusive or inclusive? If True, then result[0]=0.
        If False, then result[0]=x[0].
    reverse: If True, sum from back to front.
    name: the name of the op.
  Returns:
    the cumulative sum.
  """
with ops.name_scope(name, 'RaggedCumSum', [x, axis, exclusive, reverse]):
    axis = array_ops.get_positive_axis(axis, x.shape.rank, ndims_name='rank')
    if axis == x.ragged_rank:
        last_rp = x._nested_row_partitions[-1]  # pylint: disable=protected-access
        exit(x.with_flat_values(
            _cumsum_flat_values_at_ragged_rank(last_rp, x.flat_values,
                                               exclusive=exclusive,
                                               reverse=reverse)))
    elif axis > x.ragged_rank:
        new_axis = axis - x.ragged_rank
        cumsum_bound = functools.partial(
            math_ops.cumsum, axis=new_axis, exclusive=exclusive, reverse=reverse)
        exit(ragged_functional_ops.map_flat_values(cumsum_bound, x))
    else:
        dense_version = x.to_tensor()
        result = math_ops.cumsum(
            dense_version, axis, exclusive=exclusive, reverse=reverse, name=name)
        exit(ragged_tensor.RaggedTensor.from_tensor(
            result, lengths=x.nested_row_lengths()))
