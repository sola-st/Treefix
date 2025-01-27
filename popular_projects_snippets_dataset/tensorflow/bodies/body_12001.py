# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/state_ops.py
"""Generalization of `tf.compat.v1.scatter_update` to axis different than 0.

  Analogous to `batch_gather`. This assumes that `ref`, `indices` and `updates`
  have a series of leading dimensions that are the same for all of them, and the
  updates are performed on the last dimension of indices. In other words, the
  dimensions should be the following:

  `num_prefix_dims = indices.ndims - 1`
  `batch_dim = num_prefix_dims + 1`
  `updates.shape = indices.shape + var.shape[batch_dim:]`

  where

  `updates.shape[:num_prefix_dims]`
  `== indices.shape[:num_prefix_dims]`
  `== var.shape[:num_prefix_dims]`

  And the operation performed can be expressed as:

  `var[i_1, ..., i_n, indices[i_1, ..., i_n, j]] = updates[i_1, ..., i_n, j]`

  When indices is a 1D tensor, this operation is equivalent to
  `tf.compat.v1.scatter_update`.

  To avoid this operation there would be 2 alternatives:
  1) Reshaping the variable by merging the first `ndims` dimensions. However,
     this is not possible because `tf.reshape` returns a Tensor, which we
     cannot use `tf.compat.v1.scatter_update` on.
  2) Looping over the first `ndims` of the variable and using
     `tf.compat.v1.scatter_update` on the subtensors that result of slicing the
     first
     dimension. This is a valid option for `ndims = 1`, but less efficient than
     this implementation.

  See also `tf.compat.v1.scatter_update` and `tf.compat.v1.scatter_nd_update`.

  Args:
    ref: `Variable` to scatter onto.
    indices: Tensor containing indices as described above.
    updates: Tensor of updates to apply to `ref`.
    use_locking: Boolean indicating whether to lock the writing operation.
    name: Optional scope name string.

  Returns:
    Ref to `variable` after it has been modified.

  Raises:
    ValueError: If the initial `ndims` of `ref`, `indices`, and `updates` are
        not the same.
  """
with ops.name_scope(name):
    indices = ops.convert_to_tensor(indices, name="indices")
    indices_shape = array_ops.shape(indices)
    indices_dimensions = indices.get_shape().ndims

    if indices_dimensions is None:
        raise ValueError("batch_gather does not allow indices with unknown "
                         "shape.")

    nd_indices = array_ops.expand_dims(indices, axis=-1)
    nd_indices_list = []

    # Scatter ND requires indices to have an additional dimension, in which the
    # coordinates of the updated things are specified. For this to be adapted to
    # the scatter_update with several leading dimensions, we simply make use of
    # a tf.range for all the leading dimensions followed by concat of all the
    # coordinates we created with the original indices.

    # For example if indices.shape = [2, 3, 4], we should generate the following
    # indices for tf.compat.v1.scatter_nd_update:
    # nd_indices[:, :, 0] = [[0, 0, 0], [1, 1, 1]]
    # nd_indices[:, :, 1] = [[0, 1, 2], [0, 1, 2]]
    # nd_indices[:, :, 2] = indices
    for dimension in range(indices_dimensions - 1):
        # In this loop we generate the following for the example (one for each
        # iteration).
        # nd_indices[:, :, 0] = [[0, 0, 0], [1, 1, 1]]
        # nd_indices[:, :, 1] = [[0, 1, 2], [0, 1, 2]]
        # This is done at every iteration with a tf.range over the size of the
        # i-th dimension and using broadcasting over the desired shape.
        dimension_size = indices_shape[dimension]
        shape_to_broadcast = [1] * (indices_dimensions + 1)
        shape_to_broadcast[dimension] = dimension_size
        dimension_range = array_ops.reshape(
            gen_math_ops._range(0, dimension_size, 1), shape_to_broadcast)
        if dimension_range.dtype.base_dtype != nd_indices.dtype:
            dimension_range = gen_math_ops.cast(dimension_range, nd_indices.dtype)
        nd_indices_list.append(
            dimension_range * array_ops.ones_like(nd_indices))
    # Add the original indices at the end, as described above, and concat.
    nd_indices_list.append(nd_indices)
    final_indices = array_ops.concat(nd_indices_list, axis=-1)
    exit(scatter_nd_update(
        ref, final_indices, updates, use_locking=use_locking))
