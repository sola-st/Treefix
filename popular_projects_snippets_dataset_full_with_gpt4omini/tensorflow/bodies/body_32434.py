# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
# Note that the following three strings are regexes
expected_error_msg_full = r"""\[ *0\. +1\. +2\. +3\. +4\. +5\.\]"""
expected_error_msg_default = r"""\[ *0\. +1\. +2\.\]"""
expected_error_msg_short = r"""\[ *0\. +1\.\]"""
with context.eager_mode():
    t = constant_op.constant(
        np.array(range(6)), shape=[2, 3], dtype=np.float32)
    with self.assertRaisesRegex(  # pylint:disable=g-error-prone-assert-raises
        errors.InvalidArgumentError, expected_error_msg_full):
        check_ops.assert_none_equal(
            t, t, message="This is the error message.", summarize=10)
    with self.assertRaisesRegex(  # pylint:disable=g-error-prone-assert-raises
        errors.InvalidArgumentError, expected_error_msg_full):
        check_ops.assert_none_equal(
            t, t, message="This is the error message.", summarize=-1)
    with self.assertRaisesRegex(  # pylint:disable=g-error-prone-assert-raises
        errors.InvalidArgumentError, expected_error_msg_default):
        check_ops.assert_none_equal(t, t, message="This is the error message.")
    with self.assertRaisesRegex(  # pylint:disable=g-error-prone-assert-raises
        errors.InvalidArgumentError, expected_error_msg_short):
        check_ops.assert_none_equal(
            t, t, message="This is the error message.", summarize=2)
