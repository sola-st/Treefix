# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 10834
# 8904
# exact kw
ser = Series(
    ["19MAY11", "foobar19MAY11", "19MAY11:00:00:00", "19MAY11 00:00:00Z"]
)
result = to_datetime(ser, format="%d%b%y", exact=False, cache=cache)
expected = to_datetime(
    ser.str.extract(r"(\d+\w+\d+)", expand=False), format="%d%b%y", cache=cache
)
tm.assert_series_equal(result, expected)
