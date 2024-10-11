# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 6428
ser = Series(["10/18/2006", "10/18/2008", " "])
msg = r'^time data " " doesn\'t match format "%m/%d/%Y", at position 2$'
with pytest.raises(ValueError, match=msg):
    to_datetime(ser, errors="raise", cache=cache)
result_coerce = to_datetime(ser, errors="coerce", cache=cache)
expected_coerce = Series([datetime(2006, 10, 18), datetime(2008, 10, 18), NaT])
tm.assert_series_equal(result_coerce, expected_coerce)
result_ignore = to_datetime(ser, errors="ignore", cache=cache)
tm.assert_series_equal(result_ignore, ser)
