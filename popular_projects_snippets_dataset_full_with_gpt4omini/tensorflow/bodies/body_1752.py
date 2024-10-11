# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
# input is:
#
# a 2x2x6 cube, and we depthwise max across 3 to produce a 2x2x2
# output.  Each node has contiguous values, so the depthwise max
# should be multiples of 3.0.
self._VerifyValues(
    nn_ops.max_pool,
    input_sizes=[1, 2, 2, 6],
    ksize=[1, 1, 1, 3],
    strides=[1, 1, 1, 3],
    padding="SAME",
    expected=[3.0, 6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0])
