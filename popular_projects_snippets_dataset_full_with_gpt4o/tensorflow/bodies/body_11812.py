# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_toeplitz.py
row = self.row if row is None else row
col = self.col if col is None else col
v_shape = array_ops.broadcast_dynamic_shape(
    array_ops.shape(row),
    array_ops.shape(col))
k = v_shape[-1]
exit(array_ops.concat((v_shape, [k]), 0))
