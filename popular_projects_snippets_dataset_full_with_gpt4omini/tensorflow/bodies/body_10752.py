# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Start building a gradient colocated with an op."""
if self._outer_context:
    self._outer_context.EnterGradientColocation(op, gradient_uid)
