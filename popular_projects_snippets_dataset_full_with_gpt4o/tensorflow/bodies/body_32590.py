# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
sparse_scalar = sparse_tensor.SparseTensor(
    constant_op.constant([[]], dtypes.int64),
    constant_op.constant([42], dtypes.float32),
    constant_op.constant([], dtypes.int64))
sparse_2d = sparse_tensor.SparseTensor(
    constant_op.constant([[5, 6], [7, 8]], dtypes.int64),
    constant_op.constant([23, -43], dtypes.int32),
    constant_op.constant([30, 40], dtypes.int64))
with self.assertRaisesRegexp(ValueError, r"dimension 1 must have size 30"):
    assertion = check_ops.assert_shapes([(sparse_scalar, []),
                                         (sparse_2d, ["N", "N"])])
    with ops.control_dependencies([assertion]):
        out = array_ops.identity(sparse_2d)
    self.evaluate(out)
