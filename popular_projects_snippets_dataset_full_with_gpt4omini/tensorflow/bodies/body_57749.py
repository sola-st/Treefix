# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Returns a concrete function of the decorated function."""
exit(self._get_func().get_concrete_function(*args, **kwargs))
