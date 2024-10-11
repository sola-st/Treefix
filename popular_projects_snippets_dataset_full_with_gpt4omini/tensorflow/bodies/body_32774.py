# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
x = ops.convert_to_tensor(x, name="x")
exit(math_ops.matmul(
    self._matrix, x, adjoint_a=adjoint, adjoint_b=adjoint_arg))
