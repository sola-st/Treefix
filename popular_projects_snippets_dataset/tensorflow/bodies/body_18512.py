# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
pfor_input.stack_inputs([1])
handle, handle_stacked, _ = pfor_input.input(0)
item = pfor_input.stacked_input(1)
indices, indices_stacked, _ = pfor_input.input(2)
if handle_stacked:
    handle = _untile_variant(handle)
else:
    handle = _stack_tensor_list(handle, item.dtype,
                                pfor_input.pfor.loop_len_vector)

item = _transpose_first_two_dims(item)
if indices_stacked:
    # Pretend the list is a dense tensor:
    #   list_as_dense: Tensor[list_len, loop_len, ...]
    # And indices are a tensor with shape (before transpose):
    #   indices: Tensor[loop_len, num_scatters]
    # The item to scatter has shape (before transpose):
    #   item: Tensor[loop_len, num_scatters, ...]
    #
    # We want list_as_dense[indices[i, j], i] = item[i, j]
    #
    # Since we're not just indexing along the first axis of `list_as_dense`, we
    # need to first extract the relevant list entries based on `indices`,
    # scatter into them according to the loop index, and re-scatter the chunks
    # we updated back into the list.
    indices = _transpose_first_two_dims(indices)
    indices_flat = array_ops.reshape(indices, [-1])
    # In many cases `indices` will be unique across pfor iterations, but this is
    # not guaranteed. If there are duplicates, we need to map multiple updates
    # to a single chunk extracted from the list. The last update should win.
    unique_indices = array_ops.unique(indices_flat)
    gathered_items = list_ops.tensor_list_gather(
        handle, unique_indices.y, element_dtype=item.dtype,
        element_shape=array_ops.shape(item)[1:])
    loop_idx = math_ops.range(pfor_input.pfor.loop_len_vector[0])
    scatters_per_op = array_ops.shape(indices)[0]

    unique_indices_loop_idx = array_ops.reshape(array_ops.tile(
        loop_idx[None, :], [scatters_per_op, 1]), [-1])
    scatter_indices = array_ops.stack(
        [unique_indices.idx, unique_indices_loop_idx],
        axis=1)
    # This op does *not* guarantee last-update-wins on GPU, so semantics may not
    # be exactly preserved for duplicate updates there.
    scattered = array_ops.tensor_scatter_nd_update(
        tensor=gathered_items,
        indices=scatter_indices,
        updates=_flatten_first_two_dims(item))
    handle = list_ops.tensor_list_scatter(
        scattered, unique_indices.y, input_handle=handle)
else:
    handle = list_ops.tensor_list_scatter(item, indices, input_handle=handle)
exit(wrap(_tile_variant(handle, pfor_input), True))
