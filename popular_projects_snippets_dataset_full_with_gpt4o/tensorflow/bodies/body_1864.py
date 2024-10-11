# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
expected_output = [1.5, 4.5, 7.5, 17.5, 20.5, 23.5, 33.5, 36.5, 39.5]
self._VerifyValues(
    nn_ops.avg_pool3d,
    input_sizes=[1, 5, 8, 1, 1],
    window=[1, 2, 3],
    strides=[2, 3, 1],
    padding="SAME",
    expected=expected_output)
