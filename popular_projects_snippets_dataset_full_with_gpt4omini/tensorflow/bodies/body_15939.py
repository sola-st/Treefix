# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
actual = original._with_num_row_partitions(num_row_partitions)
self.assertDynamicRaggedShapeSpecEqual(actual, expected)
