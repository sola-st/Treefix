# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[2, 2, 2, 2],
    ksize=[1, 2, 1, 1],
    strides=[1, 1, 1, 1],
    padding="SAME",
    expected=[
        3.0, 4.0, 5.0, 6.0, 5.0, 6.0, 7.0, 8.0, 11.0, 12.0, 13.0, 14.0,
        13.0, 14.0, 15.0, 16.0
    ],
    **kwargs)
