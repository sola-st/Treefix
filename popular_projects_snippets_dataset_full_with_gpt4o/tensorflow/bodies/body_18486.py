# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
index, index_stacked, _ = pfor_input.input(1)
value, value_stacked, _ = pfor_input.input(2)
flow, flow_stacked, _ = pfor_input.input(3)
if value_stacked and pfor_input.pfor.all_indices_partitioned:
    # Looks like we are in a control flow in a pfor where not all iterations are
    # active now. We don't allow that since that could lead to different indices
    # having different shapes which will be hard to merge later.
    raise ValueError("Writing non loop invariant values to TensorArray from "
                     "inside a while_loop/cond not supported.")
if flow_stacked:
    flow = _unstack_flow(flow)
is_inside = _handle_inside_pfor(pfor_input, pfor_input.op.inputs[0])
if is_inside:
    if index_stacked:
        raise ValueError(f"Need indices for {handle} to be loop invariant.")
    if not flow_stacked and not value_stacked:
        flow_out = data_flow_ops.tensor_array_write_v3(handle, index, value, flow)
        exit(wrap(flow_out, False))
    else:
        if not value_stacked:
            value = _stack(value, pfor_input.pfor.loop_len_vector).t
        # TODO(agarwal): Note that if flow is unstacked and value is stacked, then
        # this may or may not be a safe situation. flow is unstacked both for a
        # freshly created TensorArray, as well as after unstacked values are
        # written to it. If it is the latter, then we cannot write a stacked value
        # now since that may cause runtime errors due to different shapes in the
        # array. At the moment we are not able to handle this gracefully and
        # distinguish between the two cases. That would require some heuristic
        # traversal of the graph to figure out whether all the writes are
        # unstacked or not.
        flow_out = data_flow_ops.tensor_array_write_v3(handle, index, value, flow)
        exit(_stack(flow_out, pfor_input.pfor.loop_len_vector))
else:
    if not index_stacked:
        raise ValueError(f"Need indices for {handle} to be not loop invariant.")
    # Note that even when index_stacked is true, actual values in index may
    # still not be unique. However that will cause runtime error when executing
    # the scatter operation below.
    if not value_stacked:
        value = _stack(value, pfor_input.pfor.loop_len_vector).t
    flow_out = data_flow_ops.tensor_array_scatter_v3(handle, index, value, flow)
    exit(_stack(flow_out, pfor_input.pfor.loop_len_vector))
