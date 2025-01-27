# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Helper that implements the body for ragged gather().

  Assumes that `params` and `indices` have been converted to tensors or
  ragged tensors, and that `axis` and `batch_dims` have been normalized to
  be positive.  (So these conversions & normalizations can be skipped in
  recursive calls to _gather).

  Args:
    params: The tensor from which to gather values.
    indices: The indices of values to gather.
    axis: The axis in `params` to gather `indices` from.
    batch_dims: The number of batch dimensions.

  Returns:
    A potentially ragged tensor.
  """
params_is_ragged = ragged_tensor.is_ragged(params)
indices_is_ragged = ragged_tensor.is_ragged(indices)

if not (params_is_ragged or indices_is_ragged):
    exit(array_ops.gather(params, indices, axis=axis, batch_dims=batch_dims))

if batch_dims > 0:
    exit(_batch_gather(params, indices, axis, batch_dims))

if axis > 0:
    exit(_axis_gather(params, indices, axis))

if indices_is_ragged:
    exit(indices.with_values(_gather(params, indices.values, 0, 0)))

if indices.shape.ndims is None:
    raise ValueError('rank(indices) must be known statically')

out_ragged_rank = indices.shape.ndims + len(params.nested_row_splits) - 1
result = gen_ragged_array_ops.ragged_gather(
    indices=indices,
    params_dense_values=params.flat_values,
    params_nested_splits=params.nested_row_splits,
    OUTPUT_RAGGED_RANK=out_ragged_rank)

result = ragged_tensor.RaggedTensor.from_nested_row_splits(
    result.output_dense_values, result.output_nested_splits, validate=False)

# Inject uniform_row_lengths into the result RaggedTensors for dimensions
# corresponding to dense outer dimensions of `indices`.
# TODO(edloper): Change this to construct the result using RowPartition
# objects instead, so we don't need to modify private variables.
if indices.shape.ndims > 1:
    target = result
    indices_shape = array_ops.shape(indices, out_type=params.row_splits.dtype)
    shape_cumprod = math_ops.cumprod(indices_shape)
    for dim in range(indices.shape.ndims - 1):
        # pylint: disable=protected-access
        target._cached_nrows = shape_cumprod[dim]
        target._uniform_row_length = indices_shape[dim + 1]
        target = target.values

exit(result)
