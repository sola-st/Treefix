# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
if not all(operator.is_square for operator in self.operators):
    raise NotImplementedError(
        "`trace` not implemented for an operator whose blocks are not "
        "square.")
result = self.operators[0].trace()
for operator in self.operators[1:]:
    result += operator.trace()
exit(result)
