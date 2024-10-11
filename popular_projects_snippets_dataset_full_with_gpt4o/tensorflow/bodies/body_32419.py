# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
expected_error_msg_full = r"""big does not equal small
Condition x == y did not hold.
Indices of first 3 different values:
\[\[0 0\]
 \[1 1\]
 \[2 0\]\]
Corresponding x values:
\[2 3 6\]
Corresponding y values:
\[20 30 60\]
First 6 elements of x:
\[2 2 3 3 6 6\]
First 6 elements of y:
\[20  2  3 30 60  6\]"""
expected_error_msg_default = r"""big does not equal small
Condition x == y did not hold.
Indices of first 3 different values:
\[\[0 0\]
 \[1 1\]
 \[2 0\]\]
Corresponding x values:
\[2 3 6\]
Corresponding y values:
\[20 30 60\]
First 3 elements of x:
\[2 2 3\]
First 3 elements of y:
\[20  2  3\]"""
expected_error_msg_short = r"""big does not equal small
Condition x == y did not hold.
Indices of first 2 different values:
\[\[0 0\]
 \[1 1\]\]
Corresponding x values:
\[2 3\]
Corresponding y values:
\[20 30\]
First 2 elements of x:
\[2 2\]
First 2 elements of y:
\[20  2\]"""
with context.eager_mode():
    big = constant_op.constant([[2, 2], [3, 3], [6, 6]])
    small = constant_op.constant([[20, 2], [3, 30], [60, 6]])
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                expected_error_msg_full):
        check_ops.assert_equal(big, small, message="big does not equal small",
                               summarize=10)
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                expected_error_msg_default):
        check_ops.assert_equal(big, small, message="big does not equal small")
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                expected_error_msg_short):
        check_ops.assert_equal(big, small, message="big does not equal small",
                               summarize=2)
