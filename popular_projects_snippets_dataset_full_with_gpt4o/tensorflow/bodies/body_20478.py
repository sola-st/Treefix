# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
if not self._outer_device_function_stack:
    # Capture the device function stack at the time of first entry
    # since that is the stack that will be used outside_compilation.
    graph = ops.get_default_graph()
    # pylint: disable=protected-access
    self._outer_device_function_stack = graph._device_function_stack.copy()
    # pylint: enable=protected-access
super(TPUReplicateContext, self).Enter()
