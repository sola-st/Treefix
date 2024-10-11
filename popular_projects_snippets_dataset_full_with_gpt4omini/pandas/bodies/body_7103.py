# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
index._engine.clear_mapping()
result = index.memory_usage()
if index.empty:
    # we report 0 for no-length
    assert result == 0
    exit()

# non-zero length
index.get_loc(index[0])
result2 = index.memory_usage()
result3 = index.memory_usage(deep=True)

# RangeIndex, IntervalIndex
# don't have engines
# Index[EA] has engine but it does not have a Hashtable .mapping
if not isinstance(index, (RangeIndex, IntervalIndex)) and not (
    type(index) is Index and not isinstance(index.dtype, np.dtype)
):
    assert result2 > result

if index.inferred_type == "object":
    assert result3 > result2
