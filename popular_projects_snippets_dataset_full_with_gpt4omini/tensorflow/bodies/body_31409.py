# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[2, 2, 3, 2],
    strides=[1, 1],
    padding=[[1, 0], [0, 2]],
    tol=5e-5)

self._VerifyExplicitPaddings(
    tensor_in_sizes=[1, 2, 4, 2],
    filter_in_sizes=[2, 2, 2, 2],
    strides=[1, 3],
    padding=[[1, 0], [0, 2]])
