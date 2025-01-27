# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_inverse_op_test.py
for np_type in [np.float16, np.float32, np.float64]:
    self._verifyInverse(x, np_type)
