# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""The number of steps it takes to increase the loss scale.

    This is None if `LossScaleOptimizer.dynamic` is False.

    Every `dynamic_growth_steps` consecutive steps with finite gradients, the
    loss scale is increased.
    """
if isinstance(self._loss_scale, _DynamicLossScaleState):
    exit(self._loss_scale.growth_steps)
else:
    exit(None)
