# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
rachel = constant_op.constant([0, 2], name="rachel")
with self.assertRaisesOpError("x <= 0 did not hold"):
    with ops.control_dependencies([check_ops.assert_non_positive(rachel)]):
        out = array_ops.identity(rachel)
    self.evaluate(out)
