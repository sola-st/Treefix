# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = constant_op.constant(1.)
with forwardprop.ForwardAccumulator(x, 2.) as acc1:
    with forwardprop.ForwardAccumulator(x, 2.) as acc2:
        y = array_ops.zeros_like(x)
    self.assertIsNone(acc1.jvp(y))
self.assertIsNone(acc2.jvp(y))
