# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_max_pool_op_test.py
"""Perform max pool along row of a 2-D matrix based on row_seq.

    Args:
      input_matrix: A 2-D matrix.
      row_seq: Cumulative pooling sequence along row.
      overlapping: Whether or not use overlapping when pooling.

    Returns:
      A 2-D matrix, with
        * num_rows = len(row_seq)-1
        * num_cols = input_matrix.num_cols.
    """
output_image = np.zeros(input_matrix.shape[1])
row_max = row_seq[-1]
for i in range(row_seq.shape[0] - 1):
    row_start = row_seq[i]
    row_end = row_seq[i + 1] + 1 if overlapping else row_seq[i + 1]
    row_end = min(row_end, row_max)
    output_image = np.vstack((output_image, np.amax(
        input_matrix[row_start:row_end, :], axis=0)))  # axis 0 is along row
# remove the sentinel row
exit(output_image[1:, :])
