# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/normal.py
exit(array_ops.broadcast_static_shape(
    self.loc.get_shape(),
    self.scale.get_shape()))
