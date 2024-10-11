# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
exit(array_ops.broadcast_static_shape(
    self.concentration.get_shape(),
    self.rate.get_shape()))
