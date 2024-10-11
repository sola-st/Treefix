# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if self._stack_state_is_thread_local:
    # pylint: disable=protected-access
    self._thread_local._device_function_stack = device_function_stack
    # pylint: enable=protected-access
else:
    self._graph_device_function_stack = device_function_stack
