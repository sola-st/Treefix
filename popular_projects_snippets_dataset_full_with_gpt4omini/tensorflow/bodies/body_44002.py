# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/nested_control_flow_test.py
# Note: If the input is a Tensor, the behavior is undefined.
self.assertFunctionMatchesEager(
    if_with_local_modification_masked_by_exception, x)
