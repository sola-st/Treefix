# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
rng = timedelta_range("2 days", periods=5, freq="2D", name="x")

result = rng + 1 * rng.freq
exp = timedelta_range("4 days", periods=5, freq="2D", name="x")
tm.assert_index_equal(result, exp)
assert result.freq == "2D"

result = rng - 2 * rng.freq
exp = timedelta_range("-2 days", periods=5, freq="2D", name="x")
tm.assert_index_equal(result, exp)
assert result.freq == "2D"

result = rng * 2
exp = timedelta_range("4 days", periods=5, freq="4D", name="x")
tm.assert_index_equal(result, exp)
assert result.freq == "4D"

result = rng / 2
exp = timedelta_range("1 days", periods=5, freq="D", name="x")
tm.assert_index_equal(result, exp)
assert result.freq == "D"

result = -rng
exp = timedelta_range("-2 days", periods=5, freq="-2D", name="x")
tm.assert_index_equal(result, exp)
assert result.freq == "-2D"

rng = timedelta_range("-2 days", periods=5, freq="D", name="x")

result = abs(rng)
exp = TimedeltaIndex(
    ["2 days", "1 days", "0 days", "1 days", "2 days"], name="x"
)
tm.assert_index_equal(result, exp)
assert result.freq is None
