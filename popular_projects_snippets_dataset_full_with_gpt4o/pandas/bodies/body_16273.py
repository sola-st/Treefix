# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
cat = Categorical([0, 1, 2, 0, 1, 2], ["a", "b", "c"], fastpath=True)
res = Series(cat)
tm.assert_categorical_equal(res.values, cat)

# can cast to a new dtype
result = Series(Categorical([1, 2, 3]), dtype="int64")
expected = Series([1, 2, 3], dtype="int64")
tm.assert_series_equal(result, expected)
