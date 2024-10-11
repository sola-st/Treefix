# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/self_adjoint_eig_op_test.py
x = EquilibrateEigenVectorPhases(x, y)
self.assertAllClose(x, y, atol=tol)
