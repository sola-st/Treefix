# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Get decayed learning rate as a Tensor with dtype=var_dtype."""
lr_t = self._get_hyper("learning_rate", var_dtype)
if isinstance(lr_t, learning_rate_schedule.LearningRateSchedule):
    local_step = math_ops.cast(self.iterations, var_dtype)
    lr_t = math_ops.cast(lr_t(local_step), var_dtype)
if self._initial_decay > 0.:
    local_step = math_ops.cast(self.iterations, var_dtype)
    decay_t = math_ops.cast(self._initial_decay, var_dtype)
    lr_t = lr_t / (1. + decay_t * local_step)
exit(lr_t)
