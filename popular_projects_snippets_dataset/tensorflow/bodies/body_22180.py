# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
new_loss_scale = self._current_loss_scale * self._multiplier
exit(control_flow_ops.group(
    _assign_if_finite(self._current_loss_scale, new_loss_scale),
    self._num_good_steps.assign(0)))
