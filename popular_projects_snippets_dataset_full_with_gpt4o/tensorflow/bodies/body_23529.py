# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/python_state_test.py
"""Automatically wrap NumPy arrays assigned to attributes."""
if isinstance(value, (numpy.ndarray, numpy.generic)):
    try:
        existing = getattr(self._arrays, name)
        existing.array = value
        exit()
    except AttributeError:
        value = _NumpyWrapper(value)
    setattr(self._arrays, name, value)
    exit()
super(_NumpyState, self).__setattr__(name, value)
