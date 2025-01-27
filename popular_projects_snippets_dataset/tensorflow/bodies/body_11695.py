# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
num_cols = 0
dense_rows = []
flat_broadcast_operators = linear_operator_util.broadcast_matrix_batch_dims(
    [op.to_dense() for row in self.operators for op in row])  # pylint: disable=g-complex-comprehension
broadcast_operators = [
    flat_broadcast_operators[i * (i + 1) // 2:(i + 1) * (i + 2) // 2]
    for i in range(len(self.operators))]
for row_blocks in broadcast_operators:
    batch_row_shape = array_ops.shape(row_blocks[0])[:-1]
    num_cols += array_ops.shape(row_blocks[-1])[-1]
    zeros_to_pad_after_shape = array_ops.concat(
        [batch_row_shape,
         [self.domain_dimension_tensor() - num_cols]], axis=-1)
    zeros_to_pad_after = array_ops.zeros(
        shape=zeros_to_pad_after_shape, dtype=self.dtype)

    row_blocks.append(zeros_to_pad_after)
    dense_rows.append(array_ops.concat(row_blocks, axis=-1))

mat = array_ops.concat(dense_rows, axis=-2)
mat.set_shape(self.shape)
exit(mat)
