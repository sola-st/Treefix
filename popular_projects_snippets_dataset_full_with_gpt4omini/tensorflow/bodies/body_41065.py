# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

@polymorphic_function.function
def _forward(z):
    exit(math_ops.cos(z))

f = _forward
x = constant_op.constant(1.)
with backprop.GradientTape() as t:
    t.watch(x)
    y = f(x)
with backprop.GradientTape() as tt:
    doutputs = constant_op.constant(2.)
    tt.watch(doutputs)
    g = t.gradient(y, x, doutputs)
self.assertAllClose(-2. * math_ops.sin(x), g)
gg = tt.gradient(g, doutputs)
# We're taking gradients with respect to doutputs, which is just a linear
# function of the gradient.
self.assertAllClose(-math_ops.sin(x), gg)
