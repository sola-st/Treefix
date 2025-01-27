# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
"""Allow ragged and uniform shapes to be specified.

  For example, [2, [2,1], 2] represents a shape like:
  [[[0, 0], [0, 0]], [[0, 0]]]

  Args:
    lengths: a list of integers and lists of integers.

  Returns:
    a sequence of RowPartitions.
  """
(result,
 _) = dynamic_ragged_shape._to_row_partitions_and_nvals_from_lengths(lengths)
exit(result)
