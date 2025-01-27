# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_shift.py
# GH#9903
tz = tz_naive_fixture
idx = DatetimeIndex([], name="xxx", tz=tz)
tm.assert_index_equal(idx.shift(0, freq="H"), idx)
tm.assert_index_equal(idx.shift(3, freq="H"), idx)

idx = DatetimeIndex(
    ["2011-01-01 10:00", "2011-01-01 11:00", "2011-01-01 12:00"],
    name="xxx",
    tz=tz,
    freq="H",
)
tm.assert_index_equal(idx.shift(0, freq="H"), idx)
exp = DatetimeIndex(
    ["2011-01-01 13:00", "2011-01-01 14:00", "2011-01-01 15:00"],
    name="xxx",
    tz=tz,
    freq="H",
)
tm.assert_index_equal(idx.shift(3, freq="H"), exp)
exp = DatetimeIndex(
    ["2011-01-01 07:00", "2011-01-01 08:00", "2011-01-01 09:00"],
    name="xxx",
    tz=tz,
    freq="H",
)
tm.assert_index_equal(idx.shift(-3, freq="H"), exp)
