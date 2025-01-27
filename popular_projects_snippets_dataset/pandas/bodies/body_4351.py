# Extracted from ./data/repos/pandas/pandas/tests/frame/test_logical_ops.py
d = DataFrame({"a": [np.nan, False], "b": [True, True]})

# GH4947
# bool comparisons should return bool
result = d["a"] | d["b"]
expected = Series([False, True])
tm.assert_series_equal(result, expected)

# GH4604, automatic casting here
result = d["a"].fillna(False) | d["b"]
expected = Series([True, True])
tm.assert_series_equal(result, expected)

result = d["a"].fillna(False, downcast=False) | d["b"]
expected = Series([True, True])
tm.assert_series_equal(result, expected)
