# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/uniform.py
exit(array_ops.broadcast_static_shape(
    self.low.get_shape(),
    self.high.get_shape()))
