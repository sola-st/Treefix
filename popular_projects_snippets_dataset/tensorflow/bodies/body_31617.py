# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._VerifyOneType(
    input_sizes=[1, 3, 1],
    ksize=[1, 2, 1],
    strides=[1, 2, 1],
    padding=[[0, 0], [0, 1], [0, 0]],
    expected=[2.0, 3.0],
    **kwargs)
