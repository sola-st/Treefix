# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
self._VerifyDilatedConvValues(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[1, 2, 3, 3],
    strides=[1, 1],
    dilations=[2, 1],
    padding="VALID")
