# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
# [           1]
# [-1.9        ]
# [   3    -4.2]
ind = np.array([[0, 1], [1, 0], [2, 0], [2, 1]])
val = np.array([1, -1.9, 3, -4.2])
shape = np.array([3, 3])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.float32),
    constant_op.constant(shape, dtypes.int64)))
