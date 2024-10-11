# Extracted from ./data/repos/pandas/pandas/tests/resample/test_datetime_index.py
# GH #1077
rng = date_range("1/1/2000", "2/29/2000").as_unit(unit)
rng2 = rng.repeat(2).values
ts = Series(np.random.randn(len(rng2)), index=rng2)

msg = "cannot reindex on an axis with duplicate labels"
with pytest.raises(ValueError, match=msg):
    ts.asfreq("B")
