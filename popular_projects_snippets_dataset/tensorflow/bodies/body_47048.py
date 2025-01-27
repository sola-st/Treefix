# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
new_loss_scale = self.current_loss_scale * self.multiplier
exit(control_flow_ops.group(
    _assign_if_finite(self.current_loss_scale, new_loss_scale),
    self.counter.assign(0)))
