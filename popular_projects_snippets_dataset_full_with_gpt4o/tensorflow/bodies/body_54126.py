# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
indices = [[0, 2]]
values = [1]
dense_shape = [-1, 5]
sp = sparse_tensor.SparseTensor(indices, values, dense_shape)
self.assertEqual(sp.shape.as_list(), [None, 5])
