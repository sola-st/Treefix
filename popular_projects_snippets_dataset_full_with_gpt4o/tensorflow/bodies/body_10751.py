# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Exit this control flow context."""
graph = ops.get_default_graph()
last_context = self._context_stack.pop()
graph._set_control_flow_context(last_context)
