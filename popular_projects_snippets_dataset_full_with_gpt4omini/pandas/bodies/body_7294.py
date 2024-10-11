# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_timedelta_range.py
# GH 20976
result = timedelta_range(start="0 days", end="4 days", periods=periods)
expected = timedelta_range(start="0 days", end="4 days", freq=freq)
tm.assert_index_equal(result, expected)
