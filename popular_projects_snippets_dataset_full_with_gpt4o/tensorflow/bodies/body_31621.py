# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
expected_output = [
    21.0, 22.0, 23.0, 24.0, 29.0, 30.0, 31.0, 32.0, 53.0, 54.0, 55.0, 56.0,
    61.0, 62.0, 63.0, 64.0
]
self._VerifyOneType(
    input_sizes=[1, 4, 4, 4],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=expected_output,
    **kwargs)
