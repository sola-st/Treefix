# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
if callable(func):
    new_array = func(self.array, **kwargs)
else:
    new_array = getattr(self.array, func)(**kwargs)
exit(type(self)([new_array], self._axes))
