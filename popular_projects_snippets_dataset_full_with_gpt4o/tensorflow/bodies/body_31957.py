# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_3d_test.py
expected_output = [
    0.03703704, 0.11111111, 0.25925926, 0.33333333, 0.7037037, 0.77777778,
    0.92592593, 1.
]
self._VerifyValues(
    tensor_in_sizes=[1, 3, 3, 3, 1],
    filter_in_sizes=[1, 1, 1, 1, 1],
    stride=2,
    padding="SAME",
    expected=expected_output)
self._VerifyValues(
    tensor_in_sizes=[1, 3, 3, 3, 1],
    filter_in_sizes=[1, 1, 1, 1, 1],
    stride=2,
    padding="VALID",
    expected=expected_output)

expected_output = [
    0.54081633, 0.58017493, 0.28061224, 0.81632653, 0.85568513, 0.40306122,
    0.41873178, 0.4340379, 0.19642857, 2.46938776, 2.50874636, 1.1377551,
    2.74489796, 2.78425656, 1.26020408, 1.16873178, 1.1840379, 0.51785714,
    1.09511662, 1.10604956, 0.44642857, 1.17164723, 1.18258017, 0.47704082,
    0.3691691, 0.37244898, 0.125
]
self._VerifyValues(
    tensor_in_sizes=[1, 7, 7, 7, 1],
    filter_in_sizes=[2, 2, 2, 1, 1],
    stride=3,
    padding="SAME",
    expected=expected_output)

expected_output = [
    0.540816, 0.580175, 0.816327, 0.855685, 2.469388, 2.508746, 2.744898,
    2.784257
]
self._VerifyValues(
    tensor_in_sizes=[1, 7, 7, 7, 1],
    filter_in_sizes=[2, 2, 2, 1, 1],
    stride=3,
    padding="VALID",
    expected=expected_output)
