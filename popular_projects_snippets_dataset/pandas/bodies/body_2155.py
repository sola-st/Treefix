# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH50183
msg = "cannot convert input with unit 'D'"
oneday_in_ns = 1e9 * 60 * 60 * 24
tsmax_in_days = 2**63 / oneday_in_ns  # 2**63 ns, in days
# just in bounds
should_succeed = Series(
    [0, tsmax_in_days - 0.005, -tsmax_in_days + 0.005], dtype=float
)
expected = (should_succeed * oneday_in_ns).astype(np.int64)
for error_mode in ["raise", "coerce", "ignore"]:
    result1 = to_datetime(should_succeed, unit="D", errors=error_mode)
    tm.assert_almost_equal(result1.astype(np.int64), expected, rtol=1e-10)
# just out of bounds
should_fail1 = Series([0, tsmax_in_days + 0.005], dtype=float)
should_fail2 = Series([0, -tsmax_in_days - 0.005], dtype=float)
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(should_fail1, unit="D", errors="raise")
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(should_fail2, unit="D", errors="raise")
