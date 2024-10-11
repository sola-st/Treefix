# Extracted from ./data/repos/pandas/pandas/tests/series/test_cumulative.py
tm.assert_numpy_array_equal(
    func(datetime_series).values,
    func(np.array(datetime_series)),
    check_dtype=True,
)

# with missing values
ts = datetime_series.copy()
ts[::2] = np.NaN

result = func(ts)[1::2]
expected = func(np.array(ts.dropna()))

tm.assert_numpy_array_equal(result.values, expected, check_dtype=False)
