# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
# Includes two entries with the form [1, 1, x] : 150.
ind = np.array([[0, 0, 1], [0, 1, 0], [0, 1, 2], [1, 0, 3], [1, 1, 0],
                [1, 1, 1], [1, 1, 2], [1, 2, 2]])
val = np.array([1, 10, 12, 103, 150, 149, 150, 122])
shape = np.array([2, 3, 4])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtype),
    constant_op.constant(shape, dtypes.int64)))
