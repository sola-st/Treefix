# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths(lengths)
actual = original._alt_inner_shape(new_dense_rank)
self.assertAllEqual(actual, expected_inner_shape)
