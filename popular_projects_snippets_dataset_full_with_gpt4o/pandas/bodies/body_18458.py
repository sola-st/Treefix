# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#25317
left = Series([Timestamp("1969-12-31")])
right = Series([NaT])

left = tm.box_expected(left, box_with_array)
right = tm.box_expected(right, box_with_array)

expected = TimedeltaIndex([NaT])
expected = tm.box_expected(expected, box_with_array)

result = left - right
tm.assert_equal(result, expected)
