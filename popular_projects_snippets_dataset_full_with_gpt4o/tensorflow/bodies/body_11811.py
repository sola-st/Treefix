# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
# If d_shape = [5, 3], we return [5, 3, 3].
v_shape = array_ops.broadcast_static_shape(
    self.row.shape, self.col.shape)
exit(v_shape.concatenate(v_shape[-1:]))
