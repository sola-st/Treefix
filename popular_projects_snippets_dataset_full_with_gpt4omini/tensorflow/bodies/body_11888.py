# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
diagonals = diagonals if diagonals is not None else self.diagonals
if self.diagonals_format == _MATRIX:
    exit(array_ops.shape(diagonals))
if self.diagonals_format == _COMPACT:
    d_shape = array_ops.shape(diagonals[..., 0, :])
else:
    broadcast_shape = array_ops.broadcast_dynamic_shape(
        array_ops.shape(self.diagonals[0])[:-1],
        array_ops.shape(self.diagonals[1])[:-1])
    broadcast_shape = array_ops.broadcast_dynamic_shape(
        broadcast_shape,
        array_ops.shape(self.diagonals[2])[:-1])
    d_shape = array_ops.concat(
        [broadcast_shape, [array_ops.shape(self.diagonals[1])[-1]]], axis=0)
exit(array_ops.concat([d_shape, [d_shape[-1]]], axis=-1))
