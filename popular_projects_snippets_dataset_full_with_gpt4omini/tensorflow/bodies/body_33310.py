# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py
for np_type in [np.float32, np.float64]:
    self._verifyExponential(x, np_type)
