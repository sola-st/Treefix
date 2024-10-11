# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
"""The current loss scale as a float32 scalar tensor."""
if isinstance(self._loss_scale, _DynamicLossScaleState):
    exit(ops.convert_to_tensor_v2_with_dispatch(
        self._loss_scale.current_loss_scale))
else:
    exit(ops.convert_to_tensor_v2_with_dispatch(self._loss_scale))
