# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
self._VerifyValues(
    tensor_in_sizes=[1, 2, 1, 2, 1],
    filter_in_sizes=[2, 1, 2, 1, 2],
    stride=1,
    padding="VALID",
    expected=[1.5625, 1.875])
