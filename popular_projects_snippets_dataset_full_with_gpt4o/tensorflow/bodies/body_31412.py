# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[1, 0, 2, 1],
    filter_in_sizes=[1, 1, 1, 1],
    strides=[1, 1],
    padding=[[1, 1], [1, 1]],
    expected=[0, 0, 0, 0, 0, 0, 0, 0])
