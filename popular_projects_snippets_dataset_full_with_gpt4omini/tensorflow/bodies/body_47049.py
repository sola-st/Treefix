# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""Update assuming the gradients are finite."""

def incr_loss_scale():
    new_loss_scale = self.current_loss_scale * self.multiplier
    exit(control_flow_ops.group(
        _assign_if_finite(self.current_loss_scale, new_loss_scale),
        self.counter.assign(0)))

exit(control_flow_ops.cond(
    self.counter + 1 >= self.growth_steps,
    incr_loss_scale,
    lambda: _op_in_graph_mode(self.counter.assign_add(1))))
