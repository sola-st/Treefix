# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_formats.py
index = pd.date_range(freq="1D", periods=3, start="2017-01-01")

# First, with no arguments.
expected = np.array(["2017-01-01", "2017-01-02", "2017-01-03"], dtype=object)

result = index._format_native_types()
tm.assert_numpy_array_equal(result, expected)

# No NaN values, so na_rep has no effect
result = index._format_native_types(na_rep="pandas")
tm.assert_numpy_array_equal(result, expected)

# Make sure date formatting works
expected = np.array(["01-2017-01", "01-2017-02", "01-2017-03"], dtype=object)

result = index._format_native_types(date_format="%m-%Y-%d")
tm.assert_numpy_array_equal(result, expected)

# NULL object handling should work
index = DatetimeIndex(["2017-01-01", pd.NaT, "2017-01-03"])
expected = np.array(["2017-01-01", "NaT", "2017-01-03"], dtype=object)

result = index._format_native_types()
tm.assert_numpy_array_equal(result, expected)

expected = np.array(["2017-01-01", "pandas", "2017-01-03"], dtype=object)

result = index._format_native_types(na_rep="pandas")
tm.assert_numpy_array_equal(result, expected)

result = index._format_native_types(date_format="%Y-%m-%d %H:%M:%S.%f")
expected = np.array(
    ["2017-01-01 00:00:00.000000", "NaT", "2017-01-03 00:00:00.000000"],
    dtype=object,
)
tm.assert_numpy_array_equal(result, expected)

# invalid format
result = index._format_native_types(date_format="foo")
expected = np.array(["foo", "NaT", "foo"], dtype=object)
tm.assert_numpy_array_equal(result, expected)
