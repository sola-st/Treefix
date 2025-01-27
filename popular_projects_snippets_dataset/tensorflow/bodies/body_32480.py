# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
with ops.Graph().as_default():
    with self.assertRaisesRegex(errors.InvalidArgumentError,
                                "Custom error message"):
        check_ops.assert_negative(1, message="Custom error message")
