# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_logarithm_op_test.py
np.random.seed(42)
for batch_dims in [(), (1,), (3,), (2, 2)]:
    for size in 8, 31, 32:
        shape = batch_dims + (size, size)
        matrix = np.random.uniform(
            low=-1.0, high=1.0,
            size=np.prod(shape)).reshape(shape).astype(np.complex64)
        self._verifyLogarithmComplex(matrix)
