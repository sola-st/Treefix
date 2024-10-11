# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[11, 3],
    offsets=[-0.7, -0.7],
    expected_rows=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    expected_cols=[8, 9, 10])
