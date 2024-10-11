# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops.py
"""Sorts values in reverse using `top_k`.

  Args:
    values: Tensor of numeric values.
    axis: Index of the axis which values should be sorted along.
    return_argsort: If False, return the sorted values. If True, return the
      indices that would sort the values.

  Returns:
    The sorted values.
  """
# TODO(b/190410105): replace with a proper sort kernel.
k = array_ops.shape(values)[axis]
rank = array_ops.rank(values)
static_rank = values.shape.ndims
# Fast path: sorting the last axis.
if axis == -1 or axis + 1 == values.get_shape().ndims:
    top_k_input = values
    transposition = None
else:
    # Otherwise, transpose the array. Swap axes `axis` and `rank - 1`.
    if axis < 0:
        # Calculate the actual axis index if counting from the end. Use the static
        # rank if available, or else make the axis back into a tensor.
        axis += static_rank or rank
    if static_rank is not None:
        # Prefer to calculate the transposition array in NumPy and make it a
        # constant.
        transposition = constant_op.constant(
            np.r_[
                # Axes up to axis are unchanged.
                np.arange(axis),
                # Swap axis and rank - 1.
                [static_rank - 1],
                # Axes in [axis + 1, rank - 1) are unchanged.
                np.arange(axis + 1, static_rank - 1),
                # Swap axis and rank - 1.
                [axis]],
            name='transposition')
    else:
        # Generate the transposition array from the tensors.
        transposition = array_ops.tensor_scatter_update(
            math_ops.range(rank), [[axis], [rank-1]], [rank-1, axis])
    top_k_input = array_ops.transpose(values, transposition)

values, indices = nn_ops.top_k(top_k_input, k)
return_value = indices if return_argsort else values
if transposition is not None:
    # transposition contains a single cycle of length 2 (swapping 2 elements),
    # so it is an involution (it is its own inverse).
    return_value = array_ops.transpose(return_value, transposition)
exit(return_value)
