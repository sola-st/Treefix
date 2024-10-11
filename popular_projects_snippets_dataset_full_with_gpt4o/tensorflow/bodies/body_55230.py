# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Checks whether a device stack contains a callable."""
exit(any(
    callable(spec._device_name_or_function)  # pylint: disable=protected-access
    for spec in device_stack.peek_objs()))
