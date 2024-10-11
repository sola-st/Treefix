# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_composition.py
result = self.operators[0].determinant()
for operator in self.operators[1:]:
    result *= operator.determinant()
exit(result)
