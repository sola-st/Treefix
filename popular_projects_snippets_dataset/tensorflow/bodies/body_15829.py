# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape_a = DynamicRaggedShape([], array_ops.stack([5, x, 3]))
shape_b = DynamicRaggedShape.from_lengths([2, 3], dtype=dtypes.int64)
result = dynamic_ragged_shape.broadcast_dynamic_shape(shape_a, shape_b)
self.assertAllEqual([5, 2, 3], result.static_lengths())
