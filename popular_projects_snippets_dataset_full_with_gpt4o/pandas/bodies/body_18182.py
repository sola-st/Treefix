# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH#22390
right = np.array([1, 2, 3], dtype="m8[s]")
right = box_cls(right)

expected = TimedeltaIndex(["10s", "40s", "90s"], dtype=right.dtype)

if isinstance(left, Series) or box_cls is Series:
    expected = Series(expected)
assert expected.dtype == right.dtype

result = left * right
tm.assert_equal(result, expected)

result = right * left
tm.assert_equal(result, expected)
