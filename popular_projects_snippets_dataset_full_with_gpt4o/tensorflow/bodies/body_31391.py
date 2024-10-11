# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyDilatedConvValues(
    tensor_in_sizes=[1, 4, 4, 1],
    filter_in_sizes=[2, 2, 1, 1],
    strides=[1, 1],
    dilations=[2, 1],
    padding="VALID")
