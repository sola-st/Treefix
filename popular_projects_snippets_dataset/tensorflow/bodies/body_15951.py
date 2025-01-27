# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
encoder = dynamic_ragged_shape._DynamicRaggedShapeBatchEncoder()
actual = encoder.unbatch(spec)
self.assertDynamicRaggedShapeSpecEqual(actual, expected)
