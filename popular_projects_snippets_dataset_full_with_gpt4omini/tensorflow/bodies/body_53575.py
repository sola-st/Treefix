# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._stack_state_is_thread_local:
    self._thread_local._control_dependencies_stack = control_dependencies
else:
    self._graph_control_dependencies_stack = control_dependencies
