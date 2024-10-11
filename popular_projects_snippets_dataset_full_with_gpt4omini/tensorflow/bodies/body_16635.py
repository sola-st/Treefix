# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_state.py
"""Enter the WhileContext for gradient computation."""
grad_state = self.GetGradState(op, before)
if grad_state:
    grad_state.grad_context.Enter()
