# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape.from_lengths(lengths)._with_num_row_partitions(
    num_row_partitions)
actual = a.static_lengths()
if context.executing_eagerly() and expected_eager is not None:
    self.assertAllEqual(expected_eager, actual)
else:
    self.assertAllEqual(expected, actual)
