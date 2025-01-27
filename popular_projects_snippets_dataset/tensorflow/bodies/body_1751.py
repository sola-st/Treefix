# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
# input is:
# [1.0, ..., 10.0] along depth,
#
# We maxpool by depth in patches of 2.
self._VerifyValues(
    nn_ops.max_pool,
    input_sizes=[1, 1, 1, 10],
    ksize=[1, 1, 1, 2],
    strides=[1, 1, 1, 2],
    padding="SAME",
    expected=[2.0, 4.0, 6.0, 8.0, 10.0])
