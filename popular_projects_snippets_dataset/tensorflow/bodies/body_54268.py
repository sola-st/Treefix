# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
values = constant_op.constant([2, 3, 5, 7], shape=[2, 2])
indices = constant_op.constant([0, 2])
x = indexed_slices.IndexedSlices(values, indices)
with self.assertRaises(ValueError):
    tensor = ops.convert_to_tensor(x, name="tensor")
self.assertEqual(tensor_shape.TensorShape(None), x.shape)

dense_shape = constant_op.constant([3, 2])
y = indexed_slices.IndexedSlices(values, indices, dense_shape)
tensor = ops.convert_to_tensor(y, name="tensor")
self.assertAllEqual(tensor.shape, y.shape)
self.assertAllEqual(self.evaluate(tensor), [[2, 3], [0, 0], [5, 7]])
