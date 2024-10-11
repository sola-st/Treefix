# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#19333
box = box_with_array
index = numeric_idx
expected = TimedeltaIndex([Timedelta(days=n) for n in range(len(index))])
if isinstance(scalar_td, np.timedelta64):
    dtype = scalar_td.dtype
    expected = expected.astype(dtype)
elif type(scalar_td) is timedelta:
    expected = expected.astype("m8[us]")

index = tm.box_expected(index, box)
expected = tm.box_expected(expected, box)

result = index * scalar_td
tm.assert_equal(result, expected)

commute = scalar_td * index
tm.assert_equal(commute, expected)
