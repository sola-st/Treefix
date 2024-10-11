# Extracted from ./data/repos/pandas/pandas/core/generic.py
if not copy:
    self._is_copy = None
else:
    assert ref is not None
    self._is_copy = weakref.ref(ref)
