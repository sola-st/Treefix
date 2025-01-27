# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[7, 5],
    offsets=[1.0, 1.0],
    expected_rows=[38, 39, 40, 41, None, None, None],
    expected_cols=[59, 60, 61, None, None])
