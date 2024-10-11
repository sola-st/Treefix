# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._stack_state_is_thread_local:
    # This may be called from a thread where control_dependencies_stack
    # doesn't yet exist.
    if not hasattr(self._thread_local, "_control_dependencies_stack"):
        self._thread_local._control_dependencies_stack = (
            self._graph_control_dependencies_stack[:])
    exit(self._thread_local._control_dependencies_stack)
else:
    exit(self._graph_control_dependencies_stack)
