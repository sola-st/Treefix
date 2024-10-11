# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
result = to_datetime(["March 1, 2018 12:00:00+0400"] * 2)
expected = DatetimeIndex(
    [datetime(2018, 3, 1, 12, tzinfo=timezone(timedelta(minutes=240)))] * 2
)
tm.assert_index_equal(result, expected)
