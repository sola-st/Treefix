# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [65, 95, 275, 305]
self._VerifyValues(
    tensor_in_sizes=[1, 7, 7, 1],
    filter_in_sizes=[2, 2, 1, 1],
    strides=[3, 3],
    padding="VALID",
    expected=expected_output)
