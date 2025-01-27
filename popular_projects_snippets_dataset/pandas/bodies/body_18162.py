# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
pi = period_range("2000-12-31", periods=3, freq="D")
parr = pi.array

other = np.array([Timedelta(days=1), pd.offsets.Day(2), 3])

with tm.assert_produces_warning(PerformanceWarning):
    result = parr + other

expected = PeriodIndex(
    ["2001-01-01", "2001-01-03", "2001-01-05"], freq="D"
)._data.astype(object)
tm.assert_equal(result, expected)

with tm.assert_produces_warning(PerformanceWarning):
    result = parr - other

expected = PeriodIndex(["2000-12-30"] * 3, freq="D")._data.astype(object)
tm.assert_equal(result, expected)
