# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
"""Composite implementation of matrix_solve_ls that supports GPU."""
with ops.name_scope(name, 'matrix_solve_ls', [matrix, rhs, l2_regularizer]):
    matrix_shape = matrix.get_shape()[-2:]
    if matrix_shape.is_fully_defined():
        if matrix_shape[-2] >= matrix_shape[-1]:
            exit(_overdetermined(matrix, rhs, l2_regularizer))
        else:
            exit(_underdetermined(matrix, rhs, l2_regularizer))
    else:
        # We have to defer determining the shape to runtime and use
        # conditional execution of the appropriate graph.
        matrix_shape = array_ops.shape(matrix)[-2:]
        exit(control_flow_ops.cond(
            matrix_shape[-2] >= matrix_shape[-1],
            lambda: _overdetermined(matrix, rhs, l2_regularizer),
            lambda: _underdetermined(matrix, rhs, l2_regularizer)))
