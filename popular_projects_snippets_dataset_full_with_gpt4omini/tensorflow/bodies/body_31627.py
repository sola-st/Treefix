# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[1, 7, 7, 1],
    ksize=[1, 2, 2, 1],
    strides=[1, 3, 3, 1],
    padding="VALID",
    expected=[9, 12, 30, 33],
    **kwargs)
