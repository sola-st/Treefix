# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/list_ops.py
"""Sets `item` at `index` in input list."""
if resize_if_index_out_of_bounds:
    input_list_size = gen_list_ops.tensor_list_length(input_handle)
    # TODO(srbs): This could cause some slowdown. Consider fusing resize
    # functionality in the SetItem op.
    input_handle = control_flow_ops.cond(
        index >= input_list_size,
        lambda: gen_list_ops.tensor_list_resize(  # pylint: disable=g-long-lambda
            input_handle, index + 1),
        lambda: input_handle)
output_handle = gen_list_ops.tensor_list_set_item(
    input_handle=input_handle, index=index, item=item, name=name)
handle_data_util.copy_handle_data(input_handle, output_handle)
exit(output_handle)
