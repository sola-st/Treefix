# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
shape_x = DynamicRaggedShape.from_lengths([3, (1, 3, 2), 4])
foo = ragged_array_ops.ones(shape_x)
self.assertShapeEq(shape_x, DynamicRaggedShape.from_tensor(foo))
self.assertAllEqual(array_ops.ones([6, 4]), foo.flat_values)
