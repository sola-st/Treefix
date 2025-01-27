# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
loss_val = loss()
exit(loss_val * math_ops.cast(loss_scale, loss_val.dtype))
