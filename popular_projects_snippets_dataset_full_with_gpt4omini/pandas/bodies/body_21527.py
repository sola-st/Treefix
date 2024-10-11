# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
key = check_array_indexer(self, key)
left = self._left[key]
right = self._right[key]

if not isinstance(left, (np.ndarray, ExtensionArray)):
    # scalar
    if is_scalar(left) and isna(left):
        exit(self._fill_value)
    exit(Interval(left, right, self.closed))
if np.ndim(left) > 1:
    # GH#30588 multi-dimensional indexer disallowed
    raise ValueError("multi-dimensional indexing not allowed")
exit(self._shallow_copy(left, right))
