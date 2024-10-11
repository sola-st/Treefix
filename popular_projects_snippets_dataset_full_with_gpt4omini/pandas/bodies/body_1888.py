# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
ts = simple_period_range_series("1/1/1990", "12/31/1991", freq=f"A-{month}")

result = getattr(ts.resample(targ, convention=conv), meth)()
expected = result.to_timestamp(targ, how=conv)
expected = expected.asfreq(targ, meth).to_period()
tm.assert_series_equal(result, expected)
