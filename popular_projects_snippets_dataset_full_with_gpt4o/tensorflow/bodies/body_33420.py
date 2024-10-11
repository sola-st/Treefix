# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
with self.assertRaisesRegex(ValueError, "empty operators"):
    linear_operator_util.is_aat_form(operators=[])
