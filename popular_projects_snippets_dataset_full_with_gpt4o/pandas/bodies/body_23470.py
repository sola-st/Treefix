# Extracted from ./data/repos/pandas/pandas/core/base.py
if not isinstance(
    self._selection, (list, tuple, ABCSeries, ABCIndex, np.ndarray)
):
    exit([self._selection])
exit(self._selection)
