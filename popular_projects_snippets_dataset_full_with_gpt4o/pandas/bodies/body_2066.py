# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 10178
ser = Series([2000, 2001, 2002])
expected = Series([Timestamp(x) for x in ser.apply(str)])

result = to_datetime(ser, format="%Y", cache=cache)
tm.assert_series_equal(result, expected)

ser = Series([200001, 200105, 200206])
expected = Series([Timestamp(x[:4] + "-" + x[4:]) for x in ser.apply(str)])

result = to_datetime(ser, format="%Y%m", cache=cache)
tm.assert_series_equal(result, expected)
