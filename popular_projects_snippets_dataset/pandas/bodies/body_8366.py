# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_delete.py
idx = date_range(start="2000-01-01", periods=5, freq="M", name="idx")

# preserve freq
expected_0 = date_range(start="2000-02-01", periods=4, freq="M", name="idx")
expected_4 = date_range(start="2000-01-01", periods=4, freq="M", name="idx")

# reset freq to None
expected_1 = DatetimeIndex(
    ["2000-01-31", "2000-03-31", "2000-04-30", "2000-05-31"],
    freq=None,
    name="idx",
)

cases = {
    0: expected_0,
    -5: expected_0,
    -1: expected_4,
    4: expected_4,
    1: expected_1,
}
for n, expected in cases.items():
    result = idx.delete(n)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freq == expected.freq

with pytest.raises((IndexError, ValueError), match="out of bounds"):
    # either depending on numpy version
    idx.delete(5)

for tz in [None, "Asia/Tokyo", "US/Pacific"]:
    idx = date_range(
        start="2000-01-01 09:00", periods=10, freq="H", name="idx", tz=tz
    )

    expected = date_range(
        start="2000-01-01 10:00", periods=9, freq="H", name="idx", tz=tz
    )
    result = idx.delete(0)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freqstr == "H"
    assert result.tz == expected.tz

    expected = date_range(
        start="2000-01-01 09:00", periods=9, freq="H", name="idx", tz=tz
    )
    result = idx.delete(-1)
    tm.assert_index_equal(result, expected)
    assert result.name == expected.name
    assert result.freqstr == "H"
    assert result.tz == expected.tz
