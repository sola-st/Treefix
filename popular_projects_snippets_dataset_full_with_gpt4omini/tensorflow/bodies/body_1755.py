# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
expected_output = [7, 8, 9]
self._VerifyValues(
    nn_ops.avg_pool,
    input_sizes=[1, 3, 3, 3],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="VALID",
    expected=expected_output)
