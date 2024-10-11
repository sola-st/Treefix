# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
indices, indices_stacked, _ = pfor_input.input(1)
indices = array_ops.reshape(indices, [-1])
flow, flow_stacked, _ = pfor_input.input(2)
if flow_stacked:
    flow = _unstack_flow(flow)
dtype = pfor_input.get_attr("dtype")
# TODO(agarwal): support element_shape attr?

n = pfor_input.pfor.loop_len_vector
value = data_flow_ops.tensor_array_gather_v3(
    handle, indices, flow, dtype=dtype)
is_inside = _handle_inside_pfor(pfor_input, pfor_input.op.inputs[0])
if is_inside:
    # flow_stacked indicates if values in the TensorArray are stacked or not.
    if indices_stacked:
        if flow_stacked:
            raise ValueError(
                "It looks like TensorArrayGatherV3 was called on a TensorArray "
                "whose values are not loop-invariant, and the indices were also "
                "not loop invariant. This is currently unsupported.")
        else:
            value = _unflatten_first_dim(value, n)
            exit(wrap(value, True))
    else:
        if flow_stacked:
            # Since elements in this array are stacked and `value` was produced by
            # gather, its first two dims are "gathered elements" and "stack
            # dimension". Our semantics require these two to be flipped.
            value = _transpose_first_two_dims(value)
        exit(wrap(value, flow_stacked))
else:
    # Values in the TensorArray should be unstacked (since different iterations
    # couldn't write to the same location). So whether output is stacked or not
    # depends on indices_stacked.
    if indices_stacked:
        value = _unflatten_first_dim(value, n)
    exit(wrap(value, indices_stacked))
