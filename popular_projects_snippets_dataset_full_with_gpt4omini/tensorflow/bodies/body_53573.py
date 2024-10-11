# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._stack_state_is_thread_local:
    # pylint: disable=protected-access
    self._thread_local._colocation_stack = colocation_stack
    # pylint: enable=protected-access
else:
    self._graph_colocation_stack = colocation_stack
