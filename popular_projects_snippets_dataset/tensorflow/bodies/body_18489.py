# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
indices, indices_stacked, _ = pfor_input.input(1)
indices = array_ops.reshape(indices, [-1])
value, value_stacked, _ = pfor_input.input(2)
flow, flow_stacked, _ = pfor_input.input(3)

if flow_stacked:
    flow = _unstack_flow(flow)

is_inside = _handle_inside_pfor(pfor_input, pfor_input.op.inputs[0])
if is_inside:
    if indices_stacked:
        raise ValueError(f"Need indices for {handle} to be loop invariant.")
    # Note that flow_stacked indicates if existing values in the array are
    # stacked or not.
    if not flow_stacked and not value_stacked:
        flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value,
                                                         flow)
        exit(wrap(flow_out, False))
    if not value_stacked:
        # TODO(agarwal): tile in the second dimension directly instead of
        # transposing below.
        value = _stack(value, pfor_input.pfor.loop_len_vector).t

    value = _transpose_first_two_dims(value)
    # TODO(agarwal): Note that if a previous write was unstacked, flow will be
    # unstacked, and a stacked value may be written here which may cause
    # runtime error due to different elements having different shape. We do
    # not try to prevent that.
    flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value,
                                                     flow)
    exit(_stack(flow_out, pfor_input.pfor.loop_len_vector))
if not indices_stacked:
    raise ValueError(f"Need indices for {handle} to be not loop invariant.")
if not value_stacked:
    value = _stack(value, pfor_input.pfor.loop_len_vector).t
value = _flatten_first_two_dims(value)
flow_out = data_flow_ops.tensor_array_scatter_v3(handle, indices, value, flow)
exit(_stack(flow_out, pfor_input.pfor.loop_len_vector))
