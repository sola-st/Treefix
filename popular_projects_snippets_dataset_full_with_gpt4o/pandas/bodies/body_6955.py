# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
if isinstance(index, CategoricalIndex):
    exit()
if len(index) < 2:
    exit()
if index[0] in index[1:] or index[-1] in index[:-1]:
    # index fixture has e.g. an index of bools that does not satisfy this,
    #  another with [0, 0, 1, 1, 2, 2]
    exit()

first = index[1:]
second = index[:-1]
answer = index[[0, -1]]
result = first.symmetric_difference(second)
assert tm.equalContents(result, answer)

# GH#10149
cases = [second.to_numpy(), second.to_series(), second.to_list()]
for case in cases:
    result = first.symmetric_difference(case)
    assert tm.equalContents(result, answer)

if isinstance(index, MultiIndex):
    msg = "other must be a MultiIndex or a list of tuples"
    with pytest.raises(TypeError, match=msg):
        first.symmetric_difference([1, 2, 3])
