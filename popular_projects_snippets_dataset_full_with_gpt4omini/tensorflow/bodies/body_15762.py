# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(lengths)
actual = original._num_slices_in_dimension(axis)
self.assertAllEqual(expected, actual)
