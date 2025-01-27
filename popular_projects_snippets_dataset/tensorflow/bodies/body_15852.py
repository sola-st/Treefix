# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape.from_lengths([2, (1, 2), 3])
actual = str(a)
self.assertEqual(
    '<DynamicRaggedShape lengths=[2, (1, 2), 3] num_row_partitions=1>',
    actual)
