# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/def_function.py
self._python_func = func
# TODO(srbs): Uniquify this name.
self.name = name or func.__name__
