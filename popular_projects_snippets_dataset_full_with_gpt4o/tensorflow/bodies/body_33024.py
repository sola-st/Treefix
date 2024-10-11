# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/cholesky_op_test.py
np.random.seed(0)
shapes = self.getShapes([1, 2, 10])
self.runFiniteDifferences(
    shapes, dtypes=(dtypes_lib.complex64, dtypes_lib.complex128))
