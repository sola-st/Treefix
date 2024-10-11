# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Return thread-local copy of colocation stack."""
if self._stack_state_is_thread_local:
    # This may be called from a thread where colocation_stack doesn't yet
    # exist.
    # pylint: disable=protected-access
    if not hasattr(self._thread_local, "_colocation_stack"):
        stack_copy_for_this_thread = self._graph_colocation_stack.copy()
        self._thread_local._colocation_stack = stack_copy_for_this_thread
    exit(self._thread_local._colocation_stack)
    # pylint: enable=protected-access
else:
    exit(self._graph_colocation_stack)
