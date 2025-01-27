# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
expected_output = [
    21.0, 22.0, 23.0, 24.0, 27.0, 28.0, 29.0, 30.0, 45.0, 46.0, 47.0, 48.0,
    51.0, 52.0, 53.0, 54.0
]
self._VerifyOneType(
    input_sizes=[1, 4, 4, 4],
    ksize=[1, 3, 3, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=expected_output,
    **kwargs)
