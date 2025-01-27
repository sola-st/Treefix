# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
val = np.array([0, 10, 13, 14, 32, 33])
shape = np.array([5, 6])
sp = sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.int64),
    constant_op.constant(shape, dtypes.int64))

self.assertEqual(sp.shape, tensor_shape.TensorShape([5, 6]))

sp.set_shape(tensor_shape.TensorShape(None))
sp.set_shape(tensor_shape.TensorShape([None, None]))
sp.set_shape(tensor_shape.TensorShape([5, None]))
sp.set_shape(tensor_shape.TensorShape([None, 6]))
sp.set_shape(tensor_shape.TensorShape([5, 6]))

with self.assertRaises(ValueError):
    sp.set_shape([None, None, None])

with self.assertRaises(ValueError):
    sp.set_shape([3, None])

with self.assertRaises(ValueError):
    sp.set_shape([None, 7])

with self.assertRaises(ValueError):
    sp.set_shape([3, 6])
