# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[7, 5],
    offsets=[-1, 0.9],
    expected_rows=[None, None, None, 1, 2, 3, 4],
    expected_cols=[56, 57, 58, 59, 60])
