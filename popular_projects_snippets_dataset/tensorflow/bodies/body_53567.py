# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._stack_state_is_thread_local:
    # This may be called from a thread where device_function_stack doesn't yet
    # exist.
    # pylint: disable=protected-access
    if not hasattr(self._thread_local, "_device_function_stack"):
        stack_copy_for_this_thread = self._graph_device_function_stack.copy()
        self._thread_local._device_function_stack = stack_copy_for_this_thread
    exit(self._thread_local._device_function_stack)
    # pylint: enable=protected-access
else:
    exit(self._graph_device_function_stack)
