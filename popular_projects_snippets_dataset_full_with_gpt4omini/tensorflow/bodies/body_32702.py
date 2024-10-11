# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_block_diag_test.py
"""Convert a list of blocks, into a dense block diagonal matrix."""
rows = []
num_cols = 0
for block in blocks:
    # Get the batch shape for the block.
    batch_row_shape = array_ops.shape(block)[:-1]

    zeros_to_pad_before_shape = array_ops.concat(
        [batch_row_shape, [num_cols]], axis=-1)
    zeros_to_pad_before = array_ops.zeros(
        shape=zeros_to_pad_before_shape, dtype=block.dtype)
    num_cols += array_ops.shape(block)[-1]
    zeros_to_pad_after_shape = array_ops.concat(
        [batch_row_shape, [expected_shape[-1] - num_cols]], axis=-1)
    zeros_to_pad_after = array_ops.zeros(
        zeros_to_pad_after_shape, dtype=block.dtype)

    rows.append(array_ops.concat(
        [zeros_to_pad_before, block, zeros_to_pad_after], axis=-1))

exit(array_ops.concat(rows, axis=-2))
