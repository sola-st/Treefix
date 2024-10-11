# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/student_t.py
exit(array_ops.broadcast_dynamic_shape(
    array_ops.shape(self.df),
    array_ops.broadcast_dynamic_shape(
        array_ops.shape(self.loc), array_ops.shape(self.scale))))
