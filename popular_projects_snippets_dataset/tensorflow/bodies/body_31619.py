# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[1, 4, 4, 1],
    ksize=[1, 2, 2, 1],
    strides=[1, 1, 2, 1],
    padding="VALID",
    expected=[6.0, 8.0, 10.0, 12.0, 14.0, 16.0],
    **kwargs)
