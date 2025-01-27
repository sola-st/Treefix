# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
actual = a._merge_with(b)
actual_rev = b._merge_with(a)

self.assertDynamicRaggedShapeSpecEqual(actual, expected)
self.assertDynamicRaggedShapeSpecEqual(actual_rev, expected)
