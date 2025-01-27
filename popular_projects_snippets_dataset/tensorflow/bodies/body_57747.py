# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Returns decorated function object.

    For a class method, use self._obj_func to provide `self` instance.
    """
if self._obj_func is not None:
    exit(self._obj_func)
else:
    exit(self._func)
