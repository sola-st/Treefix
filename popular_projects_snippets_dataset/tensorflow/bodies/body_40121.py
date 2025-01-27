# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
v = variables.Variable(1.)
with forwardprop.ForwardAccumulator(v, 11.):
    v.assign_sub(0.5)
    self.assertAllClose(0.5, self.evaluate(v))
