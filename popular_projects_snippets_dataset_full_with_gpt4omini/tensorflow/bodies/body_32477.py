# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
doug = constant_op.constant([1, 2], name="doug")
with self.assertRaisesOpError(  # pylint:disable=g-error-prone-assert-raises
    "fail"):
    with ops.control_dependencies(
        [check_ops.assert_negative(
            doug, message="fail")]):
        out = array_ops.identity(doug)
    self.evaluate(out)
