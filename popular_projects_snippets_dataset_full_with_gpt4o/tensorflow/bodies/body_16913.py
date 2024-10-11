# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/quantized_conv_ops_test.py
# With a shift of 21, we should execute the optimized path here.
expected_output = [2271.0, 2367.0, 2463.0]
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 3],
    filter_in_sizes=[2, 2, 3, 3],
    stride=2,
    padding="VALID",
    expected=expected_output)
