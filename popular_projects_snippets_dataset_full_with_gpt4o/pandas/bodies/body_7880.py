# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_astype.py
pi = PeriodIndex(["2011-01", "2011-02", "2011-03"], freq="M")

exp = DatetimeIndex(["2011-01-01", "2011-02-01", "2011-03-01"], tz="US/Eastern")
res = pi.astype("datetime64[ns, US/Eastern]")
tm.assert_index_equal(res, exp)
assert res.freq == exp.freq
