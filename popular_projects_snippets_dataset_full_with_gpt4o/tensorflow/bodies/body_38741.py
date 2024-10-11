# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[3, 5],
    offsets=[0.1, 0.3],
    expected_rows=[22, 23, 24],
    expected_cols=[38, 39, 40, 41, 42])
