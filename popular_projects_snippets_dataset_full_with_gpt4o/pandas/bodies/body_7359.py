# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
expected = TimedeltaIndex(
    [
        "1 days",
        "1 days 00:00:05",
        "2 days",
        "2 days 00:00:02",
        "0 days 00:00:03",
    ]
)
result = TimedeltaIndex(
    [
        "1 days",
        "1 days, 00:00:05",
        np.timedelta64(2, "D"),
        timedelta(days=2, seconds=2),
        pd.offsets.Second(3),
    ]
)
tm.assert_index_equal(result, expected)

expected = TimedeltaIndex(
    ["0 days 00:00:00", "0 days 00:00:01", "0 days 00:00:02"]
)
tm.assert_index_equal(TimedeltaIndex(range(3), unit="s"), expected)
expected = TimedeltaIndex(
    ["0 days 00:00:00", "0 days 00:00:05", "0 days 00:00:09"]
)
tm.assert_index_equal(TimedeltaIndex([0, 5, 9], unit="s"), expected)
expected = TimedeltaIndex(
    ["0 days 00:00:00.400", "0 days 00:00:00.450", "0 days 00:00:01.200"]
)
tm.assert_index_equal(TimedeltaIndex([400, 450, 1200], unit="ms"), expected)
