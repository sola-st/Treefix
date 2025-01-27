# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
epoch = 1370745748
ser = Series([epoch + t for t in range(20)] + [null])
result = to_datetime(ser, unit="s")
expected = Series(
    [Timestamp("2013-06-09 02:42:28") + timedelta(seconds=t) for t in range(20)]
    + [NaT]
)
tm.assert_series_equal(result, expected)
