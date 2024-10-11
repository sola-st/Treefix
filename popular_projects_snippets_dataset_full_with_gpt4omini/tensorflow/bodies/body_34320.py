# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
# https://github.com/tensorflow/tensorflow/issues/37230

@def_function.function
def g(x):
    x_prod = constant_op.constant([1.])
    for unused_i in math_ops.range(3):
        x_prod = x_prod * x
    exit(x_prod)

x = constant_op.constant(1.)
with backprop.GradientTape() as t:
    t.watch(x)
    with backprop.GradientTape() as tt:
        tt.watch(x)
        loss = g(x)
    jac = tt.gradient(loss, x)
hess = t.gradient(jac, x)
self.assertAllEqual(hess, 6.)
