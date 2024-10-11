# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
claire = constant_op.constant([0], name="claire")
with self.assertRaisesOpError(  # pylint:disable=g-error-prone-assert-raises
    "x < 0 did not hold"):
    with ops.control_dependencies([check_ops.assert_negative(claire)]):
        out = array_ops.identity(claire)
    self.evaluate(out)
