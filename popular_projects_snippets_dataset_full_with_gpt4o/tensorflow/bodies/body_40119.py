# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
c = constant_op.constant(1.)
c_tangent = constant_op.constant(2.)
with forwardprop.ForwardAccumulator(c, c_tangent) as acc:
    with backprop.GradientTape() as tape:
        self.assertFalse(tape_lib.should_record_backprop([c]))
        self.assertEqual(1, pywrap_tfe.TFE_Py_TapeSetPossibleGradientTypes([c]))
        tape.watch(c)
        self.assertEqual(2, pywrap_tfe.TFE_Py_TapeSetPossibleGradientTypes([c]))
        self.assertTrue(tape_lib.should_record_backprop([c]))
        with tape_lib.stop_recording():
            self.assertEqual(0,
                             pywrap_tfe.TFE_Py_TapeSetPossibleGradientTypes([c]))
            self.assertFalse(tape_lib.should_record_backprop([c]))
            d = c * 2.
        self.assertEqual(2, pywrap_tfe.TFE_Py_TapeSetPossibleGradientTypes([c]))
        self.assertTrue(tape_lib.should_record_backprop([c]))
        self.assertFalse(tape_lib.should_record_backprop([d]))
        self.assertIsNone(acc.jvp(d))
    self.assertIsNone(tape.gradient(d, c))
