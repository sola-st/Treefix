# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_repeat.py
tz = tz_naive_fixture
reps = 2
msg = "the 'axis' parameter is not supported"

rng = date_range(start="2016-01-01", periods=2, freq="30Min", tz=tz)

expected_rng = DatetimeIndex(
    [
        Timestamp("2016-01-01 00:00:00", tz=tz),
        Timestamp("2016-01-01 00:00:00", tz=tz),
        Timestamp("2016-01-01 00:30:00", tz=tz),
        Timestamp("2016-01-01 00:30:00", tz=tz),
    ]
)

res = rng.repeat(reps)
tm.assert_index_equal(res, expected_rng)
assert res.freq is None

tm.assert_index_equal(np.repeat(rng, reps), expected_rng)
with pytest.raises(ValueError, match=msg):
    np.repeat(rng, reps, axis=1)
