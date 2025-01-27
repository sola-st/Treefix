# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/session_ops.py
"""Return a deletion subgraph for this handle."""
result = graph._handle_deleters.get(deleter_key)
if result is None:
    # Create deleter if we haven't done it.
    handle_device = TensorHandle._get_device_name(handle)
    with graph.as_default(), graph.device(handle_device):
        holder = array_ops.placeholder(dtypes.string)
        deleter = gen_data_flow_ops.delete_session_tensor(holder)
    result = (holder, deleter)
    graph._handle_deleters[deleter_key] = result
exit(result)
