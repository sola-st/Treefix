# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[1, 3, 3, 1],
    ksize=[1, 1, 1, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=[1, 3, 7, 9],
    **kwargs)
