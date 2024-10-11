# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[1, 3, 3, 1],
    filter_in_sizes=[1, 1, 1, 1],
    strides=[2, 2],
    padding="SAME",
    expected=[1, 3, 7, 9])

self._VerifyValues(
    tensor_in_sizes=[1, 4, 4, 1],
    filter_in_sizes=[1, 1, 1, 1],
    strides=[2, 2],
    padding="SAME",
    expected=[1, 3, 9, 11])

self._VerifyValues(
    tensor_in_sizes=[1, 4, 4, 1],
    filter_in_sizes=[2, 2, 1, 1],
    strides=[3, 3],
    padding="SAME",
    expected=[44, 28, 41, 16])
