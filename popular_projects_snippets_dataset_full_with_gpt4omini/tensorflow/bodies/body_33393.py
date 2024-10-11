# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_util_test.py
x = ops.convert_to_tensor([0., 2, 3])
# Should not raise.
self.evaluate(
    linear_operator_util.assert_zero_imag_part(x, message="ABC123"))
