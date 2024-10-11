# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# input is:
# [1.0, 2.0
#  3.0  4.0]
#
# Window of [x, x] should do:
#
#  [max(1.0, 2.0), max(2.0, padded0),
#   max(3.0, 4.0), max(4.0, padded0)]
self._VerifyOneType(
    input_sizes=[1, 2, 2, 1],
    ksize=[1, 1, 2, 1],
    strides=[1, 1, 1, 1],
    padding="SAME",
    expected=[2.0, 2.0, 4.0, 4.0],
    **kwargs)
