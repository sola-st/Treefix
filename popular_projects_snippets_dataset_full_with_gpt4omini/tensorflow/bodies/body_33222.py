# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_triangular_solve_op_test.py
self._verifySolve(np.empty([0, 2, 2]), np.empty([0, 2, 2]), lower=True)
self._verifySolve(np.empty([2, 0, 0]), np.empty([2, 0, 0]), lower=True)
self._verifySolve(np.empty([2, 0, 0]), np.empty([2, 0, 0]), lower=False)
self._verifySolve(
    np.empty([2, 0, 0]), np.empty([2, 0, 0]), lower=True, batch_dims=[3, 2])
self._verifySolve(np.empty([0, 0]), np.empty([0, 0]), lower=True)
