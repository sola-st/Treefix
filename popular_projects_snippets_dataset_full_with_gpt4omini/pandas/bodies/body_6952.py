# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
if isinstance(index, CategoricalIndex):
    exit()

first = index[:5]
second = index[:3]
intersect = first.intersection(second)
assert tm.equalContents(intersect, second)

if is_datetime64tz_dtype(index.dtype):
    # The second.values below will drop tz, so the rest of this test
    #  is not applicable.
    exit()

# GH#10149
cases = [second.to_numpy(), second.to_series(), second.to_list()]
for case in cases:
    result = first.intersection(case)
    assert tm.equalContents(result, second)

if isinstance(index, MultiIndex):
    msg = "other must be a MultiIndex or a list of tuples"
    with pytest.raises(TypeError, match=msg):
        first.intersection([1, 2, 3])
