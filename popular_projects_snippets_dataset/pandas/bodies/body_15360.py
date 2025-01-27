# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#31765
ser = Series(range(5), index=Categorical(["a", "b", "c", "a", "b"]))
result = ser["a"]
expected = ser.iloc[[0, 3]]
tm.assert_series_equal(result, expected)
