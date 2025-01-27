# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
sparse_float = sparse_tensor.SparseTensor(
    constant_op.constant([[111], [232]], dtypes.int64),
    constant_op.constant([23.4, -43.2], dtypes.float32),
    constant_op.constant([500], dtypes.int64))
with self.assertRaisesRegexp(ValueError, r"dimension 0 must have size 499"):
    assertion = check_ops.assert_shapes([(sparse_float, [499])])
    with ops.control_dependencies([assertion]):
        out = array_ops.identity(sparse_float)
    self.evaluate(out)
