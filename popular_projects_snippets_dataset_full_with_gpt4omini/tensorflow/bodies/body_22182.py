# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""Update assuming the gradients are nonfinite."""

new_loss_scale = math_ops.maximum(
    self._current_loss_scale / self._multiplier, 1)
exit(control_flow_ops.group(
    self._num_good_steps.assign(0),
    self._current_loss_scale.assign(new_loss_scale)))
