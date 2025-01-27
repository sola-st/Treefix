# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
expected_output = [31., 32., 33., 34., 35., 36.]
self._VerifyValues(
    nn_ops.max_pool3d,
    input_sizes=[1, 2, 2, 3, 3],
    window=(2, 2, 2),
    strides=(2, 2, 2),
    padding="SAME",
    expected=expected_output)
