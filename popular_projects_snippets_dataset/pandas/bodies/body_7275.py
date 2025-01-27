# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_insert.py

idx = TimedeltaIndex(["4day", "1day", "2day"], name="idx")

result = idx.insert(2, timedelta(days=5))
exp = TimedeltaIndex(["4day", "1day", "5day", "2day"], name="idx")
tm.assert_index_equal(result, exp)

# insertion of non-datetime should coerce to object index
result = idx.insert(1, "inserted")
expected = Index(
    [Timedelta("4day"), "inserted", Timedelta("1day"), Timedelta("2day")],
    name="idx",
)
assert not isinstance(result, TimedeltaIndex)
tm.assert_index_equal(result, expected)
assert result.name == expected.name

idx = timedelta_range("1day 00:00:01", periods=3, freq="s", name="idx")

# preserve freq
expected_0 = TimedeltaIndex(
    ["1day", "1day 00:00:01", "1day 00:00:02", "1day 00:00:03"],
    name="idx",
    freq="s",
)
expected_3 = TimedeltaIndex(
    ["1day 00:00:01", "1day 00:00:02", "1day 00:00:03", "1day 00:00:04"],
    name="idx",
    freq="s",
)

# reset freq to None
expected_1_nofreq = TimedeltaIndex(
    ["1day 00:00:01", "1day 00:00:01", "1day 00:00:02", "1day 00:00:03"],
    name="idx",
    freq=None,
)
expected_3_nofreq = TimedeltaIndex(
    ["1day 00:00:01", "1day 00:00:02", "1day 00:00:03", "1day 00:00:05"],
    name="idx",
    freq=None,
)

cases = [
    (0, Timedelta("1day"), expected_0),
    (-3, Timedelta("1day"), expected_0),
    (3, Timedelta("1day 00:00:04"), expected_3),
    (1, Timedelta("1day 00:00:01"), expected_1_nofreq),
    (3, Timedelta("1day 00:00:05"), expected_3_nofreq),
]

for n, d, expected in cases:
    result = idx.insert(n, d)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
