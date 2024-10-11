# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[3, 5],
    offsets=[0.0, 0.0],
    expected_rows=[20, 21, 22],
    expected_cols=[29, 30, 31, 32, 33])
