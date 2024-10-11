# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
if isinstance(index, IntervalIndex):
    # IntervalIndex tested separately, the index.equals(index.astype(object))
    #  fails for IntervalIndex
    exit()

is_ea_idx = type(index) is Index and not isinstance(index.dtype, np.dtype)

assert index.equals(index)
assert index.equals(index.copy())
if not is_ea_idx:
    # doesn't hold for e.g. IntegerDtype
    assert index.equals(index.astype(object))

assert not index.equals(list(index))
assert not index.equals(np.array(index))

# Cannot pass in non-int64 dtype to RangeIndex
if not isinstance(index, RangeIndex) and not is_ea_idx:
    same_values = Index(index, dtype=object)
    assert index.equals(same_values)
    assert same_values.equals(index)

if index.nlevels == 1:
    # do not test MultiIndex
    assert not index.equals(Series(index))
