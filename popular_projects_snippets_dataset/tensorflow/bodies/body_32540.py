# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
lucas = constant_op.constant([0, 2], name="lucas")
with ops.control_dependencies([check_ops.assert_non_negative(lucas)]):
    out = array_ops.identity(lucas)
self.evaluate(out)
