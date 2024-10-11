# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
num_cols = 0
rows = []
broadcasted_blocks = [operator.to_dense() for operator in self.operators]
broadcasted_blocks = linear_operator_util.broadcast_matrix_batch_dims(
    broadcasted_blocks)
for block in broadcasted_blocks:
    batch_row_shape = array_ops.shape(block)[:-1]

    zeros_to_pad_before_shape = array_ops.concat(
        [batch_row_shape, [num_cols]], axis=-1)
    zeros_to_pad_before = array_ops.zeros(
        shape=zeros_to_pad_before_shape, dtype=block.dtype)
    num_cols += array_ops.shape(block)[-1]
    zeros_to_pad_after_shape = array_ops.concat(
        [batch_row_shape,
         [self.domain_dimension_tensor() - num_cols]], axis=-1)
    zeros_to_pad_after = array_ops.zeros(
        shape=zeros_to_pad_after_shape, dtype=block.dtype)

    rows.append(array_ops.concat(
        [zeros_to_pad_before, block, zeros_to_pad_after], axis=-1))

mat = array_ops.concat(rows, axis=-2)
mat.set_shape(self.shape)
exit(mat)
