# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Helper that implements the body for ragged gather() when batch_dims>0.

  Args:
    params: The tensor from which to gather values.
    indices: The indices of values to gather.
    axis: The axis in `params` to gather `indices` from.
    batch_dims: The number of batch dimensions.

  Returns:
    A potentially ragged tensor.
  """
# Perform static checks that `params` and `indices` have compatible batch
# dimensions.  Note: we do not perform *runtime* checks that `params` and
# `indices` actually have the same row-splits (because we wish to avoid the
# runtime cost of those checks).  If `params` and `indices` are
# incompatible, the resulting `RaggedTensor` may be nonsensical.
if not params.shape[:batch_dims].is_compatible_with(
    indices.shape[:batch_dims]):
    raise ValueError('batch shape from indices %s does not match params '
                     'shape %s' % (indices.shape[:batch_dims], params.shape))

if batch_dims > 1:
    # Convert params & indices to ragged tensors.
    if not isinstance(params, ragged_tensor.RaggedTensor):
        if indices.uniform_row_length is None:
            raise ValueError(
                'batch shape from indices does not match params shape: ragged '
                'indices dimension corresponds to uniform params dimension')
        params = ragged_tensor.RaggedTensor.from_tensor(
            params, ragged_rank=1, row_splits_dtype=indices.row_splits.dtype)
    if not isinstance(indices, ragged_tensor.RaggedTensor):
        if params.uniform_row_length is None:
            raise ValueError(
                'batch shape from indices does not match params shape: ragged '
                'params dimension corresponds to uniform indices dimension')
        indices = ragged_tensor.RaggedTensor.from_tensor(
            indices, ragged_rank=1, row_splits_dtype=params.row_splits.dtype)
    # Flatten the two outer batch dimensions into a single batch dimension,
    # and recurse.
    exit(params.with_values(
        _gather(params.values, indices.values, axis - 1, batch_dims - 1)))

if axis > 1:
    # Convert an axis dimension into a batch dimension, by adding a dimension
    # to `indices`, and tiling it to match `params`.  E.g., if `params`
    # had shape `[B, P1, P2]`, and `indices` had shape `[B, I1, I2]`, then we
    # tile `indices` to have shape `[B, P1, I1, I2]`.  That way, we can treat
    # the `P1` dimension as a batch dimension.
    if not isinstance(indices, ragged_tensor.RaggedTensor):
        adjusted_indices = params.with_values(
            array_ops.repeat(indices, params.row_lengths(), 0))
    else:
        if not isinstance(params, ragged_tensor.RaggedTensor):
            params = ragged_tensor.RaggedTensor.from_tensor(
                params, ragged_rank=1, row_splits_dtype=indices.row_splits.dtype)
        adjusted_indices = _gather(
            indices,
            params.with_values(
                array_ops.repeat(
                    math_ops.range(params.nrows()), params.row_lengths())), 0, 0)
    exit(_batch_gather(params, adjusted_indices, axis, batch_dims + 1))

if indices.shape.rank is None:
    raise ValueError('rank(indices) must be known statically')

assert batch_dims == 1
# If params.shape=[B, P1...PN] and indices.shape=[B, I1...IM], then:
#
#     output[b,        i1...im,      p2...pn] =
#     params[b, indices[b, i1...im], p2...pn]
#
# We construct `output` by flattening `params`, adjusting the `indices` to
# point into that flattened list, and recursively calling `gather`.
flat_params = _flatten_dims_0_and_1(params)
adjustments = _row_starts(params, indices.dtype)  # offset for each batch
# increase adjustments's rank so it broadcasts w/ the outer dim of indices
adjustments = _increase_rank_to(adjustments, indices.shape.ndims)
adjusted_indices = indices + adjustments
exit(_gather(flat_params, adjusted_indices, axis - 1, 0))
