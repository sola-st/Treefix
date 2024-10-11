# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_tridiag.py
diagonals = self.diagonals
if adjoint:
    diagonals = self._construct_adjoint_diagonals(diagonals)

# TODO(b/144860784): Remove the broadcasting code below once
# tridiagonal_solve broadcasts.

rhs_shape = array_ops.shape(rhs)
k = self._shape_tensor(diagonals)[-1]
broadcast_shape = array_ops.broadcast_dynamic_shape(
    self._shape_tensor(diagonals)[:-2], rhs_shape[:-2])
rhs = array_ops.broadcast_to(
    rhs, array_ops.concat(
        [broadcast_shape, rhs_shape[-2:]], axis=-1))
if self.diagonals_format == _MATRIX:
    diagonals = array_ops.broadcast_to(
        diagonals, array_ops.concat(
            [broadcast_shape, [k, k]], axis=-1))
elif self.diagonals_format == _COMPACT:
    diagonals = array_ops.broadcast_to(
        diagonals, array_ops.concat(
            [broadcast_shape, [3, k]], axis=-1))
else:
    diagonals = [
        array_ops.broadcast_to(d, array_ops.concat(
            [broadcast_shape, [k]], axis=-1)) for d in diagonals]

y = linalg.tridiagonal_solve(
    diagonals, rhs,
    diagonals_format=self.diagonals_format,
    transpose_rhs=adjoint_arg,
    conjugate_rhs=adjoint_arg)
exit(y)
