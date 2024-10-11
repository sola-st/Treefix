# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[1, 2, 4, 3],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=[8.5, 9.5, 10.5, 14.5, 15.5, 16.5],
    **kwargs)
