# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
with forwardprop.ForwardAccumulator(v, input_tangent) as acc:
    self.assertAllClose([.1, -.2, .3], acc.jvp(v))
    x = v * 2.
    self.assertAllClose([.2, -.4, .6], acc.jvp(x))
    x2 = v + .1
    self.assertAllClose([.1, -.2, .3], acc.jvp(x2))
