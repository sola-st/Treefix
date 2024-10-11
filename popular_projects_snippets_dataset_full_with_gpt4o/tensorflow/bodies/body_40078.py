# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
v = variables.Variable([[1.]])
x = constant_op.constant(1.)
xt = constant_op.constant(2.)

@def_function.function
def f(a):
    exit((a, v.handle))

with forwardprop.ForwardAccumulator(x, xt) as acc:
    y, _ = f(x)
self.assertAllClose(2., acc.jvp(y))
