# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = ops.convert_to_tensor([1., 0, 3])
with self.assertRaisesOpError("ABC123"):
    self.evaluate(
        linear_operator_util.assert_no_entries_with_modulus_zero(
            x, message="ABC123"))
