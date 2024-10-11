# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(lengths)
with self.assertRaisesRegex(error_type, error_regex):
    original._num_slices_in_dimension(axis)
