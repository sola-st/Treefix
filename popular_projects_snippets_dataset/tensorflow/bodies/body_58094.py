# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
in0 = self.interpreter.tensor(self.input0)()
# Make sure we get an exception if we try to run an unsafe operation
with self.assertRaisesRegex(RuntimeError, 'There is at least 1 reference'):
    _ = self.interpreter.allocate_tensors()
# Make sure we get an exception if we try to run an unsafe operation
with self.assertRaisesRegex(RuntimeError, 'There is at least 1 reference'):
    _ = self.interpreter.invoke()  # pylint: disable=assignment-from-no-return
# Now test that we can run
del in0  # this is our only buffer reference, so now it is safe to change
in0safe = self.interpreter.tensor(self.input0)
_ = self.interpreter.allocate_tensors()
del in0safe  # make sure in0Safe is held but lint doesn't complain
