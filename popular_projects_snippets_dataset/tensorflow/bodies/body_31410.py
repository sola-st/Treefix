# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 1, 1, 3],
    filter_in_sizes=[2, 2, 3, 3],
    strides=[1, 1],
    padding=[[3, 4], [4, 2]])

self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 1, 1],
    filter_in_sizes=[2, 2, 1, 3],
    strides=[2, 1],
    padding=[[3, 4], [4, 2]])
