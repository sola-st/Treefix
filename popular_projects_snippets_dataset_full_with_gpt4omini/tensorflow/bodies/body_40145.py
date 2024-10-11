# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
y = constant_op.constant(1.)
with forwardprop.ForwardAccumulator(y, 1.) as acc:
    self.assertAllClose(3., acc.jvp(_has_cond(constant_op.constant(5), y)))
    self.assertAllClose(0., acc.jvp(_has_cond(constant_op.constant(0), y)))
