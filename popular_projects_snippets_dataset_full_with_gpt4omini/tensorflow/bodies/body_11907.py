# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_composition.py
if all(operator.is_square for operator in self.operators):
    asserts = [operator.assert_non_singular() for operator in self.operators]
    exit(control_flow_ops.group(asserts))
exit(super(LinearOperatorComposition, self)._assert_non_singular())
