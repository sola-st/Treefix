# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
actual = DynamicRaggedShape.Spec._from_spec(other_spec)
self.assertDynamicRaggedShapeSpecEqual(expected, actual)
