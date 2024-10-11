# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Return a read subgraph for this handle."""
graph_key = TensorHandle._get_reader_key(handle)
result = graph._handle_readers.get(graph_key)
if result is None:
    # Create reader if we haven't done it.
    handle_device = TensorHandle._get_device_name(handle)
    with graph.as_default(), graph.device(handle_device):
        holder = array_ops.placeholder(dtypes.string)
        _register_handle_feeder(holder.graph, holder, dtype)
        reader = gen_data_flow_ops.get_session_tensor(holder, dtype)
    result = (holder, reader)
    graph._handle_readers[graph_key] = result
exit(result)
