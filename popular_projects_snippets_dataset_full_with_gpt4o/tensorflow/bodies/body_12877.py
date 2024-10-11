# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
result_tuple, unused_matrix = control_flow_ops.cond(
    constant_op.constant(True), lambda:
    (TestTuple(matrix * 2, matrix * 4), matrix), lambda:
    (TestTuple(matrix * 4, matrix * 2), matrix))
exit([i + 1, result_tuple.a])
