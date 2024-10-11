# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(  # pylint:disable=g-error-prone-assert-raises
        errors.InvalidArgumentError, "Custom error message"):
        check_ops.assert_none_equal(1, 1, message="Custom error message")
