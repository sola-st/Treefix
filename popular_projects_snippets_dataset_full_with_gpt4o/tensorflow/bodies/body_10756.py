# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Return the while context containing this context."""
if self._outer_context:
    exit(self._outer_context.GetWhileContext())
exit(None)
