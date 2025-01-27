# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
sparse_float = sparse_tensor.SparseTensor(
    constant_op.constant([[111], [232]], dtypes.int64),
    constant_op.constant([23.4, -43.2], dtypes.float32),
    constant_op.constant([500], dtypes.int64))

with ops.control_dependencies(
    [check_ops.assert_type(sparse_float, dtypes.float32)]):
    out = sparse_tensor.SparseTensor(sparse_float.indices,
                                     array_ops.identity(sparse_float.values),
                                     sparse_float.dense_shape)
self.evaluate(out)
