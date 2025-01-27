# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/attention_ops_test.py
self._VerifyValues(
    tensor_in_sizes=[20, 30],
    glimpse_sizes=[3, 3],
    offsets=[-2.0, 2.0],
    expected_rows=[None, None, None],
    expected_cols=[None, None, None])
