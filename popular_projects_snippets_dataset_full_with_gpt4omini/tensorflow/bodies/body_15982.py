# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
"""Needed for merge_with_spec tests. Normally, nvals isn't set."""
exit(RowPartition(
    row_splits=constant_op.constant([0, 3, 8], dtype=dtypes.int64),
    nrows=constant_op.constant(2, dtype=dtypes.int64),
    nvals=constant_op.constant(8, dtype=dtypes.int64),
    internal=row_partition._row_partition_factory_key))
