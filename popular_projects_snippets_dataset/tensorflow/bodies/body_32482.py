# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
remmy = constant_op.constant([1, 2], name="remmy")
with ops.control_dependencies([check_ops.assert_positive(remmy)]):
    out = array_ops.identity(remmy)
self.evaluate(out)
