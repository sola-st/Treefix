# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
# GH#8083
tdi = pd.to_timedelta(range(5), unit="d")
trange = tdi._with_freq("infer") + pd.offsets.Hour(1)
result = trange.shift(1)
expected = TimedeltaIndex(
    [
        "1 days 01:00:00",
        "2 days 01:00:00",
        "3 days 01:00:00",
        "4 days 01:00:00",
        "5 days 01:00:00",
    ],
    freq="D",
)
tm.assert_index_equal(result, expected)
