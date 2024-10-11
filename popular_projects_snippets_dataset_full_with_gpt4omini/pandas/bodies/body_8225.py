# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_repeat.py
tz = tz_naive_fixture
rng = date_range("1/1/2000", "1/1/2001")

result = rng.repeat(5)
assert result.freq is None
assert len(result) == 5 * len(rng)

index = date_range("2001-01-01", periods=2, freq="D", tz=tz)
exp = DatetimeIndex(
    ["2001-01-01", "2001-01-01", "2001-01-02", "2001-01-02"], tz=tz
)
for res in [index.repeat(2), np.repeat(index, 2)]:
    tm.assert_index_equal(res, exp)
    assert res.freq is None

index = date_range("2001-01-01", periods=2, freq="2D", tz=tz)
exp = DatetimeIndex(
    ["2001-01-01", "2001-01-01", "2001-01-03", "2001-01-03"], tz=tz
)
for res in [index.repeat(2), np.repeat(index, 2)]:
    tm.assert_index_equal(res, exp)
    assert res.freq is None

index = DatetimeIndex(["2001-01-01", "NaT", "2003-01-01"], tz=tz)
exp = DatetimeIndex(
    [
        "2001-01-01",
        "2001-01-01",
        "2001-01-01",
        "NaT",
        "NaT",
        "NaT",
        "2003-01-01",
        "2003-01-01",
        "2003-01-01",
    ],
    tz=tz,
)
for res in [index.repeat(3), np.repeat(index, 3)]:
    tm.assert_index_equal(res, exp)
    assert res.freq is None
