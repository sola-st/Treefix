# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py

s = Series(range(6), index=["a", "b", "c", "d", "e", "f"], dtype="int64")
result = read_json(s.to_json(), typ=None)
tm.assert_series_equal(result, s)
