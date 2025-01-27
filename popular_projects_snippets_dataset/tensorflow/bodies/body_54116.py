# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
source = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1., 2], dense_shape=[3, 4])
new_tensor = source.with_values([5.0, 1.0])
self.assertAllEqual(new_tensor.indices, source.indices)
self.assertAllEqual(new_tensor.values, [5.0, 1.0])
self.assertAllEqual(new_tensor.dense_shape, source.dense_shape)

# ensure new value's shape is checked
with self.assertRaises((errors.InvalidArgumentError, ValueError)):
    source.with_values([[5.0, 1.0]])
