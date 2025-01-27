# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
ser = Series(Categorical(["a", "b", "c"], categories=["d", "c", "b", "a"]))
result = ser.where([True, True, False], other="b")
expected = Series(Categorical(["a", "b", "b"], categories=ser.cat.categories))
tm.assert_series_equal(result, expected)
