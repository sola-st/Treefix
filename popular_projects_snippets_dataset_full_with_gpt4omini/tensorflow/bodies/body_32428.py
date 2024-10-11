# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
small = constant_op.constant([3, 1], name="small")
with self.assertRaisesOpError("x != y did not hold"):
    with ops.control_dependencies(
        [check_ops.assert_none_equal(small, small)]):
        out = array_ops.identity(small)
    self.evaluate(out)
