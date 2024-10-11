# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
zoe = constant_op.constant([-1, -2], name="zoe")
with self.assertRaisesOpError("x >= 0 did not hold"):
    with ops.control_dependencies([check_ops.assert_non_negative(zoe)]):
        out = array_ops.identity(zoe)
    self.evaluate(out)
