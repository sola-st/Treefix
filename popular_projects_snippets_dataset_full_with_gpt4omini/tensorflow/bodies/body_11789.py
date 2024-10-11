# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_diag.py
exit(control_flow_ops.group([
    operator.assert_positive_definite() for operator in self.operators]))
