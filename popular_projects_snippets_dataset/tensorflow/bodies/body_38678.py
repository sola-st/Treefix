# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
rhs0 = np.random.randn(6, 4)

# 6 x 6 matrix with 2 bands. Ensure all non-zero entries.
matrix = 2. * np.random.uniform(size=[3, 6]) + 1.
self._verifySolveAllWaysReal(matrix, rhs0)

# 6 x 6 matrix with 3 bands. Ensure all non-zero entries.
matrix = 2. * np.random.uniform(size=[3, 6]) + 1.
self._verifySolveAllWaysReal(matrix, rhs0)
