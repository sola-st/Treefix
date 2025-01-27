# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py

exc = KeyError
if isinstance(
    index,
    (
        DatetimeIndex,
        TimedeltaIndex,
        PeriodIndex,
        RangeIndex,
        IntervalIndex,
        MultiIndex,
    ),
):
    # TODO: make these more consistent?
    exc = InvalidIndexError
with pytest.raises(exc, match="generator object"):
    # MultiIndex specifically checks for generator; others for scalar
    index.get_loc(x for x in range(5))
