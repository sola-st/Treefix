# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_delete.py
idx = date_range(start="2000-01-01", periods=10, freq="D", name="idx")

# preserve freq
expected_0_2 = date_range(start="2000-01-04", periods=7, freq="D", name="idx")
expected_7_9 = date_range(start="2000-01-01", periods=7, freq="D", name="idx")

# reset freq to None
expected_3_5 = DatetimeIndex(
    [
        "2000-01-01",
        "2000-01-02",
        "2000-01-03",
        "2000-01-07",
        "2000-01-08",
        "2000-01-09",
        "2000-01-10",
    ],
    freq=None,
    name="idx",
)

cases = {
    (0, 1, 2): expected_0_2,
    (7, 8, 9): expected_7_9,
    (3, 4, 5): expected_3_5,
}
for n, expected in cases.items():
    result = idx.delete(n)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq

    result = idx.delete(slice(n[0], n[-1] + 1))
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq

for tz in [None, "Asia/Tokyo", "US/Pacific"]:
    ts = Series(
        1,
        index=date_range(
            "2000-01-01 09:00", periods=10, freq="H", name="idx", tz=tz
        ),
    )
    # preserve freq
    result = ts.drop(ts.index[:5]).index
    expected = date_range(
        "2000-01-01 14:00", periods=5, freq="H", name="idx", tz=tz
    )
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
    assert result.tz == expected.tz

    # reset freq to None
    result = ts.drop(ts.index[[1, 3, 5, 7, 9]]).index
    expected = DatetimeIndex(
        [
            "2000-01-01 09:00",
            "2000-01-01 11:00",
            "2000-01-01 13:00",
            "2000-01-01 15:00",
            "2000-01-01 17:00",
        ],
        freq=None,
        name="idx",
        tz=tz,
    )
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq
    assert result.tz == expected.tz
