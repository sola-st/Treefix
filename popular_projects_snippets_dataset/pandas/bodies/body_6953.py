# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
first = index[3:]
second = index[:5]
everything = index

union = first.union(second)
assert tm.equalContents(union, everything)

if is_datetime64tz_dtype(index.dtype):
    # The second.values below will drop tz, so the rest of this test
    #  is not applicable.
    exit()

# GH#10149
cases = [second.to_numpy(), second.to_series(), second.to_list()]
for case in cases:
    result = first.union(case)
    assert tm.equalContents(result, everything)

if isinstance(index, MultiIndex):
    msg = "other must be a MultiIndex or a list of tuples"
    with pytest.raises(TypeError, match=msg):
        first.union([1, 2, 3])
