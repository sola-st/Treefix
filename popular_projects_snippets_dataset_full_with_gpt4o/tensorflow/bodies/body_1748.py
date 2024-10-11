# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
self._VerifyValues(
    nn_ops.max_pool,
    input_sizes=[1, 4, 4, 1],
    ksize=[1, 2, 2, 1],
    strides=[1, 1, 2, 1],
    padding="VALID",
    expected=[6.0, 8.0, 10.0, 12.0, 14.0, 16.0])
self._VerifyValues(
    nn_ops.max_pool,
    input_sizes=[1, 4, 4, 1],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 1, 1],
    padding="VALID",
    expected=[6.0, 7.0, 8.0, 14.0, 15.0, 16.0])
