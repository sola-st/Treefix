# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]])
val = np.array(["a", "b", "c", "d", "e", "f"])
shape = np.array([5, 6])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.string),
    constant_op.constant(shape, dtypes.int64)))
