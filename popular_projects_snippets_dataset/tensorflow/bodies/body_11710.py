# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
batch_shape = array_ops.broadcast_static_shape(
    self.base_operator.batch_shape,
    self.diag_operator.batch_shape)
batch_shape = array_ops.broadcast_static_shape(
    batch_shape,
    self.u.shape[:-2])
batch_shape = array_ops.broadcast_static_shape(
    batch_shape,
    self.v.shape[:-2])
exit(batch_shape.concatenate(self.base_operator.shape[-2:]))
