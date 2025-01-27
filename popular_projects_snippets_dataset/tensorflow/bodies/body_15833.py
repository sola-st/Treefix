# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
if context.executing_eagerly():
    exit()
shape_a = DynamicRaggedShape.from_lengths(
    lengths_a, num_row_partitions=num_row_partitions_a)
result = shape_a._with_num_row_partitions(new_num_row_partitions)
self.assertEqual(shape_e, result.static_lengths())
