# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
idx = DatetimeIndex(["2000-01-04", "2000-01-01", "2000-01-02"], name="idx")

result = idx.insert(2, datetime(2000, 1, 5))
exp = DatetimeIndex(
    ["2000-01-04", "2000-01-01", "2000-01-05", "2000-01-02"], name="idx"
)
tm.assert_index_equal(result, exp)

# insertion of non-datetime should coerce to object index
result = idx.insert(1, "inserted")
expected = Index(
    [
        datetime(2000, 1, 4),
        "inserted",
        datetime(2000, 1, 1),
        datetime(2000, 1, 2),
    ],
    name="idx",
)
assert not isinstance(result, DatetimeIndex)
tm.assert_index_equal(result, expected)
assert result.name == expected.name

idx = date_range("1/1/2000", periods=3, freq="M", name="idx")

# preserve freq
expected_0 = DatetimeIndex(
    ["1999-12-31", "2000-01-31", "2000-02-29", "2000-03-31"],
    name="idx",
    freq="M",
)
expected_3 = DatetimeIndex(
    ["2000-01-31", "2000-02-29", "2000-03-31", "2000-04-30"],
    name="idx",
    freq="M",
)

# reset freq to None
expected_1_nofreq = DatetimeIndex(
    ["2000-01-31", "2000-01-31", "2000-02-29", "2000-03-31"],
    name="idx",
    freq=None,
)
expected_3_nofreq = DatetimeIndex(
    ["2000-01-31", "2000-02-29", "2000-03-31", "2000-01-02"],
    name="idx",
    freq=None,
)

cases = [
    (0, datetime(1999, 12, 31), expected_0),
    (-3, datetime(1999, 12, 31), expected_0),
    (3, datetime(2000, 4, 30), expected_3),
    (1, datetime(2000, 1, 31), expected_1_nofreq),
    (3, datetime(2000, 1, 2), expected_3_nofreq),
]

for n, d, expected in cases:
    result = idx.insert(n, d)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq

# reset freq to None
result = idx.insert(3, datetime(2000, 1, 2))
expected = DatetimeIndex(
    ["2000-01-31", "2000-02-29", "2000-03-31", "2000-01-02"],
    name="idx",
    freq=None,
)
tm.assert_index_equal(result, expected)
assert result.name == expected.name
assert result.freq is None

for tz in ["US/Pacific", "Asia/Singapore"]:
    idx = date_range("1/1/2000 09:00", periods=6, freq="H", tz=tz, name="idx")
    # preserve freq
    expected = date_range(
        "1/1/2000 09:00", periods=7, freq="H", tz=tz, name="idx"
    )
    for d in [
        Timestamp("2000-01-01 15:00", tz=tz),
        pytz.timezone(tz).localize(datetime(2000, 1, 1, 15)),
    ]:

        result = idx.insert(6, d)
        tm.assert_index_equal(result, expected)
        assert result.name == expected.name
        assert result.freq == expected.freq
        assert result.tz == expected.tz

    expected = DatetimeIndex(
        [
            "2000-01-01 09:00",
            "2000-01-01 10:00",
            "2000-01-01 11:00",
            "2000-01-01 12:00",
            "2000-01-01 13:00",
            "2000-01-01 14:00",
            "2000-01-01 10:00",
        ],
        name="idx",
        tz=tz,
        freq=None,
    )
    # reset freq to None
    for d in [
        Timestamp("2000-01-01 10:00", tz=tz),
        pytz.timezone(tz).localize(datetime(2000, 1, 1, 10)),
    ]:
        result = idx.insert(6, d)
        tm.assert_index_equal(result, expected)
        assert result.name == expected.name
        assert result.tz == expected.tz
        assert result.freq is None
