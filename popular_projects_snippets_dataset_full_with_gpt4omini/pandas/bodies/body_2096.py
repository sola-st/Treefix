# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/50036
result = to_datetime([arg, np.datetime64("2020-01-01")], format=format)
expected = DatetimeIndex(["2001-01-01", "2020-01-01"])
tm.assert_index_equal(result, expected)
