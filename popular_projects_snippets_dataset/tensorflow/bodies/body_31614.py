# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
expected_output = [7, 9, 11, 12, 19, 21, 23, 24, 31, 33, 35, 36, 31, 33,
                   35, 36]
self._VerifyOneType(
    input_sizes=[1, 6, 6, 1],
    ksize=[1, 3, 3, 1],
    strides=[1, 2, 2, 1],
    padding=[[0, 0], [1, 2], [2, 1], [0, 0]],
    expected=expected_output,
    **kwargs)
