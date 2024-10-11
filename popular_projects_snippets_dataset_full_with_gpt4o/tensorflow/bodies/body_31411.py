# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 3, 2, 1],
    filter_in_sizes=[1, 2, 1, 2],
    strides=[1, 1],
    padding=[[1, 0], [0, 1]],
    dilations=[2, 1])

self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 3, 2],
    filter_in_sizes=[3, 2, 2, 1],
    strides=[1, 1],
    padding=[[2, 1], [1, 2]],
    dilations=[2, 3])
