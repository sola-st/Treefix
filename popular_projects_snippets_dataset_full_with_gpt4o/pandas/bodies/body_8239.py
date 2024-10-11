# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
idx = DatetimeIndex(["2000-01-01", "2000-01-02", "2000-01-04"])
msg = "You must pass a freq argument as current index has none."
with pytest.raises(ValueError, match=msg):
    idx.to_period()

idx = DatetimeIndex(["2000-01-01", "2000-01-02", "2000-01-03"], freq="infer")
assert idx.freqstr == "D"
expected = PeriodIndex(["2000-01-01", "2000-01-02", "2000-01-03"], freq="D")
tm.assert_index_equal(idx.to_period(), expected)

# GH#7606
idx = DatetimeIndex(["2000-01-01", "2000-01-02", "2000-01-03"])
assert idx.freqstr is None
tm.assert_index_equal(idx.to_period(), expected)
