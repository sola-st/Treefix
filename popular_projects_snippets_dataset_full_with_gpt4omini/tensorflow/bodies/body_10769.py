# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
if self.GetWhileContext():
    exit(self.GetWhileContext().grad_state)
exit(None)
