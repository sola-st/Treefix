# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# input is:
# [1.0, 2.0
#  3.0  4.0]
#
# Window of [x, x] should do:
#  [avg(1.0, 2.0), avg(2.0, padded0),
#   avg(3.0, 4.0), avg(4.0, padded0)]
self._VerifyOneType(
    input_sizes=[1, 2, 2, 1],
    ksize=[1, 1, 2, 1],
    strides=[1, 1, 1, 1],
    padding="SAME",
    expected=[1.5, 2.0, 3.5, 4.0],
    **kwargs)
