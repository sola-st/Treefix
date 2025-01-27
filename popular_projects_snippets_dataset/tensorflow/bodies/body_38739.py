# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[41, 61],
    glimpse_sizes=[41, 61],
    offsets=[0.0, 0.0],
    expected_rows=list(range(1, 42)),
    expected_cols=list(range(1, 62)))
