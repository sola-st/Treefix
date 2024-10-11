# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
matrix_t = array_ops.matrix_transpose(matrix)
exit(control_flow_ops.with_dependencies(
    [check_ops.assert_equal(matrix, matrix_t)], matrix))
