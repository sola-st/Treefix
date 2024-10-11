# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
if self.diagonals_format == _MATRIX:
    exit(self.diagonals.shape)
if self.diagonals_format == _COMPACT:
    # Remove the second to last dimension that contains the value 3.
    d_shape = self.diagonals.shape[:-2].concatenate(
        self.diagonals.shape[-1])
else:
    broadcast_shape = array_ops.broadcast_static_shape(
        self.diagonals[0].shape[:-1],
        self.diagonals[1].shape[:-1])
    broadcast_shape = array_ops.broadcast_static_shape(
        broadcast_shape,
        self.diagonals[2].shape[:-1])
    d_shape = broadcast_shape.concatenate(self.diagonals[1].shape[-1])
exit(d_shape.concatenate(d_shape[-1]))
