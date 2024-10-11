# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
rhs = ops.convert_to_tensor(rhs, name="rhs")
assert not adjoint_arg, "Not implemented for this test class."
exit(linalg_ops.matrix_solve(self._matrix, rhs, adjoint=adjoint))
