# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/eig_op_test.py
x = EquilibrateEigenVectorPhases(x, y)
self.assertAllClose(x, y, atol=tol)
