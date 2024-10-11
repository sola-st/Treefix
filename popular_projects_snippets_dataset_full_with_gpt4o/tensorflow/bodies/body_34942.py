# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/special_math_test.py
diff = np.diff(array_1d)
np.testing.assert_array_less(0, diff)
