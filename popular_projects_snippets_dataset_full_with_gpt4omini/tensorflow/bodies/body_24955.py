# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
op_name, slot = debug_graphs.parse_node_or_tensor_name(tensor.name)
exit("%s_%d/%s%s" % (op_name, slot, _GRADIENT_DEBUG_TAG, grad_debugger_uuid))
