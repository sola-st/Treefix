# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
c = constant_op.constant(1.)
c_tangent = constant_op.constant(2.)
with forwardprop.ForwardAccumulator(c, c_tangent) as acc:
    with backprop.GradientTape(persistent=True) as tape:
        tape.watch(c)
        with tape_lib.stop_recording():
            two = constant_op.constant(2.)
            d = c * two
            three = constant_op.constant(3.)
            e = c * three
        self.assertIsNone(acc.jvp(d))
        self.assertIsNone(acc.jvp(e))
        self.assertIsNone(tape.gradient(d, c))
        self.assertIsNone(tape.gradient(e, c))
        tape_lib.record_operation_forwardprop_only(
            "CustomForwardMul", [d], [c, two], lambda dd: (two * dd, c * dd),
            None)
        tape_lib.record_operation_backprop_only("CustomBackwardMul", [e],
                                                [c, three], lambda de:
                                                (three * de, c * de))
        self.assertAllClose(4., acc.jvp(d))
        self.assertIsNone(acc.jvp(e))
        self.assertIsNone(tape.gradient(d, c))
        self.assertAllClose(3., tape.gradient(e, c))
