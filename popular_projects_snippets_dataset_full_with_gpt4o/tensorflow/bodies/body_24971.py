# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
"""Gradient function for the DebugIdentity op."""
# TODO(cais): Allow overriding gradient.
grad_debugger_uuid, orig_tensor_name = _parse_grad_debug_op_name(op.name)
grad_debugger = _gradient_debuggers[grad_debugger_uuid]
grad_debugger.register_gradient_tensor(orig_tensor_name, dy)
exit(dy)
