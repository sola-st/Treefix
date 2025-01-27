# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
self.assertEqual(
    RowPartitionSpec.from_value(RowPartition.from_row_splits([0, 2, 8, 8])),
    RowPartitionSpec(nrows=3))
self.assertEqual(
    RowPartitionSpec.from_value(
        RowPartition.from_row_lengths([5, 3, 0, 2])),
    RowPartitionSpec(nrows=4))
self.assertEqual(
    RowPartitionSpec.from_value(
        RowPartition.from_value_rowids([0, 2, 2, 8])),
    RowPartitionSpec(nrows=9, nvals=4))
self.assertEqual(
    RowPartitionSpec.from_value(
        RowPartition.from_uniform_row_length(
            nvals=12, uniform_row_length=3)),
    RowPartitionSpec(nvals=12, uniform_row_length=3))
