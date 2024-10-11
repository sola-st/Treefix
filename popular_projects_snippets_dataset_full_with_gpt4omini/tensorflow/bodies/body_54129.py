# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
indices = [[0, 0]]
values = [1]
sp = sparse_tensor.SparseTensor(indices, values, dense_shape)
self.assertEqual(sp.shape.rank, None)
exit(sp)
