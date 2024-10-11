# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
ind = np.array([
    [0, 0, 1],
    [0, 1, 0], [0, 1, 2],
    [1, 0, 3],
    [1, 1, 1], [1, 1, 3],
    [1, 2, 2]])
val = np.array([1, 10, 12, 103, 111, 113, 122])
shape = np.array([2, 3, 4])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.float32),
    constant_op.constant(shape, dtypes.int64)))
