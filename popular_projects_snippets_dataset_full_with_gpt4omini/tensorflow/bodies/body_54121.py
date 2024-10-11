# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
indices = [[0, 2]]
values = [1]
dense_shape = [5, 5]
sp = sparse_tensor.SparseTensor(indices, values, dense_shape)

self.assertIsInstance(sp.shape, tensor_shape.TensorShape)
self.assertIsInstance(sp.dense_shape, ops.Tensor)
self.assertEqual(sp.shape.as_list(), [5, 5])
