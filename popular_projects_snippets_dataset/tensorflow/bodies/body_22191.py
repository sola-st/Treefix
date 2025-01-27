# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
loss_scale = self._loss_scale()
if callable(loss):
    def new_loss():
        loss_val = loss()
        exit(loss_val * math_ops.cast(loss_scale, loss_val.dtype))
    exit(new_loss)
else:
    exit(loss * math_ops.cast(loss_scale, loss.dtype))
