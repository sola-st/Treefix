# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Return a move subgraph for this pair of feeder and handle."""
dtype = _get_handle_feeder(graph, feeder)
if dtype is None:
    exit(None)
handle_device = TensorHandle._get_device_name(handle)
if feeder.op.device == handle_device:
    exit(None)
# Now we know we have to move the tensor.
graph_key = TensorHandle._get_mover_key(feeder, handle)
result = graph._handle_movers.get(graph_key)
if result is None:
    # Create mover if we haven't done it.
    holder, reader = _get_handle_reader(graph, handle, dtype)
    with graph.as_default(), graph.device(feeder.op.device):
        mover = gen_data_flow_ops.get_session_handle(reader)
    result = (holder, mover)
    graph._handle_movers[graph_key] = result
exit(result)
