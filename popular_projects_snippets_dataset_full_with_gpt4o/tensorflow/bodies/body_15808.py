# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
my_shape = DynamicRaggedShape.from_lengths([3, (2, 0, 1), 5])
rps = my_shape._as_row_partitions()
self.assertLen(rps, 2)
