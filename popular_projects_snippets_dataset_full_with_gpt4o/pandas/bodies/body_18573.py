# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_array_to_datetime.py
# see gh-19382, gh-19529
#
# Close enough to bounds that dropping nanos
# would result in an in-bounds datetime.
arr = np.array(["2262-04-11 23:47:16.854775808"], dtype=object)
msg = "^Out of bounds nanosecond timestamp: 2262-04-11 23:47:16, at position 0$"

with pytest.raises(tslib.OutOfBoundsDatetime, match=msg):
    tslib.array_to_datetime(arr)
