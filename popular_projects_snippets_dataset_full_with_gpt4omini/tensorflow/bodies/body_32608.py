# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
check_ops.assert_scalar(constant_op.constant(3))
check_ops.assert_scalar(constant_op.constant("foo"))
check_ops.assert_scalar(3)
check_ops.assert_scalar("foo")
with self.assertRaisesRegex(ValueError, "Expected scalar"):
    check_ops.assert_scalar(constant_op.constant([3, 4]))
