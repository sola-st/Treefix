# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""gather_nd implementation with batch support."""
with ops.name_scope(name, "BatchGatherND", [params, indices]):
    indices = ops.convert_to_tensor(indices, name="indices")
    params = ops.convert_to_tensor(params, name="params")

    if not isinstance(batch_dims, int):
        raise TypeError(f"Argument `batch_dims` must be an int; got {batch_dims}")
    if batch_dims < 0:
        raise ValueError("tf.gather_nd does not allow negative batch_dims.")
    params_ndims = params.shape.ndims
    indices_ndims = indices.shape.ndims
    if indices_ndims is not None and batch_dims >= indices_ndims:
        raise ValueError(f"Argument `batch_dims` = {batch_dims} must be "
                         f"less than rank(`indices`) = {indices_ndims}")
    if params_ndims is not None and batch_dims >= params_ndims:
        raise ValueError(f"Argument `batch_dims` = {batch_dims} must be "
                         f"less than rank(`params`) = {params_ndims}")

    expand = batch_dims == 0
    if expand:
        # Normally gather_nd will be called when batch_dims == 0.
        # But if this function is called with batch_dims = 0, e.g. for testing
        # purposes, this adds a dummy batch dimension to make batch_dims = 1.
        params = expand_dims(params, axis=0)
        indices = expand_dims(indices, axis=0)
        batch_dims = 1

    params_shape = shape(params)
    indices_shape = shape(indices)
    batch_shape = params_shape[:batch_dims]
    batch_size = gen_math_ops.prod(batch_shape, [0])
    index_internal_ndims = rank(indices) - batch_dims - 1
    indices_internal_shape = indices_shape[batch_dims:-1]

    # Assuming a 'params' with shape [b1, ..., bM, g1, ..., gN] and an 'indices'
    # with shape [b1, ..., bM, i1, ..., iK, C], where C <= N, we need to modify
    # 'indices' s.t. it has shape [i1, ..., iK, D], where D <= M + N and slices
    # to the entire 'params' tensor.
    # Assuming we have a batch of shape [B1, B2], we use meshgrid to create a
    # grid of size B1 x B2.
    batch_dim_list = unstack(batch_shape, axis=0)
    dim_ranges = [
        gen_math_ops.cast(gen_math_ops._range(0, x, 1), indices.dtype)
        for x in batch_dim_list
    ]
    mesh_list = meshgrid(*dim_ranges, indexing="ij") if dim_ranges else []
    # Then we flatten and stack the tensors to form a (B1.B2) by 2 matrix.
    flat_list = [reshape(x, shape=(-1,)) for x in mesh_list]
    index_grid = transpose(stack(flat_list, axis=0))
    # We need to concatenate these batch coordinates with the internal indices.
    # concat -> index_grid [B1.B2, 2] with indices [i1, ..., iK, C]
    # So we reshape them both to [(B1.B2), i1, ..., iK, *]
    index_grid_shape = shape(index_grid)
    index_grid = reshape(
        index_grid,
        concat([
            index_grid_shape[:1],
            ones(index_internal_ndims, dtype=dtypes.int32), index_grid_shape[1:]
        ],
               axis=0))
    tile_shape = concat(((1,), indices_internal_shape, (1,)), axis=0)
    index_grid = tile(index_grid, multiples=tile_shape)
    # index_grid now has shape [(B1.B2), i1, ..., iK, 2]
    flat_shape = concat(([batch_size], indices_shape[batch_dims:]), axis=0)
    flat_indices = reshape(indices, shape=flat_shape)
    # flat_indices now has shape [(B1.B2), i1, ..., iK, C]
    indices = concat((index_grid, flat_indices), axis=-1)
    # indices has shape [(B1.B2), i1, ..., iK, 2+C]
    out = gen_array_ops.gather_nd(params, indices)
    # out has shape [(B1.B2), i1, ..., iK, N-C]. Now we reshape batch to
    # its original form.
    out_shape = shape(out)
    out = reshape(out, shape=concat((batch_shape, out_shape[1:]), axis=0))
    if expand:
        out = squeeze(out, axis=0)
exit(out)
