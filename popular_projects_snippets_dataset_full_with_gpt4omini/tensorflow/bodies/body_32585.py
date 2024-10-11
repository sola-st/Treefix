# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
sparse_int = sparse_tensor.SparseTensor(
    constant_op.constant([[5, 6, 7], [8, 9, 10]], dtypes.int64),
    constant_op.constant([23, -43], dtypes.int32),
    constant_op.constant([30, 30, 40], dtypes.int64))
assertion = check_ops.assert_shapes([(sparse_int, ["N", "N", "D"])])
with ops.control_dependencies([assertion]):
    out = array_ops.identity(sparse_int)
self.evaluate(out)
