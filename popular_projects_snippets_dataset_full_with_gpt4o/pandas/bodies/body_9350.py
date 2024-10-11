# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_indexing.py
arr = pd.array([1, 2, None], dtype=float_ea_dtype)
self._check_setitem_invalid(arr, invalid)
