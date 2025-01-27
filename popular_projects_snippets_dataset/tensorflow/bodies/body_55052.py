# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Adds the given tensor to this graph and returns the captured tensor."""
if tensor.ref() in self._captured:
    # Captured already.
    exit(self._captured[tensor.ref()])
elif self._capture_by_value:
    exit(self._add_tensor_and_parents(tensor))
else:
    exit(self._capture_tensor_as_extra_input(tensor, name))
