# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with backprop.GradientTape(persistent=True) as g:
    g.watch(variables)
    y = c(x)
grad_vars = [
    2 * math_ops.reduce_sum(dy * g.jacobian(y, v)) for v in variables
]
del g
exit(((), grad_vars))
