# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#4521
# divide/multiply by integers

tdser = Series(["59 Days", "59 Days", "NaT"], dtype="m8[ns]")
vector = vector.astype(any_real_numpy_dtype)

expected = Series(["1180 Days", "1770 Days", "NaT"], dtype="timedelta64[ns]")

tdser = tm.box_expected(tdser, box_with_array)
xbox = get_upcast_box(tdser, vector)

expected = tm.box_expected(expected, xbox)

result = tdser * vector
tm.assert_equal(result, expected)

result = vector * tdser
tm.assert_equal(result, expected)
