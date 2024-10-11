# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
ser = Series(Categorical(["a", "b"]))
result = ser.where([True, False])
expected = Series(Categorical(["a", None], categories=["a", "b"]))
tm.assert_series_equal(result, expected)

# all NA
ser = Series(Categorical(["a", "b"]))
result = ser.where([False, False])
expected = Series(Categorical([None, None], categories=["a", "b"]))
tm.assert_series_equal(result, expected)
