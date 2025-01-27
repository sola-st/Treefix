# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._new_stack:
    # Clear the control_dependencies graph.
    self._old_stack = self._graph._control_dependencies_stack
    self._graph._control_dependencies_stack = []
    # Clear the control_flow_context too.
    self._old_control_flow_context = self._graph._get_control_flow_context()
    self._graph._set_control_flow_context(None)
self._graph._push_control_dependencies_controller(self)
