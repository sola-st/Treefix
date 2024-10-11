# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Unbox either a scalar with _unbox_scalar or an instance of our own type.
        """
if lib.is_scalar(other):
    other = self._unbox_scalar(other)
else:
    # same type as self
    self._check_compatible_with(other)
    other = other._ndarray
exit(other)
