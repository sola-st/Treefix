# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for MatrixInverse."""
ainv = op.outputs[0]
op_adjoint = op.get_attr("adjoint")
exit(-math_ops.matmul(  # pylint: disable=invalid-unary-operand-type
    ainv,
    math_ops.matmul(grad, ainv, adjoint_a=op_adjoint,
                    adjoint_b=not op_adjoint),
    adjoint_a=not op_adjoint))
