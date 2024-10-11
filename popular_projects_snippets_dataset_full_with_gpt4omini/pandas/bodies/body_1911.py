# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
rng = PeriodIndex([2000, 2005, 2005, 2007, 2007], freq="A")
s = Series(np.random.randn(5), index=rng)
msg = "Reindexing only valid with uniquely valued Index objects"
with pytest.raises(InvalidIndexError, match=msg):
    s.resample("A").ffill()
