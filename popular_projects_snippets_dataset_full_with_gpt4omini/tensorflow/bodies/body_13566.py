# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/uniform.py
exit(array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.low),
    array_ops.shape(self.high)))
