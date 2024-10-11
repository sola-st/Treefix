# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
indices = [[1, 2], [2, 0], [3, 4]]
values = [b"a", b"b", b"c"]
shape = [4, 5]
sp_value = sparse_tensor.SparseTensorValue(indices, values, shape)
for sp in [
    sparse_tensor.SparseTensor(indices, values, shape),
    sparse_tensor.SparseTensor.from_value(sp_value),
    sparse_tensor.SparseTensor.from_value(
        sparse_tensor.SparseTensor(indices, values, shape))]:
    self.assertEqual(sp.indices.dtype, dtypes.int64)
    self.assertEqual(sp.values.dtype, dtypes.string)
    self.assertEqual(sp.dense_shape.dtype, dtypes.int64)
    self.assertEqual(sp.get_shape(), (4, 5))

    value = self.evaluate(sp)
    self.assertAllEqual(indices, value.indices)
    self.assertAllEqual(values, value.values)
    self.assertAllEqual(shape, value.dense_shape)
    sp_value = self.evaluate(sp)
    self.assertAllEqual(sp_value.indices, value.indices)
    self.assertAllEqual(sp_value.values, value.values)
    self.assertAllEqual(sp_value.dense_shape, value.dense_shape)
