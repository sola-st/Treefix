# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
"""Check that get_tensor returns a copy."""
self.interpreter.set_tensor(self.input0, self.initial_data)
array_initial_copy = self.interpreter.get_tensor(self.input0)
new_value = np.add(1., array_initial_copy)
self.interpreter.set_tensor(self.input0, new_value)
self.assertAllEqual(array_initial_copy, self.initial_data)
self.assertAllEqual(self.interpreter.get_tensor(self.input0), new_value)
