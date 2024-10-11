# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[43, 63],
    offsets=[0.0, 0.0],
    expected_rows=[None] + list(range(1, 42)) + [None],
    expected_cols=[None] + list(range(1, 62)) + [None])
