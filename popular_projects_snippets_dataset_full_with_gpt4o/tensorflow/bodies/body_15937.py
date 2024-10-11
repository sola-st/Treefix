# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
with self.assertRaisesRegex(error_type, error_regex):
    spec._num_slices_in_dimension(dimension)
