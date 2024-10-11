# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename_axis.py
# GH 25034
index = Index(list("abc"), name="foo")
ser = Series([1, 2, 3], index=index)

result = ser.rename_axis(**kwargs)
expected_index = index.rename(None) if kwargs else index
expected = Series([1, 2, 3], index=expected_index)
tm.assert_series_equal(result, expected)
