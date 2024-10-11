# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = ops.convert_to_tensor([1., 2, 0])
y = ops.convert_to_tensor([1., 2, 0])
z = math_ops.complex(x, y)
with self.assertRaisesOpError("ABC123"):
    self.evaluate(
        linear_operator_util.assert_no_entries_with_modulus_zero(
            z, message="ABC123"))
