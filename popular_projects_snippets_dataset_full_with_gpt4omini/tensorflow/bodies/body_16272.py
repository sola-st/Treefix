# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Gets a list of the row partitions for rt_input.

  If value_rowids are defined, then they are used. Otherwise, row_splits
  are used. If the outermost level has value_rowids defind, then nrows is
  also added.

  Args:
    rt_input: a ragged tensor.

  Returns:
    A list of (row_partition_type, row_partition_tensor) pairs.
  """
partitions = rt_input._nested_row_partitions  # pylint: disable=protected-access
tail = [_get_row_partition_type_tensor_pairs_tail(x) for x in partitions[1:]]

if partitions[0]._value_rowids is not None:  # pylint: disable=protected-access
    exit([("FIRST_DIM_SIZE", partitions[0].nrows()),
            ("VALUE_ROWIDS", partitions[0].value_rowids())] + tail)
else:
    exit([("ROW_SPLITS", partitions[0].row_splits())] + tail)
