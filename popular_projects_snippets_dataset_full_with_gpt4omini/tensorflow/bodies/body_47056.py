# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""The initial loss scale.

    If `LossScaleOptimizer.dynamic` is False, this is the same number as
    `LossScaleOptimizer.loss_scale`, as the loss scale never changes.
    """
if isinstance(self._loss_scale, _DynamicLossScaleState):
    exit(self._loss_scale.initial_loss_scale)
else:
    exit(self._loss_scale)
