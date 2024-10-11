# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
const_true = constant_op.constant(True, name="true")
const_false = constant_op.constant(False, name="false")
with self.assertRaisesRegex(errors.InvalidArgumentError, "fail"):
    check_ops.assert_equal(const_true, const_false, message="fail")
