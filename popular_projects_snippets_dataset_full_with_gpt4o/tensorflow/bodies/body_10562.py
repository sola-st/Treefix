# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for MatMul, only for the first input."""
t_a = op.get_attr("transpose_a")
t_b = op.get_attr("transpose_b")
b = math_ops.conj(op.inputs[1])
if not t_a and not t_b:
    grad_a = gen_math_ops.mat_mul(grad, b, transpose_b=True)
elif not t_a and t_b:
    grad_a = gen_math_ops.mat_mul(grad, b)
elif t_a and not t_b:
    grad_a = gen_math_ops.mat_mul(b, grad, transpose_b=True)
elif t_a and t_b:
    grad_a = gen_math_ops.mat_mul(b, grad, transpose_a=True, transpose_b=True)
exit((grad_a, None))
