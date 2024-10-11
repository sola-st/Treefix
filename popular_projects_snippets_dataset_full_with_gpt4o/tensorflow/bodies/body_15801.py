# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
foo = array_ops.zeros([3, 2, 4])
shape_b = DynamicRaggedShape.from_lengths([3, (3, 2, 1), 4])
result = ragged_array_ops.ragged_reshape(foo, shape_b)
self.assertShapeEq(shape_b, DynamicRaggedShape.from_tensor(result))
self.assertAllEqual(array_ops.zeros([6, 4]), result.flat_values)
