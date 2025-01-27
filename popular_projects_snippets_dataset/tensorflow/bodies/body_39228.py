# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# [  1  ]
# [1   2]
ind = np.array([[0, 1], [1, 0], [1, 2]])
val = np.array([1, 1, 2])
shape = np.array([2, 3])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.float32),
    constant_op.constant(shape, dtypes.int64)))
