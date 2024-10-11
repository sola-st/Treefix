# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_lower_triangular_test.py
"""Convert a list of blocks into a dense blockwise lower-triangular matrix."""
rows = []
num_cols = 0
for row_blocks in blocks:

    # Get the batch shape for the block.
    batch_row_shape = array_ops.shape(row_blocks[0])[:-1]

    num_cols += array_ops.shape(row_blocks[-1])[-1]
    zeros_to_pad_after_shape = array_ops.concat(
        [batch_row_shape, [expected_shape[-2] - num_cols]], axis=-1)
    zeros_to_pad_after = array_ops.zeros(
        zeros_to_pad_after_shape, dtype=row_blocks[-1].dtype)

    row_blocks.append(zeros_to_pad_after)
    rows.append(array_ops.concat(row_blocks, axis=-1))

exit(array_ops.concat(rows, axis=-2))
