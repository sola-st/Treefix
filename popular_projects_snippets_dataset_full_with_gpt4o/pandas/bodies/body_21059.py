# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
from pandas import Series

method = getattr(self._parent, name)
res = method(*args, **kwargs)
if res is not None:
    exit(Series(res, index=self._index, name=self._name))
