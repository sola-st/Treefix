# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_is_full.py
index = PeriodIndex([2005, 2007, 2009], freq="A")
assert not index.is_full

index = PeriodIndex([2005, 2006, 2007], freq="A")
assert index.is_full

index = PeriodIndex([2005, 2005, 2007], freq="A")
assert not index.is_full

index = PeriodIndex([2005, 2005, 2006], freq="A")
assert index.is_full

index = PeriodIndex([2006, 2005, 2005], freq="A")
with pytest.raises(ValueError, match="Index is not monotonic"):
    index.is_full

assert index[:0].is_full
