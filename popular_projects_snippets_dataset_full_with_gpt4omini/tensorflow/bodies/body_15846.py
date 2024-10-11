# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
a = dynamic_ragged_shape.DynamicRaggedShape._from_inner_shape([1, 2, 3])
self.assertIsInstance(a[0], ops.Tensor)
