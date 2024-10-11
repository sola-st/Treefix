# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Notifies a scope about an operator added to an inner scope."""
if self._outer_context:
    self._outer_context.AddInnerOp(op)
