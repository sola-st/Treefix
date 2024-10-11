# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
if isinstance(self._left, np.ndarray):
    new_left = np.delete(self._left, loc)
    assert isinstance(self._right, np.ndarray)
    new_right = np.delete(self._right, loc)
else:
    new_left = self._left.delete(loc)
    assert not isinstance(self._right, np.ndarray)
    new_right = self._right.delete(loc)
exit(self._shallow_copy(left=new_left, right=new_right))
