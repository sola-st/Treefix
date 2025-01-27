# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/determinant_op_test.py
max_double = np.finfo("d").max
huge_matrix = np.array([[max_double, 0.0], [0.0, max_double]])
self._compareDeterminant(huge_matrix)
