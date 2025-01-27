# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
indexer = [4, 3, 0, 2]
if len(index) < 5:
    # not enough elements; ignore
    exit()

result = index.take(indexer)
expected = index[indexer]
assert result.equals(expected)

if not isinstance(index, (DatetimeIndex, PeriodIndex, TimedeltaIndex)):
    # GH 10791
    msg = r"'(.*Index)' object has no attribute 'freq'"
    with pytest.raises(AttributeError, match=msg):
        index.freq
