# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
exit(array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.concentration),
    array_ops.shape(self.rate)))
