# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x = constant_op.constant(10., name="x")
y = constant_op.constant(10.2, name="y")
with self.assertRaisesOpError(  # pylint:disable=g-error-prone-assert-raises
    "x and y not equal to tolerance"):
    with ops.control_dependencies(
        [check_ops.assert_near(x, y, atol=0.1,
                               message="failure message")]):
        out = array_ops.identity(x)
        self.evaluate(out)
