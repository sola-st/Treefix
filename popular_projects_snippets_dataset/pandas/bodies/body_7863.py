# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_shift.py
# GH#9903
idx = PeriodIndex([], name="xxx", freq="H")

msg = "`freq` argument is not supported for PeriodIndex.shift"
with pytest.raises(TypeError, match=msg):
    # period shift doesn't accept freq
    idx.shift(1, freq="H")

tm.assert_index_equal(idx.shift(0), idx)
tm.assert_index_equal(idx.shift(3), idx)

idx = PeriodIndex(
    ["2011-01-01 10:00", "2011-01-01 11:00", "2011-01-01 12:00"],
    name="xxx",
    freq="H",
)
tm.assert_index_equal(idx.shift(0), idx)
exp = PeriodIndex(
    ["2011-01-01 13:00", "2011-01-01 14:00", "2011-01-01 15:00"],
    name="xxx",
    freq="H",
)
tm.assert_index_equal(idx.shift(3), exp)
exp = PeriodIndex(
    ["2011-01-01 07:00", "2011-01-01 08:00", "2011-01-01 09:00"],
    name="xxx",
    freq="H",
)
tm.assert_index_equal(idx.shift(-3), exp)
