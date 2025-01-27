# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
# used in get_numeric_data / get_bool_data
if predicate(self.array):
    exit(type(self)(self.arrays, self._axes, verify_integrity=False))
else:
    exit(self.make_empty())
