# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
box = box_with_array

index = numeric_idx[1:3]

expected = TimedeltaIndex(["3 Days", "36 Hours"])
if isinstance(three_days, np.timedelta64):
    dtype = three_days.dtype
    if dtype < np.dtype("m8[s]"):
        # i.e. resolution is lower -> use lowest supported resolution
        dtype = np.dtype("m8[s]")
    expected = expected.astype(dtype)
elif type(three_days) is timedelta:
    expected = expected.astype("m8[us]")

index = tm.box_expected(index, box)
expected = tm.box_expected(expected, box)

result = three_days / index
tm.assert_equal(result, expected)

msg = "cannot use operands with types dtype"
with pytest.raises(TypeError, match=msg):
    index / three_days
