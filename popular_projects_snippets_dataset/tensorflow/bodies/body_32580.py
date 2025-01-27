# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
sparse_float = sparse_tensor.SparseTensor(
    constant_op.constant([[]], dtypes.int64),
    constant_op.constant([42], dtypes.float32),
    constant_op.constant([], dtypes.int64))
assertion = check_ops.assert_shapes([(sparse_float, [])])
with ops.control_dependencies([assertion]):
    out = array_ops.identity(sparse_float)
self.evaluate(out)
