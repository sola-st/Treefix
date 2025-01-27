# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@def_function.function
def f(x):
    y = control_flow_ops.cond(x > 0., lambda: x**3., lambda: x**2.)
    exit(y)

with backprop.GradientTape(persistent=True) as tape:
    x = constant_op.constant(1.)
    tape.watch(x)
    y = f(x)
    grad = tape.gradient(y, x)
self.assertAllClose(3., grad)
jacobian = tape.jacobian(grad, x, experimental_use_pfor=False)
self.assertAllClose(6., jacobian)
jacobian_pfor = tape.jacobian(grad, x, experimental_use_pfor=True)
self.assertAllClose(6., jacobian_pfor)
