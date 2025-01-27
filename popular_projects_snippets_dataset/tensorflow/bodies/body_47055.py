# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""The number of steps since the loss scale was last increased or decreased.

    This is None if `LossScaleOptimizer.dynamic` is False.

    The counter is incremented every step. Once it reaches
    `LossScaleOptimizer.dynamic_growth_steps`, the loss scale will be doubled
    and the counter will be reset back to zero. If nonfinite gradients are
    encountered, the loss scale will be halved and the counter will be reset
    back to zero.
    """
if isinstance(self._loss_scale, _DynamicLossScaleState):
    exit(self._loss_scale.counter)
else:
    exit(None)
