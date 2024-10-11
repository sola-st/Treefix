# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
idx = period_range("2007-01", periods=20, freq="M")

# values is an array of Period, thus can retrieve freq
tm.assert_index_equal(PeriodIndex(idx.values), idx)
tm.assert_index_equal(PeriodIndex(list(idx.values)), idx)

msg = "freq not specified and cannot be inferred"
with pytest.raises(ValueError, match=msg):
    PeriodIndex(idx.asi8)
with pytest.raises(ValueError, match=msg):
    PeriodIndex(list(idx.asi8))

msg = "'Period' object is not iterable"
with pytest.raises(TypeError, match=msg):
    PeriodIndex(data=Period("2007", freq="A"))

result = PeriodIndex(iter(idx))
tm.assert_index_equal(result, idx)

result = PeriodIndex(idx)
tm.assert_index_equal(result, idx)

result = PeriodIndex(idx, freq="M")
tm.assert_index_equal(result, idx)

result = PeriodIndex(idx, freq=offsets.MonthEnd())
tm.assert_index_equal(result, idx)
assert result.freq == "M"

result = PeriodIndex(idx, freq="2M")
tm.assert_index_equal(result, idx.asfreq("2M"))
assert result.freq == "2M"

result = PeriodIndex(idx, freq=offsets.MonthEnd(2))
tm.assert_index_equal(result, idx.asfreq("2M"))
assert result.freq == "2M"

result = PeriodIndex(idx, freq="D")
exp = idx.asfreq("D", "e")
tm.assert_index_equal(result, exp)
