# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
expected_output = [
    3.77199074, 3.85069444, 3.92939815, 4.2650463, 4.35763889, 4.45023148,
    6.73032407, 6.89236111, 7.05439815, 7.22337963, 7.39930556, 7.57523148,
    9.68865741, 9.93402778, 10.17939815, 10.18171296, 10.44097222,
    10.70023148
]
# expected_shape = [1, 3, 1, 2, 5]
self._VerifyValues(
    tensor_in_sizes=[1, 4, 2, 3, 3],  # b, z, y, x, fin
    filter_in_sizes=[2, 2, 2, 3, 3],  # z, y, x, fin, fout
    stride=1,
    padding="VALID",
    expected=expected_output)
