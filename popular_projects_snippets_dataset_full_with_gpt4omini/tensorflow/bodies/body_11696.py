# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_block_lower_triangular.py
exit(control_flow_ops.group([
    op.assert_non_singular() for op in self._diagonal_operators]))
