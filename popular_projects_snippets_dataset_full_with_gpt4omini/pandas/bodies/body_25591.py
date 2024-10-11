# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
if args and kwargs:
    raise AssertionError("Only positional or keyword args are allowed")

self.params = args or kwargs
