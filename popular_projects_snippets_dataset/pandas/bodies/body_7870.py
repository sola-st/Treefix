# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_asfreq.py
pi = PeriodIndex(["2001-01", "2001-02", "NaT", "2001-03"], freq="2M")

result = pi.asfreq(freq)
exp = PeriodIndex(["2001-02-28", "2001-03-31", "NaT", "2001-04-30"], freq=freq)
tm.assert_index_equal(result, exp)
assert result.freq == exp.freq

result = pi.asfreq(freq, how="S")
exp = PeriodIndex(["2001-01-01", "2001-02-01", "NaT", "2001-03-01"], freq=freq)
tm.assert_index_equal(result, exp)
assert result.freq == exp.freq
