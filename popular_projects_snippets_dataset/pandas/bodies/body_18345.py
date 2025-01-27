# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#18808, GH#23320 special handling for timedelta64("NaT")
box = box_with_array
tdi = TimedeltaIndex([NaT, Timedelta("1s")])
expected = TimedeltaIndex(["NaT"] * 2)

obj = tm.box_expected(tdi, box)
expected = tm.box_expected(expected, box)

result = obj + tdnat
tm.assert_equal(result, expected)
result = tdnat + obj
tm.assert_equal(result, expected)
result = obj - tdnat
tm.assert_equal(result, expected)
result = tdnat - obj
tm.assert_equal(result, expected)
