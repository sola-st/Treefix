# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
data = ma.masked_all((3,), dtype=float)
result = Series(data)
expected = Series([np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)

data[0] = 0.0
data[2] = 2.0
index = ["a", "b", "c"]
result = Series(data, index=index)
expected = Series([0.0, np.nan, 2.0], index=index)
tm.assert_series_equal(result, expected)

data[1] = 1.0
result = Series(data, index=index)
expected = Series([0.0, 1.0, 2.0], index=index)
tm.assert_series_equal(result, expected)

data = ma.masked_all((3,), dtype=int)
result = Series(data)
expected = Series([np.nan, np.nan, np.nan], dtype=float)
tm.assert_series_equal(result, expected)

data[0] = 0
data[2] = 2
index = ["a", "b", "c"]
result = Series(data, index=index)
expected = Series([0, np.nan, 2], index=index, dtype=float)
tm.assert_series_equal(result, expected)

data[1] = 1
result = Series(data, index=index)
expected = Series([0, 1, 2], index=index, dtype=int)
tm.assert_series_equal(result, expected)

data = ma.masked_all((3,), dtype=bool)
result = Series(data)
expected = Series([np.nan, np.nan, np.nan], dtype=object)
tm.assert_series_equal(result, expected)

data[0] = True
data[2] = False
index = ["a", "b", "c"]
result = Series(data, index=index)
expected = Series([True, np.nan, False], index=index, dtype=object)
tm.assert_series_equal(result, expected)

data[1] = True
result = Series(data, index=index)
expected = Series([True, True, False], index=index, dtype=bool)
tm.assert_series_equal(result, expected)

data = ma.masked_all((3,), dtype="M8[ns]")
result = Series(data)
expected = Series([iNaT, iNaT, iNaT], dtype="M8[ns]")
tm.assert_series_equal(result, expected)

data[0] = datetime(2001, 1, 1)
data[2] = datetime(2001, 1, 3)
index = ["a", "b", "c"]
result = Series(data, index=index)
expected = Series(
    [datetime(2001, 1, 1), iNaT, datetime(2001, 1, 3)],
    index=index,
    dtype="M8[ns]",
)
tm.assert_series_equal(result, expected)

data[1] = datetime(2001, 1, 2)
result = Series(data, index=index)
expected = Series(
    [datetime(2001, 1, 1), datetime(2001, 1, 2), datetime(2001, 1, 3)],
    index=index,
    dtype="M8[ns]",
)
tm.assert_series_equal(result, expected)
