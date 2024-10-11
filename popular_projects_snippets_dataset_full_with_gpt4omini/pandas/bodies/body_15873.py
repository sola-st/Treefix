# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# https://github.com/pandas-dev/pandas/issues/34530
obj = frame_or_series(pd.array([1, 2, 3], dtype="Int64"))
result = obj.replace("", "")  # no exception
# should not have changed dtype
tm.assert_equal(obj, result)
