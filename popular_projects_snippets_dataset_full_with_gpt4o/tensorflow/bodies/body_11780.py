# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
result = self.operators[0].log_abs_determinant()
for operator in self.operators[1:]:
    result += operator.log_abs_determinant()
exit(result)
