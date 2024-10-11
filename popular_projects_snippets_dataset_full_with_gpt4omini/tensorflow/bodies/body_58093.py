# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
self.assertTrue(self.interpreter._safe_to_run())
_ = self.interpreter.tensor(self.input0)
self.assertTrue(self.interpreter._safe_to_run())
in0 = self.interpreter.tensor(self.input0)()
self.assertFalse(self.interpreter._safe_to_run())
in0b = self.interpreter.tensor(self.input0)()
self.assertFalse(self.interpreter._safe_to_run())
# Now get rid of the buffers so that we can evaluate.
del in0
del in0b
self.assertTrue(self.interpreter._safe_to_run())
