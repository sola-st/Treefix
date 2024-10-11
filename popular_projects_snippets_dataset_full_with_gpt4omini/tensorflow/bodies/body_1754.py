# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
self._VerifyValues(
    nn_ops.max_pool,
    input_sizes=[1, 3, 3, 1],
    ksize=[1, 1, 1, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=[1, 3, 7, 9])

self._VerifyValues(
    nn_ops.max_pool,
    input_sizes=[1, 4, 4, 1],
    ksize=[1, 1, 1, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=[1, 3, 9, 11])
