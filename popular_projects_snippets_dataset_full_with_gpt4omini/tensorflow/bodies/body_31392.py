# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = []
self._VerifyValues(
    tensor_in_sizes=[0, 2, 3, 3],
    filter_in_sizes=[1, 1, 3, 3],
    strides=[1, 1],
    padding="VALID",
    expected=expected_output)
