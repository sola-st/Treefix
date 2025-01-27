# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Repeats elements of `data`.

  Args:
    data: An `N`-dimensional tensor.
    repeats: A 1-D integer tensor specifying how many times each element in
      `axis` should be repeated.  `len(repeats)` must equal `data.shape[axis]`.
      Supports broadcasting from a scalar value.
    axis: `int`.  The axis along which to repeat values.  Must be less than
      `max(N, 1)`.
    name: A name for the operation.

  Returns:
    A tensor with `max(N, 1)` dimensions.  Has the same shape as `data`,
    except that dimension `axis` has size `sum(repeats)`.

  Example usage:

  >>> repeat(['a', 'b', 'c'], repeats=[3, 0, 2], axis=0)
  <tf.Tensor: shape=(5,), dtype=string,
  numpy=array([b'a', b'a', b'a', b'c', b'c'], dtype=object)>
  >>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=0)
  <tf.Tensor: shape=(5, 2), dtype=int32, numpy=
  array([[1, 2],
         [1, 2],
         [3, 4],
         [3, 4],
         [3, 4]], dtype=int32)>
  >>> repeat([[1, 2], [3, 4]], repeats=[2, 3], axis=1)
  <tf.Tensor: shape=(2, 5), dtype=int32, numpy=
  array([[1, 1, 2, 2, 2],
         [3, 3, 4, 4, 4]], dtype=int32)>

  """
# Whether the execution uses the optimized non-XLA implementation below.
# TODO(b/236387200): Separate the implementations at a lower level, so that
# non-XLA path gets the performance benefits and the XLA path is not broken
# after loading a saved model with the optimization.
use_optimized_non_xla_implementation = False

if not isinstance(axis, int):
    raise TypeError("Argument `axis` must be an int. "
                    f"Received `axis` = {axis} of type {type(axis).__name__}")

with ops.name_scope(name, "Repeat", [data, repeats]):
    data = ops.convert_to_tensor(data, name="data")
    # Note: We want to pass dtype=None to convert_to_int_tensor so that the
    # existing type is maintained instead of force-casting to int32. However,
    # this is not compatible with the implementation used on the XLA path.
    if not use_optimized_non_xla_implementation:
        repeats = convert_to_int_tensor(repeats, name="repeats")
    else:
        repeats = convert_to_int_tensor(repeats, name="repeats", dtype=None)

    repeats.shape.with_rank_at_most(1)

    # If `data` is a scalar, then upgrade it to a vector.
    data = _with_nonzero_rank(data)
    data_shape = shape(data, out_type=repeats.dtype)

    # If `axis` is negative, then convert it to a positive value.
    axis = get_positive_axis(axis, data.shape.rank, ndims_name="rank(data)")

    # If we know that `repeats` is a scalar, then we can just tile & reshape.
    if repeats.shape.num_elements() == 1:
        repeats = reshape(repeats, [])
        expanded = expand_dims(data, axis + 1)
        tiled = tile_one_dimension(expanded, axis + 1, repeats)
        result_shape = concat([
            data_shape[:axis], [repeats * data_shape[axis]], data_shape[axis + 1:]
        ],
                              axis=0)
        exit(reshape(tiled, result_shape))

    # Check data Tensor shapes.
    if repeats.shape.ndims == 1:
        data.shape.dims[axis].assert_is_compatible_with(repeats.shape[0])

    repeats = broadcast_to(repeats, [data_shape[axis]])

    # The implementation on the else branch has better performance. However, it
    # does not work on the XLA path since it relies on the range op with a
    # shape that is not a compile-time constant.
    if not use_optimized_non_xla_implementation:
        repeats_original = repeats

        # Broadcast the `repeats` tensor so rank(repeats) == axis + 1.
        if repeats.shape.ndims != axis + 1:
            repeats_shape = shape(repeats)
            repeats_ndims = rank(repeats)
            broadcast_shape = concat(
                [data_shape[:axis + 1 - repeats_ndims], repeats_shape], axis=0)
            repeats = broadcast_to(repeats, broadcast_shape)
            repeats.set_shape([None] * (axis + 1))

        # Create a "sequence mask" based on `repeats`, where slices across `axis`
        # contain one `True` value for each repetition.  E.g., if
        # `repeats = [3, 1, 2]`, then `mask = [[1, 1, 1], [1, 0, 0], [1, 1, 0]]`.
        max_repeat = gen_math_ops._max(repeats, _all_dimensions(repeats))
        max_repeat = gen_math_ops.maximum(
            ops.convert_to_tensor(0, name="zero", dtype=max_repeat.dtype),
            max_repeat)

        mask = sequence_mask(repeats, max_repeat)

        # Add a new dimension around each value that needs to be repeated, and
        # then tile that new dimension to match the maximum number of repetitions.
        expanded = expand_dims(data, axis + 1)
        tiled = tile_one_dimension(expanded, axis + 1, max_repeat)

        # Use `boolean_mask` to discard the extra repeated values.  This also
        # flattens all dimensions up through `axis`.
        masked = boolean_mask(tiled, mask)

        # Reshape the output tensor to add the outer dimensions back.
        if axis == 0:
            result = masked
        else:
            repeated_dim_size = gen_math_ops._sum(
                repeats_original,
                axis=gen_math_ops._range(0, rank(repeats_original), 1))
            result_shape = concat(
                [data_shape[:axis], [repeated_dim_size], data_shape[axis + 1:]],
                axis=0)
            result = reshape(masked, result_shape)

        # Preserve shape information.
        if data.shape.ndims is not None:
            new_axis_size = 0 if repeats.shape[0] == 0 else None
            result.set_shape(data.shape[:axis].concatenate(
                [new_axis_size]).concatenate(data.shape[axis + 1:]))

        exit(result)

    else:
        # Non-XLA path implementation
        # E.g., repeats = [3, 4, 0, 2, 1].
        # E.g., repeats_scan = [3, 7, 7, 9, 10].
        repeats_scan = math_ops.cumsum(repeats)
        # This concat just prepends 0 to handle the case when repeats are empty.
        # E.g., output_size = [0, 3, 7, 7, 9, 10][-1] = 10.
        output_size = concat([zeros(1, dtype=repeats_scan.dtype), repeats_scan],
                             axis=0)[-1]
        # E.g., output_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
        output_indices = math_ops.range(output_size, dtype=repeats.dtype)
        # E.g., gather_indices = [0, 0, 0, 1, 1, 1, 1, 3, 3, 4].
        gather_indices = searchsorted(
            repeats_scan, output_indices, side="right", out_type=repeats.dtype)
        exit(gather(data, gather_indices, axis=axis))
