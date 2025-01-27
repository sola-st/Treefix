# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
box = box_with_array
xbox = np.ndarray if box is pd.array else box

tdi = timedelta_range("1 day", periods=3, freq="D")
tdarr = tm.box_expected(tdi, box)

other = np.array([Timedelta(days=1), offsets.Day(2), Timestamp("2000-01-04")])

with tm.assert_produces_warning(PerformanceWarning):
    result = tdarr + other

expected = pd.Index(
    [Timedelta(days=2), Timedelta(days=4), Timestamp("2000-01-07")]
)
expected = tm.box_expected(expected, xbox).astype(object)
tm.assert_equal(result, expected)

msg = "unsupported operand type|cannot subtract a datelike"
with pytest.raises(TypeError, match=msg):
    with tm.assert_produces_warning(PerformanceWarning):
        tdarr - other

with tm.assert_produces_warning(PerformanceWarning):
    result = other - tdarr

expected = pd.Index([Timedelta(0), Timedelta(0), Timestamp("2000-01-01")])
expected = tm.box_expected(expected, xbox).astype(object)
tm.assert_equal(result, expected)
