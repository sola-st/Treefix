# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
# GH#8083
tdi = pd.to_timedelta(range(5), unit="d")
trange = tdi._with_freq("infer") + pd.offsets.Hour(1)
result = trange.shift(3, freq="2D 1s")
expected = TimedeltaIndex(
    [
        "6 days 01:00:03",
        "7 days 01:00:03",
        "8 days 01:00:03",
        "9 days 01:00:03",
        "10 days 01:00:03",
    ],
    freq="D",
)
tm.assert_index_equal(result, expected)
