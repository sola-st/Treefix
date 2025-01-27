# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
original = string_series.copy()
numSlice = string_series[10:20]
numSliceEnd = string_series[-10:]
objSlice = object_series[10:20]

assert string_series.index[9] not in numSlice.index
assert object_series.index[9] not in objSlice.index

assert len(numSlice) == len(numSlice.index)
assert string_series[numSlice.index[0]] == numSlice[numSlice.index[0]]

assert numSlice.index[1] == string_series.index[11]
assert tm.equalContents(numSliceEnd, np.array(string_series)[-10:])

# Test return view.
sl = string_series[10:20]
sl[:] = 0

if using_copy_on_write:
    # Doesn't modify parent (CoW)
    tm.assert_series_equal(string_series, original)
else:
    assert (string_series[10:20] == 0).all()
