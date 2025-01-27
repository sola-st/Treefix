# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
shift, shift_stacked, _ = pfor_input.input(1)
axis = pfor_input.unstacked_input(2)
if not shift_stacked:
    exit(wrap(manip_ops.roll(t, shift, axis + 1), True))
else:
    # `axis` and `shift` may both be vectors, with repeated axes summing the
    # corresponding `shift`s. We scatter shifts into a dense array of shape
    # [loop_len, num_unstacked_axes] indicating the offset for each axis.
    num_unstacked_axes = math_ops.cast(array_ops.rank(t), dtypes.int64) - 1
    axis = math_ops.cast(array_ops.reshape(axis, [-1]), dtypes.int64)
    loop_len = math_ops.cast(pfor_input.pfor.loop_len_vector[0], dtypes.int64)
    shift = math_ops.cast(array_ops.reshape(shift, [loop_len, -1]),
                          dtypes.int64)
    axis_segment_ids = (
        math_ops.range(loop_len, dtype=dtypes.int64)[:, None]
        * num_unstacked_axes + axis[None, :])
    axis_offsets = array_ops.reshape(
        math_ops.unsorted_segment_sum(
            data=shift, segment_ids=axis_segment_ids,
            num_segments=loop_len * num_unstacked_axes),
        [loop_len, num_unstacked_axes])

    # Determine the coordinates in the input array of each result and gather
    # them.
    unstacked_shape = array_ops.shape(t, out_type=dtypes.int64)[1:]
    cumsize = math_ops.cumprod(unstacked_shape, exclusive=True, reverse=True)
    num_unstacked_elements = math_ops.reduce_prod(unstacked_shape)
    result_coordinates = (
        (math_ops.range(num_unstacked_elements,
                        dtype=dtypes.int64)[None, :, None]
         // cumsize[None, None, :] - axis_offsets[:, None, :])
        % unstacked_shape[None, None, :])
    result_flat = array_ops.gather_nd(params=t, indices=result_coordinates,
                                      batch_dims=1)
    exit(wrap(array_ops.reshape(result_flat, array_ops.shape(t)),
                True))
