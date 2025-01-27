# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
index, index_stacked, _ = pfor_input.input(1)
dtype = pfor_input.get_attr("dtype")
flow, flow_stacked, _ = pfor_input.input(2)
if flow_stacked:
    flow = _unstack_flow(flow)

is_inside_pfor = _handle_inside_pfor(pfor_input, pfor_input.op.inputs[0])
if is_inside_pfor:
    # Note that if we are inside a control flow construct inside the pfor, and
    # only some of the iterations are doing the read (i.e.
    # `all_indices_partitioned` is True), then the read operation should only
    # return values for the currently active pfor iterations (`all_indices`
    # below). Hence, whenever the returned value is stacked (i.e. `flow` is
    # stacked), we may need to do an extra gather after reading the values. Also
    # note that if `is_inside` is false, then values in the tensor array are
    # unstacked. So the check is only needed in this branch.
    all_indices = pfor_input.pfor.all_indices
    all_indices_partitioned = pfor_input.pfor.all_indices_partitioned
    # Note: flow_stacked indicates if values in the TensorArray are stacked or
    # not.
    if index_stacked:
        if flow_stacked:
            raise ValueError(
                "It looks like TensorArrayReadV3 was called on a TensorArray whose"
                " values are not loop-invariant, and the read indices were also"
                " not loop invariant. This is currently unsupported.")
        value = data_flow_ops.tensor_array_gather_v3(
            handle, index, flow, dtype=dtype)
        exit(wrap(value, True))
    value = data_flow_ops.tensor_array_read_v3(handle, index, flow, dtype=dtype)
    if flow_stacked and all_indices_partitioned:
        value = array_ops.gather(value, all_indices)
    exit(wrap(value, flow_stacked))
# Values in the TensorArray should be unstacked (since different iterations
# couldn't write to the same location). So whether output is stacked or not
# depends on index_stacked.
if index_stacked:
    value = data_flow_ops.tensor_array_gather_v3(
        handle, index, flow, dtype=dtype)
else:
    value = data_flow_ops.tensor_array_read_v3(handle, index, flow, dtype=dtype)
exit(wrap(value, index_stacked))
