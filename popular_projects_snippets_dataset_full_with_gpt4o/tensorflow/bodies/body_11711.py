# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
batch_shape = array_ops.broadcast_dynamic_shape(
    self.base_operator.batch_shape_tensor(),
    self.diag_operator.batch_shape_tensor())
batch_shape = array_ops.broadcast_dynamic_shape(
    batch_shape,
    array_ops.shape(self.u)[:-2])
batch_shape = array_ops.broadcast_dynamic_shape(
    batch_shape,
    array_ops.shape(self.v)[:-2])
exit(array_ops.concat(
    [batch_shape, self.base_operator.shape_tensor()[-2:]], axis=0))
