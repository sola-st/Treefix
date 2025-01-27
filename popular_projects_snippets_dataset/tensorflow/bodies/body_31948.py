# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
expected_output = [
    0.18518519, 0.22222222, 0.25925926, 0.40740741, 0.5, 0.59259259,
    0.62962963, 0.77777778, 0.92592593, 0.85185185, 1.05555556, 1.25925926,
    1.07407407, 1.33333333, 1.59259259, 1.2962963, 1.61111111, 1.92592593
]

# These are equivalent to the Conv2D1x1 case.
self._VerifyValues(
    tensor_in_sizes=[1, 2, 3, 1, 3],
    filter_in_sizes=[1, 1, 1, 3, 3],
    stride=1,
    padding="VALID",
    expected=expected_output)
self._VerifyValues(
    tensor_in_sizes=[1, 2, 1, 3, 3],
    filter_in_sizes=[1, 1, 1, 3, 3],
    stride=1,
    padding="VALID",
    expected=expected_output)
self._VerifyValues(
    tensor_in_sizes=[1, 1, 2, 3, 3],
    filter_in_sizes=[1, 1, 1, 3, 3],
    stride=1,
    padding="VALID",
    expected=expected_output)
