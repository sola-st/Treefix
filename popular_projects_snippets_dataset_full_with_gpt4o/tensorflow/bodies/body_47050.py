# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""Update assuming the gradients are nonfinite."""

new_loss_scale = math_ops.maximum(
    self.current_loss_scale / self.multiplier, 1)
exit(control_flow_ops.group(
    self.counter.assign(0),
    self.current_loss_scale.assign(new_loss_scale)))
