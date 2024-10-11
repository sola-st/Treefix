# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
ind = np.empty(shape=(0, len(dense_shape)))
val = np.array([])
shape = np.array(dense_shape)
exit(sparse_tensor.SparseTensor(
    constant_op.constant(ind, dtypes.int64),
    constant_op.constant(val, dtypes.float32),
    constant_op.constant(shape, dtypes.int64)))
