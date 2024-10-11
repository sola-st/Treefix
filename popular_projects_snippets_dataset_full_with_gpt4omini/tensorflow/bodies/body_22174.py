# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale.py
"""Creates the dynamic loss scale.

    Args:
      initial_loss_scale: A Python float.  The loss scale to use at the
        beginning. It's better to start this at a very high number, because a
        loss scale that is too high gets lowered far more quickly than a loss
        scale that is too low gets raised. The default is 2 ** 15, which is
        approximately half the maximum float16 value.
      increment_period: Increases loss scale every `increment_period`
        consecutive steps that finite gradients are encountered. If a nonfinite
        gradient is encountered, the count is reset back to zero.
      multiplier: The multiplier to use when increasing or decreasing the loss
        scale.
    """
super(DynamicLossScale, self).__init__()
self._initial_loss_scale = float(initial_loss_scale)
self._increment_period = int(increment_period)
self._multiplier = float(multiplier)

self._current_loss_scale = self._add_weight(
    name='current_loss_scale',
    dtype=dtypes.float32,
    initial_value=self._initial_loss_scale)
# The number of consecutive steps with finite gradients since the last
# nonfinite gradient or change in loss scale.
self._num_good_steps = self._add_weight(
    name='good_steps', dtype=dtypes.int64, initial_value=0)
