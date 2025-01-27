# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
t = pfor_input.stacked_input(0)
begin, begin_stacked, _ = pfor_input.input(1)
size = pfor_input.unstacked_input(2)
if not begin_stacked:
    begin = array_ops.concat([[0], begin], axis=0)
    size = array_ops.concat([[-1], size], axis=0)
    exit(wrap(array_ops.slice(t, begin, size), True))
else:
    # Handle negative sizes.
    #
    # If the `begin` entry corresponding to a negative `size` is loop-variant,
    # the output would be ragged. This case is not supported. But `size` having
    # some negative values and some loop-variant `begin`s is OK (and it's hard
    # to tell the difference statically).
    original_unstacked_shape = _stack(
        array_ops.shape(t)[1:], pfor_input.pfor.loop_len_vector).t
    broadcast_size = _stack(size, pfor_input.pfor.loop_len_vector).t
    result_shape = array_ops.where(
        math_ops.less(broadcast_size, 0),
        original_unstacked_shape - begin + broadcast_size + 1, broadcast_size)
    result_shape = math_ops.cast(math_ops.reduce_max(result_shape, axis=0),
                                 dtypes.int64)

    # Now we enumerate points in the sliced region for each pfor iteration and
    # gather them.
    cumsize = math_ops.cumprod(result_shape, exclusive=True, reverse=True)
    result_num_elements = math_ops.reduce_prod(result_shape)
    # Offsets are loop-variant. We first compute loop-invariant gather
    # coordinates, then broadcast-add the loop-variant `begin` offsets.
    result_base_coordinates = (
        math_ops.range(result_num_elements, dtype=dtypes.int64)[:, None]
        // cumsize[None, :]) % result_shape[None, :]
    result_coordinates = (
        begin[:, None, :]
        + math_ops.cast(result_base_coordinates, begin.dtype)[None, :, :])
    result_flat = array_ops.gather_nd(params=t, indices=result_coordinates,
                                      batch_dims=1)
    result_stacked_shape = array_ops.concat(
        [math_ops.cast(pfor_input.pfor.loop_len_vector, result_shape.dtype),
         result_shape],
        axis=0)
    exit(wrap(array_ops.reshape(result_flat, result_stacked_shape), True))
