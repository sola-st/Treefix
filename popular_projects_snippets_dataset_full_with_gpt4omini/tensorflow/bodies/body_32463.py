# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([1, 2], name="small")
big = constant_op.constant([3, 4], name="big")
with self.assertRaisesOpError(  # pylint:disable=g-error-prone-assert-raises
    "x > y did not hold"):
    with ops.control_dependencies([check_ops.assert_greater(small, big)]):
        out = array_ops.identity(big)
    self.evaluate(out)
