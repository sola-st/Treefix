# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# [   ]
# [1  ]
# [2  ]
ind = np.array([[1, 0], [2, 0]])
val = np.array([1, 2])
shape = np.array([3, 2])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.float32),
    constant_op.constant(shape, dtypes.int64)))
