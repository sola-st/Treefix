# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
freddie = constant_op.constant([-1, -2], name="freddie")
with self.assertRaisesOpError("fail"):
    with ops.control_dependencies(
        [check_ops.assert_positive(
            freddie, message="fail")]):
        out = array_ops.identity(freddie)
    self.evaluate(out)
