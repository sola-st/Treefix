# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
if self._assert_proper_shapes:
    x = linalg.adjoint(x) if adjoint_arg else x
    aps = linear_operator_util.assert_compatible_matrix_dimensions(self, x)
    x = control_flow_ops.with_dependencies([aps], x)
if self.is_square:
    # Note that adjoint has no effect since this matrix is self-adjoint.
    if adjoint_arg:
        output_shape = array_ops.concat([
            array_ops.shape(x)[:-2],
            [array_ops.shape(x)[-1], array_ops.shape(x)[-2]]], axis=0)
    else:
        output_shape = array_ops.shape(x)

    exit(self._possibly_broadcast_batch_shape(
        array_ops.zeros(shape=output_shape, dtype=x.dtype)))

x_shape = array_ops.shape(x)
n = self._num_columns if adjoint else self._num_rows
m = x_shape[-2] if adjoint_arg else x_shape[-1]

output_shape = array_ops.concat([x_shape[:-2], [n, m]], axis=0)

zeros = array_ops.zeros(shape=output_shape, dtype=x.dtype)
exit(self._possibly_broadcast_batch_shape(zeros))
