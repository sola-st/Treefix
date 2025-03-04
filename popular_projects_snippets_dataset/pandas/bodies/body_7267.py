# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_repeat.py
index = timedelta_range("1 days", periods=2, freq="D")
exp = TimedeltaIndex(["1 days", "1 days", "2 days", "2 days"])
for res in [index.repeat(2), np.repeat(index, 2)]:
    tm.assert_index_equal(res, exp)
    assert res.freq is None

index = TimedeltaIndex(["1 days", "NaT", "3 days"])
exp = TimedeltaIndex(
    [
        "1 days",
        "1 days",
        "1 days",
        "NaT",
        "NaT",
        "NaT",
        "3 days",
        "3 days",
        "3 days",
    ]
)
for res in [index.repeat(3), np.repeat(index, 3)]:
    tm.assert_index_equal(res, exp)
    assert res.freq is None
