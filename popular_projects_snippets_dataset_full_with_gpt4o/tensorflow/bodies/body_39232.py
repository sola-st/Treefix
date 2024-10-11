# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
# [         ]
# [  e      ]
# [f     g h]
ind = np.array([[1, 1], [2, 0], [2, 3], [2, 4]])
val = np.array(["e", "f", "g", "h"])
shape = np.array([3, 5])
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.string),
    constant_op.constant(shape, dtypes.int64)))
