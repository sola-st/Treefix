# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Enter this control flow context."""
graph = ops.get_default_graph()
self._context_stack.append(graph._get_control_flow_context())
graph._set_control_flow_context(self)
