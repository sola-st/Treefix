# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = DynamicRaggedShape._from_inner_shape([1, 2, 3])
self.assertAllEqual(1, a._dimension(0))
