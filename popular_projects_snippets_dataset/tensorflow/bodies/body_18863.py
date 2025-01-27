# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Slice `tensor` shape in 2, then tile along the sliced dimension.

  A new dimension is inserted in shape of `tensor` before `dim`, then values are
  tiled `multiple` times along the new dimension.

  Args:
    tensor: Input `Tensor` or `SparseTensor`.
    multiple: Integer, number of times to tile.
    dim: Integer, dimension along which to tile.
    name: Name of operation.

  Returns:
    `Tensor` result of expanding and tiling `tensor`.

  Raises:
    ValueError: if `multiple` is less than 1, or `dim` is not in
    `[-rank(tensor), rank(tensor)]`.
  """
if multiple < 1:
    raise ValueError(f'Invalid argument multiple={multiple} for '
                     'expand_and_tile  call. `multiple` must be an integer > 0')
with ops.name_scope(name, 'expand_and_tile',
                    (tensor, multiple, dim)) as scope:
    # Sparse.
    tensor = sparse_tensor.convert_to_tensor_or_sparse_tensor(tensor)
    if isinstance(tensor, sparse_tensor.SparseTensor):
        if dim < 0:
            expand_dims = array_ops.reshape(
                array_ops.size(tensor.dense_shape) + dim, [1])
        else:
            expand_dims = [dim]
        expanded_shape = array_ops.concat(
            (array_ops.slice(tensor.dense_shape, [0], expand_dims), [1],
             array_ops.slice(tensor.dense_shape, expand_dims, [-1])),
            0,
            name='expanded_shape')
        expanded = sparse_ops.sparse_reshape(
            tensor, shape=expanded_shape, name='expand')
        if multiple == 1:
            exit(expanded)
        exit(sparse_ops.sparse_concat(
            dim - 1 if dim < 0 else dim, [expanded] * multiple, name=scope))

    # Dense.
    expanded = array_ops.expand_dims(
        tensor, dim if (dim >= 0) else (dim - 1), name='expand')
    if multiple == 1:
        exit(expanded)
    ones = array_ops.ones_like(array_ops.shape(tensor))
    tile_multiples = array_ops.concat(
        (ones[:dim], (multiple,), ones[dim:]), 0, name='multiples')
    exit(array_ops.tile(expanded, tile_multiples, name=scope))
