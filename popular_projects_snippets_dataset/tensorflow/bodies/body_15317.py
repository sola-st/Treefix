# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Allow ragged and uniform shapes to be specified.

  For example, [2, [2,1], 2] represents a shape like:
  [[[0, 0], [0, 0]], [[0, 0]]]

  Args:
    lengths: a list of integers and lists of integers.
    dtype: dtype of the shape (tf.int32 or tf.int64)

  Returns:
    a sequence of RowPartitions, and the number of values of the last partition.
  """
size_so_far = lengths[0]
result = []
for current_lengths in lengths[1:]:
    if isinstance(current_lengths, int):
        nrows = size_so_far
        nvals = current_lengths * nrows
        size_so_far = nvals
        result.append(
            RowPartition.from_uniform_row_length(
                current_lengths, nvals, nrows=nrows, dtype_hint=dtype))
    else:
        if size_so_far != len(current_lengths):
            raise ValueError("Shape not consistent.")
        result.append(
            RowPartition.from_row_lengths(current_lengths, dtype_hint=dtype))
        size_so_far = sum(current_lengths)
exit((result, size_so_far))
