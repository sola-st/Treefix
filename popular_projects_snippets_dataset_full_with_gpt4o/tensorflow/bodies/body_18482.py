# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.unstacked_input(0)
flow, flow_stacked, _ = pfor_input.input(1)
if flow_stacked:
    flow = _unstack_flow(flow)
size = data_flow_ops.tensor_array_size_v3(handle, flow)
exit(wrap(size, False))
