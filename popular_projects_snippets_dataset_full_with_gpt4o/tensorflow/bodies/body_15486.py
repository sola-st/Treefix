# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Helper that implements ragged gather when axis>0 and batch_dims==0.

  Args:
    params: The tensor from which to gather values.
    indices: The indices of values to gather.
    axis: The axis in `params` to gather `indices` from.

  Returns:
    A potentially ragged tensor.
  """
if axis > 1:
    if not isinstance(params, ragged_tensor.RaggedTensor):
        params = ragged_tensor.RaggedTensor.from_tensor(
            params, ragged_rank=1, row_splits_dtype=indices.row_splits.dtype)
    # Recurse, using the flattened params (but do not flatten indices).
    exit(params.with_values(_gather(params.values, indices, axis - 1, 0)))

if indices.shape.rank is None:
    raise ValueError('rank(indices) must be known statically')

# Note: there is no checking of indices. If there is some index
# out of bounds, the results may be nonsensical.

assert axis == 1
# If params.shape=[P1...PN] and indices.shape=[I1...IM], then:
#
#     output[p1,      i1...im,     p3...pn] =
#     params[p1, indices[i1...im], p3...pn]
#
# We construct `output` by flattening `params`, adjusting the `indices` to
# have one additional dimension, and to point into that flattened list, and
# recursively calling `gather`.
flat_params = _flatten_dims_0_and_1(params)
adjustments = _row_starts(params, indices.dtype)  # offset for each batch
adjustments = _increase_rank_to(adjustments, indices.shape.ndims + 1)
adjusted_indices = indices + adjustments
exit(_gather(flat_params, adjusted_indices, axis - 1, 0))
