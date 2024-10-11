# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#38952 Case with not setting a full column
#  IntegerArray without NAs
arr = array([1, 2, 3, 4])
obj = frame_or_series(arr.to_numpy("i8"))

if frame_or_series is Series:
    values = obj.values
else:
    values = obj._mgr.arrays[0]

if frame_or_series is Series:
    obj.iloc[:2] = box(arr[2:])
else:
    obj.iloc[:2, 0] = box(arr[2:])

expected = frame_or_series(np.array([3, 4, 3, 4], dtype="i8"))
tm.assert_equal(obj, expected)

# Check that we are actually in-place
if frame_or_series is Series:
    assert obj.values is values
else:
    assert np.shares_memory(obj[0].values, values)
