# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#19529
# GH#19382 close enough to bounds that dropping nanos would result
# in an in-bounds datetime
arr = np.array(["2262-04-11 23:47:16.854775808"], dtype=object)

msg = "^Out of bounds nanosecond timestamp: .*, at position 0"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    with tm.assert_produces_warning(
        UserWarning, match="Could not infer format"
    ):
        to_datetime(arr)
