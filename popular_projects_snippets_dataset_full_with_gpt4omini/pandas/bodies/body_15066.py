# Extracted from ./data/repos/pandas/pandas/tests/base/test_transpose.py
obj = index_or_series_obj
tm.assert_equal(obj.transpose(), obj)
