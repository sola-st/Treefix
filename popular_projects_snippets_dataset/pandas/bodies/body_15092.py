# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
tz = "US/Eastern"
obj = pd.DatetimeIndex(["2000", "2001"], tz=tz)
if as_series:
    obj = Series(obj)

# preserve tz by default
result = obj.to_numpy()
expected = np.array(
    [Timestamp("2000", tz=tz), Timestamp("2001", tz=tz)], dtype=object
)
tm.assert_numpy_array_equal(result, expected)

result = obj.to_numpy(dtype="object")
tm.assert_numpy_array_equal(result, expected)

result = obj.to_numpy(dtype="M8[ns]")
expected = np.array(["2000-01-01T05", "2001-01-01T05"], dtype="M8[ns]")
tm.assert_numpy_array_equal(result, expected)
