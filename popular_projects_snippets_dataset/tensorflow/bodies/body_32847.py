# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/svd_op_test.py
atol = (x[0] + y[0]) * tol if len(x) else tol
self.assertAllClose(x, y, atol=atol)
