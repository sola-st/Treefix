# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
idx = PeriodIndex(["2011-01", NaT, Period("2011-01", freq="M")])
exp = PeriodIndex(["2011-01", "NaT", "2011-01"], freq="M")
tm.assert_index_equal(idx, exp)

idx = PeriodIndex(["NaT", NaT, Period("2011-01", freq="M")])
exp = PeriodIndex(["NaT", "NaT", "2011-01"], freq="M")
tm.assert_index_equal(idx, exp)

idx = PeriodIndex([Period("2011-01-01", freq="D"), NaT, "2012-01-01"])
exp = PeriodIndex(["2011-01-01", "NaT", "2012-01-01"], freq="D")
tm.assert_index_equal(idx, exp)
