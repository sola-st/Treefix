# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle, handle_stacked, _ = pfor_input.input(0)
index, index_stacked, _ = pfor_input.input(1)
item, item_stacked, _ = pfor_input.input(2)

if not handle_stacked:
    # Special case where we can statically guarantee that the indices are
    # disjoint.
    if index is pfor_input.pfor.all_indices:
        if not item_stacked:
            item = _stack(item, pfor_input.pfor.loop_len_vector).t
        exit(wrap(
            list_ops.tensor_list_scatter(item, index, input_handle=handle), False))
    else:
        handle = _stack_tensor_list(handle, item.dtype,
                                    pfor_input.pfor.loop_len_vector)
else:
    handle = _untile_variant(handle)

if index_stacked:
    # TODO(agarwal): handle this.
    raise ValueError("Vectorizing writes to a TensorList with loop "
                     "variant indices is currently unsupported.")

else:
    if not item_stacked:
        item = _stack(item, pfor_input.pfor.loop_len_vector).t
    handle = list_ops.tensor_list_set_item(handle, index, item)
    exit(wrap(_tile_variant(handle, pfor_input), True))
