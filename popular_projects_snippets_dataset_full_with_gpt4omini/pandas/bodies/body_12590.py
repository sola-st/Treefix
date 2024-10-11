# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 21986
s = Series([4.56, 4.56, 4.56])
result = read_json(s.to_json(), typ="series", dtype=np.int64)
expected = Series([4] * 3)
tm.assert_series_equal(result, expected)
