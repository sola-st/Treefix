# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for MatMul, only for the second input."""
t_a = op.get_attr("transpose_a")
t_b = op.get_attr("transpose_b")
a = math_ops.conj(op.inputs[0])
if not t_a and not t_b:
    grad_b = gen_math_ops.mat_mul(a, grad, transpose_a=True)
elif not t_a and t_b:
    grad_b = gen_math_ops.mat_mul(grad, a, transpose_a=True)
elif t_a and not t_b:
    grad_b = gen_math_ops.mat_mul(a, grad)
elif t_a and t_b:
    grad_b = gen_math_ops.mat_mul(grad, a, transpose_a=True, transpose_b=True)
exit((None, grad_b))
