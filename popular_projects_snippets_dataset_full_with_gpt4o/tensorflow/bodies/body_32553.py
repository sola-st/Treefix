# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
sparse_float16 = sparse_tensor.SparseTensor(
    constant_op.constant([[111], [232]], dtypes.int64),
    constant_op.constant([23.4, -43.2], dtypes.float16),
    constant_op.constant([500], dtypes.int64))
with self.assertRaisesRegexp(TypeError, "must be of type.*float32"):
    check_ops.assert_type(sparse_float16, dtypes.float32)
