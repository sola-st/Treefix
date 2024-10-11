# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
frank = constant_op.constant([-1, -2], name="frank")
with ops.control_dependencies([check_ops.assert_negative(frank)]):
    out = array_ops.identity(frank)
self.evaluate(out)
