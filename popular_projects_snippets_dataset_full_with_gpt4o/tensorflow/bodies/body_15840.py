# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
original = DynamicRaggedShape.from_lengths([2, (3, 5), 6])
result = original._merge_with(original)
self.assertShapeEq(result, original)
