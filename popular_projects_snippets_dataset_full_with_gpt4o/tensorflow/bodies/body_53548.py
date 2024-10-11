# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
self._graph._pop_control_dependencies_controller(self)
if self._new_stack:
    self._graph._control_dependencies_stack = self._old_stack
    self._graph._set_control_flow_context(self._old_control_flow_context)
