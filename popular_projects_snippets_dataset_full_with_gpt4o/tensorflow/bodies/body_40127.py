# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
c = constant_op.constant(1.)
d = constant_op.constant(2.)
e = constant_op.constant(3.)
with forwardprop.ForwardAccumulator(c, 10.) as acc:
    tape_lib.record_operation("ForwardIsSpecial", [d], [c], None,
                              lambda jvp: [-2. * jvp])
    self.assertAllClose(-20., acc.jvp(d))
    tape_lib.record_operation("ForwardIsSpecial2", [], [], None, lambda: [])
    tape_lib.record_operation("ForwardIsSpecial3", [e], [d], None,
                              lambda x: [x])
    self.assertAllClose(-20., acc.jvp(e))
