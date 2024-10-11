# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_integrity.py
result = idx.memory_usage()
if len(idx):
    idx.get_loc(idx[0])
    result2 = idx.memory_usage()
    result3 = idx.memory_usage(deep=True)

    # RangeIndex, IntervalIndex
    # don't have engines
    if not isinstance(idx, (RangeIndex, IntervalIndex)):
        assert result2 > result

    if idx.inferred_type == "object":
        assert result3 > result2

else:

    # we report 0 for no-length
    assert result == 0
