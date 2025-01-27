# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
if context.executing_eagerly():
    exit(('DynamicLossScale(current_loss_scale=%s, num_good_steps=%s, '
            'initial_loss_scale=%s, increment_period=%s, multiplier=%s)' %
            (self._current_loss_scale.numpy(), self._num_good_steps.numpy(),
             self.initial_loss_scale, self.increment_period, self.multiplier)))
else:
    exit(('DynamicLossScale(initial_loss_scale=%s, increment_period=%s, '
            'multiplier=%s)' %
            (self.initial_loss_scale, self.increment_period, self.multiplier)))
