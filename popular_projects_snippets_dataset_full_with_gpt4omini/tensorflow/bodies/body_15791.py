# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Testing the test.
actual = _to_row_partitions_from_lengths([1, 2, 3])
expected = [
    RowPartition.from_row_splits([0, 2]),
    RowPartition.from_row_splits([0, 3, 6])
]
self.assertRowPartitionEq(actual[0], expected[0])
self.assertRowPartitionEq(actual[1], expected[1])
