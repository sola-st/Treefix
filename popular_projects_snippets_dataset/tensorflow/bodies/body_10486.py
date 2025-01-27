# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
y = op.outputs[0]  # y = x^(1/2)
exit(gen_math_ops.sqrt_grad(y, grad))
