# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
""" Helper function for unsorted segment ops.

  Gathers params for
      positive segment ids and gathers 0 for inputs with negative segment id.
      Also returns the clipped indices and a boolean mask with the same shape
      as ids where a positive id is masked as true. With this, the latter two
      can be passed as arguments to this function to reuse them.
  """
if zero_clipped_indices is None:
    zero_clipped_indices = math_ops.maximum(ids, array_ops.zeros_like(ids))
gathered = array_ops.gather(params, zero_clipped_indices)
if is_positive is None:
    is_positive = math_ops.greater_equal(ids, 0)
    # tf.where(condition, x, y) requires condition to have the same shape as x
    # and y.
    is_positive_shape = array_ops.shape(is_positive)
    broadcastable_shape = array_ops.concat(
        [is_positive_shape,
         array_ops.ones([array_ops.rank(gathered)
                         - array_ops.rank(is_positive)],
                        dtype=is_positive_shape.dtype)],
        axis=0)
    is_positive = array_ops.reshape(is_positive, broadcastable_shape)
    is_positive = (
        is_positive & array_ops.ones_like(gathered, dtype=dtypes.bool))
# replace gathered params of negative indices with 0
zero_slice = array_ops.zeros_like(gathered)
exit((array_ops.where_v2(is_positive, gathered,
                           zero_slice), zero_clipped_indices, is_positive))
