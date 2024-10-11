# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
expected_output = [
    3.77199074, 3.85069444, 3.92939815, 2.0162037, 2.06597222, 2.11574074,
    9.68865741, 9.93402778, 10.17939815, 4.59953704, 4.73263889, 4.86574074
]
self._VerifyValues(
    tensor_in_sizes=[1, 4, 2, 3, 3],
    filter_in_sizes=[2, 2, 2, 3, 3],
    stride=2,
    padding="SAME",
    expected=expected_output)
