# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
rng = date_range("1/1/2000", "2/29/2000").as_unit(unit)
rng2 = rng.repeat(5).values
ts = Series(np.random.randn(len(rng2)), index=rng2)

result = ts.resample("M").mean()

expected = ts.groupby(lambda x: x.month).mean()
assert len(result) == 2
tm.assert_almost_equal(result[0], expected[1])
tm.assert_almost_equal(result[1], expected[2])
