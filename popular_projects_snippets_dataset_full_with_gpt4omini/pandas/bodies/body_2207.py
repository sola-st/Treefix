# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
ser = Series(date_range("20000101", periods=50, freq="H"))

s_as_dt_strings = ser.apply(lambda x: x.strftime(test_format))

with_format = to_datetime(s_as_dt_strings, format=test_format, cache=cache)
without_format = to_datetime(s_as_dt_strings, cache=cache)

# Whether the format is explicitly passed, or
# it is inferred, the results should all be the same
tm.assert_series_equal(with_format, without_format)
