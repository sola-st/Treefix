# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linalg_ops_test.py
q = linalg.qr(random_ops.random_uniform([3, 3], dtype=self.dtype))[0]
e = constant_op.constant([0.1, 0.2, 0.3], dtype=self.dtype)
a = linalg.solve(q, linalg.transpose(a=e * q), adjoint=True)
self.assertAllEqual([3, 2, 1, 0],
                    self.evaluate(
                        linalg.matrix_rank(
                            a, tol=[[0.09], [0.19], [0.29], [0.31]])))
