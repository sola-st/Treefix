# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#13071
idx = PeriodIndex(
    ["2011-01", "NaT", "2011-03", "2011-04"], freq="M", name="idx"
)

result = idx - Period("2012-01", freq="M")
off = idx.freq
exp = pd.Index([-12 * off, pd.NaT, -10 * off, -9 * off], name="idx")
tm.assert_index_equal(result, exp)

result = Period("2012-01", freq="M") - idx
exp = pd.Index([12 * off, pd.NaT, 10 * off, 9 * off], name="idx")
tm.assert_index_equal(result, exp)

exp = TimedeltaIndex([np.nan, np.nan, np.nan, np.nan], name="idx")
tm.assert_index_equal(idx - Period("NaT", freq="M"), exp)
tm.assert_index_equal(Period("NaT", freq="M") - idx, exp)
