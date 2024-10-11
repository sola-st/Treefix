# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#4521
# divide/multiply by integers
tdser = Series(["59 Days", "59 Days", "NaT"], dtype="m8[ns]")
expected = Series(["-59 Days", "-59 Days", "NaT"], dtype="timedelta64[ns]")

tdser = tm.box_expected(tdser, box_with_array)
expected = tm.box_expected(expected, box_with_array)

result = tdser * (-one)
tm.assert_equal(result, expected)
result = (-one) * tdser
tm.assert_equal(result, expected)

expected = Series(["118 Days", "118 Days", "NaT"], dtype="timedelta64[ns]")
expected = tm.box_expected(expected, box_with_array)

result = tdser * (2 * one)
tm.assert_equal(result, expected)
result = (2 * one) * tdser
tm.assert_equal(result, expected)
