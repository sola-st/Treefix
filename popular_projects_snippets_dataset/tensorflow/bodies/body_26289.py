# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
if context.executing_eagerly():
    exit(context.context().device_name is None)
# pylint: disable=protected-access
device_stack = ops.get_default_graph()._device_functions_outer_to_inner
# pylint: enable=protected-access
exit(not bool(device_stack))
