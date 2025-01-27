# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape = DynamicRaggedShape.from_lengths(lengths)
original_row_partitions = shape.num_row_partitions
shape_a = shape._with_num_row_partitions(num_row_partitions_a)
self.assertEqual(shape_a.num_row_partitions, num_row_partitions_a)
shape_b = shape_a._with_num_row_partitions(num_row_partitions_b)
self.assertEqual(shape_b.num_row_partitions, num_row_partitions_b)
actual = shape_b._with_num_row_partitions(original_row_partitions)
self.assertShapeEq(actual, shape)
