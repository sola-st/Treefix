# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
expected_output = [2271.0, 2367.0, 2463.0]
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[2, 2, 3, 3],
    strides=[2, 2],
    padding="VALID",
    expected=expected_output)
