# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
dtype = IntervalDtype(subtype, "right")

if subtype != "int64":
    msg = (
        r"Cannot convert interval\[(timedelta64|datetime64)\[ns.*\], .*\] "
        r"to interval\[uint64, .*\]"
    )
    with pytest.raises(TypeError, match=msg):
        index.astype(dtype)
    exit()

result = index.astype(dtype)
new_left = index.left.astype(subtype)
new_right = index.right.astype(subtype)

expected = IntervalIndex.from_arrays(new_left, new_right, closed=index.closed)
tm.assert_index_equal(result, expected)
