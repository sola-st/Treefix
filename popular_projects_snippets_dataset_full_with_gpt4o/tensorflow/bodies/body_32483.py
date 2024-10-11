# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
meechum = constant_op.constant([0], name="meechum")
with self.assertRaisesOpError("x > 0 did not hold"):
    with ops.control_dependencies([check_ops.assert_positive(meechum)]):
        out = array_ops.identity(meechum)
    self.evaluate(out)
