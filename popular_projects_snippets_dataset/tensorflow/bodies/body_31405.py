# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[2, 2, 3, 3],
    strides=[1, 1],
    padding=[[0, 0], [0, 0]])

self._VerifyExplicitPaddings(
    tensor_in_sizes=[3, 4, 3, 2],
    filter_in_sizes=[1, 1, 2, 1],
    strides=[2, 2],
    padding=[[0, 0], [0, 0]])
