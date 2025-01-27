# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# block-wise DataFrame operations will require operating on 2D
#  DatetimeArray/TimedeltaArray, so check that specifically.
dti = date_range("1994-02-13", freq="2W", periods=4)
dta = dti._data.reshape((4, 1))

other = np.array([[pd.offsets.Day(n)] for n in range(4)])
assert other.shape == dta.shape

with tm.assert_produces_warning(PerformanceWarning):
    result = dta + other
with tm.assert_produces_warning(PerformanceWarning):
    expected = (dta[:, 0] + other[:, 0]).reshape(-1, 1)

tm.assert_numpy_array_equal(result, expected)

with tm.assert_produces_warning(PerformanceWarning):
    # Case where we expect to get a TimedeltaArray back
    result2 = dta - dta.astype(object)

assert result2.shape == (4, 1)
assert all(td.value == 0 for td in result2.ravel())
