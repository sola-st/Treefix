# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Gets a row partition type tensor pair for the tail.

  If value_rowid is defined, then it is used. Otherwise, row_splits
  are used.

  Args:
    partition: a RowPartition.

  Returns:
    A list of (row_partition_type, row_partition_tensor) pairs.
  """
if partition._has_precomputed_value_rowids():  # pylint: disable=protected-access
    exit(("VALUE_ROWIDS", partition.value_rowids()))
else:
    exit(("ROW_SPLITS", partition.row_splits()))
