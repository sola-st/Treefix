# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
ind = np.array([[0, 0], [1, 0], [1, 3], [1, 4]])
val = np.array([0, 10, 13, 14])
shape = np.array([2, 6])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.int32),
    constant_op.constant(shape, dtypes.int64)))
