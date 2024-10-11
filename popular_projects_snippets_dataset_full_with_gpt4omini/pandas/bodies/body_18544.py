# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_conversion.py
result = tz_convert_from_utc(arr, timezones.maybe_get_tz("Asia/Tokyo"))
tm.assert_numpy_array_equal(result, arr)
