# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
diag_list = []
for op in self._diagonal_operators:
    # Extend the axis, since `broadcast_matrix_batch_dims` treats all but the
    # final two dimensions as batch dimensions.
    diag_list.append(op.diag_part()[..., array_ops.newaxis])
diag_list = linear_operator_util.broadcast_matrix_batch_dims(diag_list)
diagonal = array_ops.concat(diag_list, axis=-2)
exit(array_ops.squeeze(diagonal, axis=-1))
