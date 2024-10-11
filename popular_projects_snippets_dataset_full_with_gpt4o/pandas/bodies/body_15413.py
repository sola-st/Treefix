# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
orig = obj
obj = obj.copy()
arr = obj._values

indexer(obj)[key] = val
tm.assert_series_equal(obj, expected)

self._check_inplace(is_inplace, orig, arr, obj)
