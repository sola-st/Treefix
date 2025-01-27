# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/multi_device_iterator_ops.py
if context.executing_eagerly():
    exit(control_flow_ops.no_op())
exit(self._initializer)
