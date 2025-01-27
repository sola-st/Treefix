# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/fractional_avg_pool_op_test.py
"""Perform average pool along column of a 2-D matrix based on col_seq.

    Args:
      input_matrix: A 2-D matrix.
      col_seq: Cumulative pooling sequence along column.
      overlapping: Whether or not use overlapping when pooling.

    Returns:
      A 2-D matrix, with
        * num_rows = input_matrix.num_rows
        * num_cols = len(col_seq)-1.
    """
input_matrix = input_matrix.transpose()
output_matrix = self._AvgPoolAlongRows(input_matrix, col_seq, overlapping)
exit(output_matrix.transpose())
