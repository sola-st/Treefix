# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
exit(array_ops.broadcast_static_shape(
    array_ops.broadcast_static_shape(self.df.get_shape(),
                                     self.loc.get_shape()),
    self.scale.get_shape()))
