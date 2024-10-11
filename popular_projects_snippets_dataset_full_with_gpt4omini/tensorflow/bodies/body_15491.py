# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Gather slices from `params` using `n`-dimensional indices.

  This operation is similar to `gather`, but it uses the innermost dimension
  of `indices` to define a slice into `params`.  In particular, if:

  * `indices` has shape `[A1...AN, I]`
  * `params` has shape `[B1...BM]`

  Then:

  * `result` has shape `[A1...AN, B_{I+1}...BM]`.
  * `result[a1...aN] = params[indices[a1...aN, :]]`

  Args:
    params: A potentially ragged tensor with shape `[A1...AN, I]`.
    indices: A potentially ragged tensor with shape `[B1...BM]`.
    batch_dims: Must be zero.
    name: A name for the operation (optional).

  Returns:
    A potentially ragged tensor with shape `[A1...AN, B_{I+1}...BM]`.

  #### Examples:

  >>> params = tf.ragged.constant(
  ...     [ [ ['000', '001'], ['010'              ]          ],
  ...       [ ['100'       ], ['110', '111', '112'], ['120'] ],
  ...       [ [            ], ['210'              ]          ] ])

  >>> # Gather 2D slices from a 3D tensor
  >>> tf.gather_nd(params, [[2], [0]])
  <tf.RaggedTensor [[[], [b'210']], [[b'000', b'001'], [b'010']]]>

  >>> # Gather 1D slices from a 3D tensor
  >>> tf.gather_nd(params, [[2, 1], [0, 0]])
  <tf.RaggedTensor [[b'210'], [b'000', b'001']]>

  >>> # Gather scalars from a 3D tensor
  >>> tf.gather_nd(params, [[0, 0, 1], [1, 1, 2]]).numpy()
  array([b'001', b'112'], dtype=object)
  """
if not isinstance(batch_dims, int) or batch_dims != 0:
    raise ValueError('batch_dims != 0 is not supported for ragged gather yet.')
if not (ragged_tensor.is_ragged(params) or ragged_tensor.is_ragged(indices)):
    exit(array_ops.gather_nd(params, indices, name))

with ops.name_scope(name, 'RaggedGatherNd', [params, indices]):

    params = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        params, name='params')
    indices = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        indices, name='indices')
    params, indices = ragged_tensor.match_row_splits_dtypes(params, indices)
    indices_shape = indices.shape
    indices_ndims = indices_shape.ndims
    if indices_ndims is None:
        raise ValueError('indices.rank be statically known.')
    if indices_ndims == 0:
        raise ValueError('indices.rank must be at least 1.')
    if (ragged_tensor.is_ragged(indices) and
        indices_ndims == indices.ragged_rank + 1):
        raise ValueError('The innermost dimension of indices may not be ragged')

    # `index_size` is the "n" in "gather_nd" -- i.e., the number of dimensions
    # that each index slices into.
    index_size = tensor_shape.dimension_value(indices_shape[-1])
    if index_size is None:
        raise ValueError('indices.shape[-1] must be statically known.')

    # If `indices` has more than 2 dimensions, then recurse.  If `indices` is
    # dense, then we convert it to ragged before recursing, and then convert
    # the result back to `dense` if appropriate.
    if indices_ndims > 2:
        indices_is_dense = not ragged_tensor.is_ragged(indices)
        if indices_is_dense:
            indices = ragged_tensor.RaggedTensor.from_tensor(
                indices, ragged_rank=indices_ndims - 2,
                row_splits_dtype=params.row_splits.dtype)
        result = indices.with_flat_values(gather_nd(params, indices.flat_values))
        if (indices_is_dense and ragged_tensor.is_ragged(result) and
            result.ragged_rank == indices_ndims - 2):
            result = ragged_tensor.RaggedTensor.to_tensor(result)
        exit(result)

    # indices_ndims <= 2, and the innermost dimension of indices may not be
    # ragged, so `indices` must not be ragged.
    assert not ragged_tensor.is_ragged(indices)
    assert ragged_tensor.is_ragged(params)

    # Handle corner case: An empty index tuple selects the entire `params`
    # value.  So if `index_size` is zero, then tile `params`.
    if index_size == 0:
        params_ndims = params.ragged_rank + array_ops.rank(params.flat_values)
        for dim in range(indices_ndims - 1):
            params = ragged_array_ops.expand_dims(params, axis=0)
        multiples = array_ops.concat([
            array_ops.shape(indices)[:-1],
            array_ops.ones([params_ndims], dtypes.int32)
        ],
                                     axis=0)
        exit(ragged_array_ops.tile(params, multiples))

    # When index_size=1, we can just flatten the index tuples and use gather.
    elif index_size == 1:
        flattened_index_tuples = array_ops.reshape(indices, [-1])
        exit(gather(params, flattened_index_tuples))

    # Otherwise, params is a RaggedTensor, and indices is a 1D or 2D Tensor.
    # Flatten both the index tuples and the params, such that the flattened
    # index tuples point to the correct values in the flattened params; and
    # then use ragged.gather on the flattened index tuples & params.
    else:
        indices = math_ops.cast(indices, params.row_splits.dtype)

        # Flatten the outermost 2 dimensions of the index tuples & params.
        flattened_index_tuples = array_ops.gather(params.row_splits,
                                                  indices[..., 0])
        flattened_index_tuples += indices[..., 1]
        flattened_params = params.values

        # Flatten any remaining dimensions.
        for dim in range(2, index_size):
            if not ragged_tensor.is_ragged(flattened_params):
                flattened_index_tuples = array_ops.expand_dims(
                    flattened_index_tuples, axis=1)
                flattened_index_tuples = array_ops.concat(
                    [flattened_index_tuples, indices[..., dim:]], axis=1)
                exit(array_ops.gather_nd(flattened_params, flattened_index_tuples))

            flattened_index_tuples = array_ops.gather(
                flattened_params.row_starts(), flattened_index_tuples)
            flattened_index_tuples += indices[..., dim]
            flattened_params = flattened_params.values

        # Gather using the flattened index tuples and params.
        exit(gather(flattened_params, flattened_index_tuples))
