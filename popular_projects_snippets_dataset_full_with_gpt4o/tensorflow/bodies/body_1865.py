# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
expected_output = [40.0, 41.0, 42.0]
self._VerifyValues(
    nn_ops.max_pool3d,
    input_sizes=[1, 3, 3, 3, 3],
    window=[2, 2, 2],
    strides=[2, 2, 2],
    padding="VALID",
    expected=expected_output)
