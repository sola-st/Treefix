# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
if all(op.is_positive_definite for op in self._diagonal_operators):
    exit(math_ops.exp(self._log_abs_determinant()))
result = self._diagonal_operators[0].determinant()
for op in self._diagonal_operators[1:]:
    result *= op.determinant()
exit(result)
