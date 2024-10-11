# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/50255
ts_strings = [string_arg, outofbounds]
result = to_datetime(ts_strings, errors="coerce", format=format)
expected = DatetimeIndex([datetime(2018, 3, 1), NaT])
tm.assert_index_equal(result, expected)
