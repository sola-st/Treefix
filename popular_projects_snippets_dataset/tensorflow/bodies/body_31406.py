# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 3, 2],
    filter_in_sizes=[2, 2, 2, 2],
    strides=[1, 1],
    padding=[[1, 1], [1, 1]])

self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 2, 1],
    filter_in_sizes=[1, 1, 1, 2],
    strides=[1, 1],
    padding=[[1, 1], [1, 1]])
