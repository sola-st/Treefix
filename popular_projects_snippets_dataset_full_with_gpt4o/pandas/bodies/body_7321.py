# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_formats.py
idx1 = TimedeltaIndex([], freq="D")
idx2 = TimedeltaIndex(["1 days"], freq="D")
idx3 = TimedeltaIndex(["1 days", "2 days"], freq="D")
idx4 = TimedeltaIndex(["1 days", "2 days", "3 days"], freq="D")
idx5 = TimedeltaIndex(["1 days 00:00:01", "2 days", "3 days"])

exp1 = """Series([], dtype: timedelta64[ns])"""

exp2 = "0   1 days\ndtype: timedelta64[ns]"

exp3 = "0   1 days\n1   2 days\ndtype: timedelta64[ns]"

exp4 = "0   1 days\n1   2 days\n2   3 days\ndtype: timedelta64[ns]"

exp5 = (
    "0   1 days 00:00:01\n"
    "1   2 days 00:00:00\n"
    "2   3 days 00:00:00\n"
    "dtype: timedelta64[ns]"
)

with pd.option_context("display.width", 300):
    for idx, expected in zip(
        [idx1, idx2, idx3, idx4, idx5], [exp1, exp2, exp3, exp4, exp5]
    ):
        result = repr(Series(idx))
        assert result == expected
