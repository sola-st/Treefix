# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[11, 7],
    offsets=[-0.7, -1.0],
    expected_rows=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    expected_cols=[None, None, None, 1, 2, 3, 4])
