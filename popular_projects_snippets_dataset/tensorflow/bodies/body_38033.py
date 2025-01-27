# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/matmul_op_test.py
a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
c = math_ops.matvec(a, b)
self.assertAllEqual((2,), c.shape)
self.assertAllEqual([5 + 2 * 6, 3 * 5 + 4 * 6], c)
