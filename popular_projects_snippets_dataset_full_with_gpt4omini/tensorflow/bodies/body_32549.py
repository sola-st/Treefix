# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
integers = constant_op.constant([1, 2], dtype=dtypes.int64)
with ops.control_dependencies([
    check_ops.assert_type(integers, dtypes.int64)]):
    out = array_ops.identity(integers)
self.evaluate(out)
