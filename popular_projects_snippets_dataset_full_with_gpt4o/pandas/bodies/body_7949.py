# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
dti = date_range("2016-01-01", periods=3)
pi = dti.to_period("D")
pi2 = dti.to_period("H")

mask = np.array([0, 1, 0], dtype=bool)

msg = "must be DatetimeIndex or PeriodIndex"
with pytest.raises(TypeError, match=msg):
    pi.asof_locs(pd.Index(pi.asi8, dtype=np.int64), mask)

with pytest.raises(TypeError, match=msg):
    pi.asof_locs(pd.Index(pi.asi8, dtype=np.float64), mask)

with pytest.raises(TypeError, match=msg):
    # TimedeltaIndex
    pi.asof_locs(dti - dti, mask)

msg = "Input has different freq=H"
with pytest.raises(libperiod.IncompatibleFrequency, match=msg):
    pi.asof_locs(pi2, mask)
