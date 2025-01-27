# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""The name of the underlying queue."""
if context.executing_eagerly():
    exit(self._name)
exit(self._queue_ref.op.name)
