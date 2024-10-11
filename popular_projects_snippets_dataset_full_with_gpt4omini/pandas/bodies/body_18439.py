# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#18808
dti = DatetimeIndex([NaT, Timestamp("19900315")])
ser = tm.box_expected(dti, box_with_array)

result = ser - NaT
expected = Series([NaT, NaT], dtype="timedelta64[ns]")
expected = tm.box_expected(expected, box_with_array)
tm.assert_equal(result, expected)

dti_tz = dti.tz_localize("Asia/Tokyo")
ser_tz = tm.box_expected(dti_tz, box_with_array)

result = ser_tz - NaT
expected = Series([NaT, NaT], dtype="timedelta64[ns]")
expected = tm.box_expected(expected, box_with_array)
tm.assert_equal(result, expected)
