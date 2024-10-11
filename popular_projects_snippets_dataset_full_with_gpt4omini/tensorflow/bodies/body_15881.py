# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rts = DynamicRaggedShape.from_tensor(x)
actual = rts[:1]
self.assertShapeEq(rts, actual)
