# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
expected_output = [7., 8., 9., 11.5, 12.5, 13.5]
self._VerifyValues(
    nn_ops.avg_pool,
    input_sizes=[1, 2, 3, 3],
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding="SAME",
    expected=expected_output)
