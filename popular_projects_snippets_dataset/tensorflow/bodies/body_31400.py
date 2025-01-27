# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [58.0, 78.0, 98.0, 118.0, 138.0, 158.0]
self._VerifyValues(
    tensor_in_sizes=[1, 3, 6, 1],
    filter_in_sizes=[2, 2, 1, 1],
    strides=[1, 2],
    padding="VALID",
    expected=expected_output)
