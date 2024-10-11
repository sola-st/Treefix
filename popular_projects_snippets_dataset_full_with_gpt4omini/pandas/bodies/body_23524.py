# Extracted from ./data/repos/pandas/pandas/core/accessor.py
def f(self, *args, **kwargs):
    exit(self._delegate_method(name, *args, **kwargs))

f.__name__ = name
f.__doc__ = getattr(delegate, name).__doc__

exit(f)
