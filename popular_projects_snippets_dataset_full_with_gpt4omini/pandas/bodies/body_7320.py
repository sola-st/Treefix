# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_formats.py
idx1 = TimedeltaIndex([], freq="D")
idx2 = TimedeltaIndex(["1 days"], freq="D")
idx3 = TimedeltaIndex(["1 days", "2 days"], freq="D")
idx4 = TimedeltaIndex(["1 days", "2 days", "3 days"], freq="D")
idx5 = TimedeltaIndex(["1 days 00:00:01", "2 days", "3 days"])

exp1 = "TimedeltaIndex([], dtype='timedelta64[ns]', freq='D')"

exp2 = "TimedeltaIndex(['1 days'], dtype='timedelta64[ns]', freq='D')"

exp3 = "TimedeltaIndex(['1 days', '2 days'], dtype='timedelta64[ns]', freq='D')"

exp4 = (
    "TimedeltaIndex(['1 days', '2 days', '3 days'], "
    "dtype='timedelta64[ns]', freq='D')"
)

exp5 = (
    "TimedeltaIndex(['1 days 00:00:01', '2 days 00:00:00', "
    "'3 days 00:00:00'], dtype='timedelta64[ns]', freq=None)"
)

with pd.option_context("display.width", 300):
    for idx, expected in zip(
        [idx1, idx2, idx3, idx4, idx5], [exp1, exp2, exp3, exp4, exp5]
    ):
        result = getattr(idx, method)()
        assert result == expected
