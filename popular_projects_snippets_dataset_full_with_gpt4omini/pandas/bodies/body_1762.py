# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH #1259

rng = date_range("1/1/2000", "12/31/2000").as_unit(unit)
ts = Series(np.random.randn(len(rng)), index=rng)

result = ts.resample("M", kind="period").mean()
exp_index = period_range("Jan-2000", "Dec-2000", freq="M")
tm.assert_index_equal(result.index, exp_index)
