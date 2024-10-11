# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# GH#42816
dtype = any_numeric_ea_dtype
arr = np.random.randn(10).astype(dtype.lower(), copy=False)

ser = Series(arr.copy(), dtype=dtype)
ser[1] = pd.NA
result = ser.nlargest(5)

expected = (
    Series(np.delete(arr, 1), index=ser.index.delete(1))
    .nlargest(5)
    .astype(dtype)
)
tm.assert_series_equal(result, expected)
