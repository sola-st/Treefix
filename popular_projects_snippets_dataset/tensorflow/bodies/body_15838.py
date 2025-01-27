# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
# Note that this test loses the later static values.
if context.executing_eagerly():
    exit()
shape = DynamicRaggedShape.from_lengths(
    [5, 2, 3], num_row_partitions=2)
shape_b = shape._with_num_row_partitions(0)
self.assertEqual([5, 2, 3], shape_b.static_lengths())
