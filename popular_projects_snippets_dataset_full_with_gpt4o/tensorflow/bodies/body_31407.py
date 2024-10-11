# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 1, 2],
    filter_in_sizes=[2, 1, 2, 1],
    strides=[1, 1],
    padding=[[2, 2], [2, 2]])

self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 1, 2],
    filter_in_sizes=[1, 1, 2, 1],
    strides=[2, 1],
    padding=[[2, 2], [2, 2]])
