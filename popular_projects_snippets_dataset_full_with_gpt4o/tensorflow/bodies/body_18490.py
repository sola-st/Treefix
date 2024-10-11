# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
flow, flow_stacked, _ = pfor_input.input(1)
if flow_stacked:
    flow = _unstack_flow(flow)
source = pfor_input.get_attr("source")
# TODO(agarwal): For now, we assume that gradients are stacked if the
# TensorArrayGradV3 call is being done inside the pfor. Getting that wrong
# will give runtime error due to incorrect shape being written to the
# accumulator. It is difficult to know in advance if gradients written will be
# stacked or not. Note that flow being stacked is not indicative of the
# gradient being stacked or not. Revisit this later.
shape_to_prepend = pfor_input.pfor.loop_len_vector
grad_handle, flow_out = data_flow_ops.tensor_array_grad_with_shape(
    handle=handle,
    flow_in=flow,
    shape_to_prepend=shape_to_prepend,
    source=source)
flow_out = _stack(flow_out, pfor_input.pfor.loop_len_vector).t
exit([wrap(grad_handle, False), wrap(flow_out, True)])
