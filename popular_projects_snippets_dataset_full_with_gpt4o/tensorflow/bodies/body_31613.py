# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
expected_output = [9.0, 9.0]
self._VerifyOneType(
    input_sizes=[1, 3, 3, 1],
    ksize=[1, 3, 3, 1],
    strides=[1, 2, 2, 1],
    padding=[[0, 0], [0, 2], [0, 1], [0, 0]],
    expected=expected_output,
    **kwargs)
