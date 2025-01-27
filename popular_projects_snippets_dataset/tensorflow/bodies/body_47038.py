# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""Creates the dynamic loss scale."""
super(_DynamicLossScaleState, self).__init__()
self._initial_loss_scale = float(initial_loss_scale)
self._growth_steps = int(growth_steps)
self._multiplier = float(multiplier)

self._weights = {}
self._current_loss_scale = self._add_weight(
    name='current_loss_scale',
    dtype=dtypes.float32,
    initial_value=self._initial_loss_scale)
# The number of consecutive steps with finite gradients since the last
# nonfinite gradient or change in loss scale. The name is 'good_steps' for
# backwards compatibility with older checkpoints.
self._counter = self._add_weight(
    name='good_steps', dtype=dtypes.int64, initial_value=0)
