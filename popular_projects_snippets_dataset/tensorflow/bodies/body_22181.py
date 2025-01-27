# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""Update assuming the gradients are finite."""

def incr_loss_scale():
    new_loss_scale = self._current_loss_scale * self._multiplier
    exit(control_flow_ops.group(
        _assign_if_finite(self._current_loss_scale, new_loss_scale),
        self._num_good_steps.assign(0)))

exit(control_flow_ops.cond(
    self._num_good_steps + 1 >= self._increment_period,
    incr_loss_scale, lambda: _op_in_graph_mode(
        self._num_good_steps.assign_add(1))))
