# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
if isinstance(self._loss_scale, _DynamicLossScaleState):
    exit(self._loss_scale.update(grads))
else:
    exit((control_flow_ops.no_op(), True))
