# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# [    a]
# [b    ]
# [c   d]
ind = np.array([[0, 2], [1, 0], [2, 0], [2, 2]])
val = np.array(["a", "b", "c", "d"])
shape = np.array([3, 3])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.string),
    constant_op.constant(shape, dtypes.int64)))
