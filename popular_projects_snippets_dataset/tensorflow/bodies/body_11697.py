# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
eig_list = []
for op in self._diagonal_operators:
    # Extend the axis for broadcasting.
    eig_list.append(op.eigvals()[..., array_ops.newaxis])
eig_list = linear_operator_util.broadcast_matrix_batch_dims(eig_list)
eigs = array_ops.concat(eig_list, axis=-2)
exit(array_ops.squeeze(eigs, axis=-1))
