# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
ser = Series(["a", "b", "a"])
result = ser.astype(CategoricalDtype(["a", "b"], ordered=True))
expected = Series(Categorical(["a", "b", "a"], ordered=True))
tm.assert_series_equal(result, expected)

result = ser.astype(CategoricalDtype(["a", "b"], ordered=False))
expected = Series(Categorical(["a", "b", "a"], ordered=False))
tm.assert_series_equal(result, expected)

result = ser.astype(CategoricalDtype(["a", "b", "c"], ordered=False))
expected = Series(
    Categorical(["a", "b", "a"], categories=["a", "b", "c"], ordered=False)
)
tm.assert_series_equal(result, expected)
tm.assert_index_equal(result.cat.categories, Index(["a", "b", "c"]))
