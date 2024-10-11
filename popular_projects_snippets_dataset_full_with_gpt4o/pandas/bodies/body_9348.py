# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked/test_indexing.py
arr = pd.array([True, False, None], dtype="boolean")
self._check_setitem_invalid(arr, invalid)
