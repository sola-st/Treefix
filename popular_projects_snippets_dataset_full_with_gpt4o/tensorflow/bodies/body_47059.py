# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
loss_val = loss()
exit(loss_val * math_ops.cast(self.loss_scale, loss_val.dtype))
