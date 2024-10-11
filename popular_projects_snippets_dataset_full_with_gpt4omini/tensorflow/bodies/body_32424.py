# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
cond = constant_op.constant([True, False], name="small")
with self.assertRaisesRegex(errors.InvalidArgumentError, "fail"):
    check_ops.assert_equal(cond, False, message="fail")
