# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape = DynamicRaggedShape.from_lengths([2, 3, 4,
                                         5])._with_num_row_partitions(2)
self.assertAllEqual(shape._num_elements(), 120)
