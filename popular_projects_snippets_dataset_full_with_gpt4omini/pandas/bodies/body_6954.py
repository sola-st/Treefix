# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
first = index[2:]
second = index[:4]
if is_bool_dtype(index):
    # i think (TODO: be sure) there assumptions baked in about
    #  the index fixture that don't hold here?
    answer = set(first).difference(set(second))
elif isinstance(index, CategoricalIndex):
    answer = []
else:
    answer = index[4:]
result = first.difference(second, sort)
assert tm.equalContents(result, answer)

# GH#10149
cases = [second.to_numpy(), second.to_series(), second.to_list()]
for case in cases:
    result = first.difference(case, sort)
    assert tm.equalContents(result, answer)

if isinstance(index, MultiIndex):
    msg = "other must be a MultiIndex or a list of tuples"
    with pytest.raises(TypeError, match=msg):
        first.difference([1, 2, 3], sort)
