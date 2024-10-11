# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# https://github.com/pandas-dev/pandas/issues/50108
d1 = date(2020, 1, 2)
res = to_datetime(["2020-01-01", d1], format=format)
expected = DatetimeIndex(["2020-01-01", "2020-01-02"])
tm.assert_index_equal(res, expected)
