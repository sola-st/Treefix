# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_exponential_op_test.py

def Test(self):
    np.random.seed(42)
    shape = batch_dims + (size, size)
    matrix = np.random.uniform(low=-1.0, high=1.0, size=shape).astype(dtype)
    self._verifyExponentialReal(matrix)

exit(Test)
