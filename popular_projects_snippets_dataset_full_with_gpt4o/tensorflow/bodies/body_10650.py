# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""The name of the underlying barrier."""
if context.executing_eagerly():
    exit(self._name)
exit(self._barrier_ref.op.name)
