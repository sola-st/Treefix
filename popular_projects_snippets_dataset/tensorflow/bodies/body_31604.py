# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
expected_output = [
    11.0, 12.0, 13.0, 14.0, 19.0, 20.0, 21.0, 22.0, 43.0, 44.0, 45.0, 46.0,
    51.0, 52.0, 53.0, 54.0
]
self._VerifyOneType(
    input_sizes=[1, 4, 4, 4],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=expected_output,
    **kwargs)
