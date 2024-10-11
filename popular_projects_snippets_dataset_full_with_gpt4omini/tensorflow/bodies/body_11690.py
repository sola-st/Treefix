# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
result = self._diagonal_operators[0].log_abs_determinant()
for op in self._diagonal_operators[1:]:
    result += op.log_abs_determinant()
exit(result)
