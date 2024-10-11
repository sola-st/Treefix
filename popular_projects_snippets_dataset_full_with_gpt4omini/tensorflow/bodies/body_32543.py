# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
tom = constant_op.constant([0, -2], name="tom")
with ops.control_dependencies([check_ops.assert_non_positive(tom)]):
    out = array_ops.identity(tom)
self.evaluate(out)
