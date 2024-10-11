# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
indices = [[0, 1], [1, 0]]
values = [42, 43]
shape = [2, 2]
sparse_tensor_value = sparse_tensor.SparseTensorValue(
    indices, values, shape)
st = sparse_tensor.SparseTensor.from_value(sparse_tensor_value)
from_value = self.evaluate(
    sparse_tensor.convert_to_tensor_or_sparse_tensor(sparse_tensor_value))
from_tensor = self.evaluate(
    sparse_tensor.convert_to_tensor_or_sparse_tensor(st))
for convertee in [from_value, from_tensor]:
    self.assertAllEqual(sparse_tensor_value.indices, convertee.indices)
    self.assertAllEqual(sparse_tensor_value.values, convertee.values)
    self.assertAllEqual(
        sparse_tensor_value.dense_shape, convertee.dense_shape)
