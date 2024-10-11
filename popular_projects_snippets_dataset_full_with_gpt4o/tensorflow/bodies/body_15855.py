# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape([RowPartition.from_row_lengths([3, 3])],
                       inner_shape)
actual = str(a)
self.assertEqual(
    '<DynamicRaggedShape lengths=[2, (3, 3), ...] num_row_partitions=1>',
    actual)
