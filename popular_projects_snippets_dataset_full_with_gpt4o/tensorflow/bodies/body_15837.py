# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Note that this test loses the later static values.
if context.executing_eagerly():
    exit()
shape = DynamicRaggedShape.from_lengths(
    lengths, num_row_partitions=num_row_partitions)
shape_b = shape._with_num_row_partitions(shape.rank - 1)
self.assertEqual(shape_e, shape_b.static_lengths())
