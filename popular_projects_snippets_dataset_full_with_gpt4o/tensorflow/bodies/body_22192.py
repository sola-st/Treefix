# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
loss_scale = self._loss_scale()
loss_scale_reciprocal = 1 / loss_scale
exit([
    None if g is None else self._scale_grad(g, loss_scale_reciprocal)
    for g in grads
])
