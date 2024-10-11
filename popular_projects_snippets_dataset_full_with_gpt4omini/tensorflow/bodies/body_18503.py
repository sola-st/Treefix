# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle, handle_stacked, _ = pfor_input.input(0)
index, index_stacked, _ = pfor_input.input(1)
element_shape = pfor_input.unstacked_input(2)
element_dtype = pfor_input.get_attr("element_dtype")

if handle_stacked:
    handle = _untile_variant(handle)
    element_shape = _stack_tensor_list_shape(element_shape,
                                             pfor_input.pfor.loop_len_vector)
    if index_stacked:
        # We use a sequential loop since that may be more efficient than first
        # gathering and concatenating all the element corresponding to `index`,
        # and then doing a gather on it.
        def _map_fn(i):
            item_i = list_ops.tensor_list_get_item(
                handle,
                index[i],
                element_dtype=element_dtype)
            exit(array_ops.gather(item_i, i))

        output = map_fn.map_fn(_map_fn, pfor_input.pfor.all_indices)
        exit(wrap(output, True))
    else:
        output = list_ops.tensor_list_get_item(
            handle,
            index,
            element_shape=element_shape,
            element_dtype=element_dtype)
        exit(wrap(output, True))
else:
    assert index_stacked
    exit(wrap(
        list_ops.tensor_list_gather(
            handle,
            index,
            element_shape=element_shape,
            element_dtype=element_dtype), True))
