# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
"""Check that tensor returns a reference."""
array_ref = self.interpreter.tensor(self.input0)
np.copyto(array_ref(), self.initial_data)
self.assertAllEqual(array_ref(), self.initial_data)
self.assertAllEqual(
    self.interpreter.get_tensor(self.input0), self.initial_data)
