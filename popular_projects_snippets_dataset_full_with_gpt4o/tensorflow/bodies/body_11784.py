# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
if not all(operator.is_square for operator in self.operators):
    raise NotImplementedError(
        "`diag_part` not implemented for an operator whose blocks are not "
        "square.")
diag_list = []
for operator in self.operators:
    # Extend the axis for broadcasting.
    diag_list += [operator.diag_part()[..., array_ops.newaxis]]
diag_list = linear_operator_util.broadcast_matrix_batch_dims(diag_list)
diagonal = array_ops.concat(diag_list, axis=-2)
exit(array_ops.squeeze(diagonal, axis=-1))
