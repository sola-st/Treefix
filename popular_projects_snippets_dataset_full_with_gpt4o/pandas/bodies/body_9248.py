# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
ser = Series(Categorical(["a", "b", "c"], categories=["d", "c", "b", "a"]))
other = Categorical(["b", "c", "a"], categories=["a", "c", "b", "d"])
result = ser.where([True, False, True], other)
expected = Series(Categorical(["a", "c", "c"], dtype=ser.dtype))
tm.assert_series_equal(result, expected)
