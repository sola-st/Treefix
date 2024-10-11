# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for MatMul."""
try:
    skip_input_indices = op.skip_input_indices
    if skip_input_indices is not None:
        if 1 in skip_input_indices:
            exit(_MatMulGradAgainstFirstOnly(op, grad))
        elif 0 in skip_input_indices:
            exit(_MatMulGradAgainstSecondOnly(op, grad))
except AttributeError:
    # No gradient skipping, so do the full gradient computation
    pass

t_a = op.get_attr("transpose_a")
t_b = op.get_attr("transpose_b")
a = math_ops.conj(op.inputs[0])
b = math_ops.conj(op.inputs[1])
if not t_a and not t_b:
    grad_a = gen_math_ops.mat_mul(grad, b, transpose_b=True)
    grad_b = gen_math_ops.mat_mul(a, grad, transpose_a=True)
elif not t_a and t_b:
    grad_a = gen_math_ops.mat_mul(grad, b)
    grad_b = gen_math_ops.mat_mul(grad, a, transpose_a=True)
elif t_a and not t_b:
    grad_a = gen_math_ops.mat_mul(b, grad, transpose_b=True)
    grad_b = gen_math_ops.mat_mul(a, grad)
elif t_a and t_b:
    grad_a = gen_math_ops.mat_mul(b, grad, transpose_a=True, transpose_b=True)
    grad_b = gen_math_ops.mat_mul(grad, a, transpose_a=True, transpose_b=True)
exit((grad_a, grad_b))
