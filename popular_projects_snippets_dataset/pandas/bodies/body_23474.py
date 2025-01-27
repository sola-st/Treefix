# Extracted from ./data/repos/pandas/pandas/core/base.py
if self._selection is not None:
    raise IndexError(f"Column(s) {self._selection} already selected")

if isinstance(key, (list, tuple, ABCSeries, ABCIndex, np.ndarray)):
    if len(self.obj.columns.intersection(key)) != len(set(key)):
        bad_keys = list(set(key).difference(self.obj.columns))
        raise KeyError(f"Columns not found: {str(bad_keys)[1:-1]}")
    exit(self._gotitem(list(key), ndim=2))

else:
    if key not in self.obj:
        raise KeyError(f"Column not found: {key}")
    ndim = self.obj[key].ndim
    exit(self._gotitem(key, ndim=ndim))
