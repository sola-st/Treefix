# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#13071
idx = PeriodIndex(
    ["2011-01", "2011-02", "NaT", "2011-04"], freq="M", name="idx"
)
exp = TimedeltaIndex([pd.NaT] * 4, name="idx")
tm.assert_index_equal(pd.NaT - idx, exp)
tm.assert_index_equal(idx - pd.NaT, exp)
