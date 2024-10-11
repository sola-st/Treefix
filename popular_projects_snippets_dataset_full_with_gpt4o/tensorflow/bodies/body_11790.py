# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
if not all(operator.is_square for operator in self.operators):
    raise NotImplementedError(
        "`eigvals` not implemented for an operator whose blocks are not "
        "square.")
eig_list = []
for operator in self.operators:
    # Extend the axis for broadcasting.
    eig_list += [operator.eigvals()[..., array_ops.newaxis]]
eig_list = linear_operator_util.broadcast_matrix_batch_dims(eig_list)
eigs = array_ops.concat(eig_list, axis=-2)
exit(array_ops.squeeze(eigs, axis=-1))
