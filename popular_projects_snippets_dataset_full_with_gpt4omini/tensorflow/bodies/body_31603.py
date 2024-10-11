# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[1, 3, 3, 3],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 1, 1],
    padding="VALID",
    expected=[7.0, 8.0, 9.0, 10.0, 11.0, 12.0],
    **kwargs)
