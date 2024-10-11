# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
ser = Series([19801222, 19801222] + [19810105] * 5)
expected = Series([Timestamp(x) for x in ser.apply(str)])

result = to_datetime(ser, format="%Y%m%d", cache=cache)
tm.assert_series_equal(result, expected)

result = to_datetime(ser.apply(str), format="%Y%m%d", cache=cache)
tm.assert_series_equal(result, expected)
