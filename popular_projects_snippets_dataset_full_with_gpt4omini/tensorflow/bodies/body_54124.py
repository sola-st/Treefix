# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor_test.py
indices = [[0, 2]]
values = [1]
y = ops.convert_to_tensor(3, dtype=dtypes.int64)
dense_shape = [x, y]
sp = sparse_tensor.SparseTensor(indices, values, dense_shape)
self.assertEqual(sp.shape.as_list(), [None, 3])
exit(sp)
