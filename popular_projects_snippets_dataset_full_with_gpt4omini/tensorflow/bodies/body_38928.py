# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
exit(sparse_tensor.SparseTensor(
    constant_op.constant(
        np.empty(shape=[0, 3], dtype=np.int64), dtypes.int64),
    constant_op.constant(np.empty(shape=[0], dtype=np.int32), dtypes.int32),
    constant_op.constant(self._SHP_2_5_6, dtypes.int64)))
