# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
v = variables.Variable([[1.]])
x = constant_op.constant(1.)
xt = constant_op.constant(2.)
with forwardprop.ForwardAccumulator(x, xt) as acc:
    pass
self.assertIsNone(acc.jvp(v))
self.assertAllClose([[0.]], acc.jvp(v, unconnected_gradients="zero"))
