# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
full = np.array([[1., 2.], [3., 4.], [5., 6.]])
empty = np.empty([3, 0])
self.assertShapeEqual(
    np.matmul(full.T, empty), math_ops.matmul(full, empty, adjoint_a=True))
self.assertShapeEqual(
    np.matmul(empty.T, full), math_ops.matmul(empty, full, adjoint_a=True))
