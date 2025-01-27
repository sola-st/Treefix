# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
expected_output = [20.5, 21.5, 22.5, 26.5, 27.5, 28.5]
self._VerifyValues(
    nn_ops.avg_pool3d,
    input_sizes=[1, 2, 2, 4, 3],
    window=[2, 2, 2],
    strides=[2, 2, 2],
    padding="SAME",
    expected=expected_output)
