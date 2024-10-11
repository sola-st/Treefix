# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = constant_op.constant(-1.)
with forwardprop.ForwardAccumulator(x, 0.1) as acc:
    self.assertAllClose(0.1, acc.jvp(x, unconnected_gradients="zero"))
    self.assertAllClose(0.1, acc.jvp(x, unconnected_gradients="none"))
    y = constant_op.constant(-2.)
    self.assertAllClose(0.0, acc.jvp(y, unconnected_gradients="zero"))
    self.assertIsNone(acc.jvp(y, unconnected_gradients="none"))
