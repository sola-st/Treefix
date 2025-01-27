# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = constant_op.constant(1., name="x")
y = constant_op.constant(1., name="y")
with ops.control_dependencies(
    [check_ops.assert_near(x, y, message="failure message")]):
    out = array_ops.identity(x)
    self.evaluate(out)
