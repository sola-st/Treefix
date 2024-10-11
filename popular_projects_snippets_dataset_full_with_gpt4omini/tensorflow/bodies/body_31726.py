# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
expected_output = [20.5, 21.5, 22.5]
self._VerifyValues(
    nn_ops.avg_pool3d,
    input_sizes=[1, 3, 3, 3, 3],
    window=(2, 2, 2),
    strides=(2, 2, 2),
    padding="VALID",
    expected=expected_output)
