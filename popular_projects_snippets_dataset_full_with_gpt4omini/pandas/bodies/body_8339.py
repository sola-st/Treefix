# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
# GH 21262
tz = tz_naive_fixture
rng = date_range(start="2016-01-01", periods=5, freq="2Min", tz=tz)

expected_rng = DatetimeIndex(
    [
        Timestamp("2016-01-01 00:00:00", tz=tz),
        Timestamp("2016-01-01 00:02:00", tz=tz),
        Timestamp("2016-01-01 00:04:00", tz=tz),
        Timestamp("2016-01-01 00:06:00", tz=tz),
        Timestamp("2016-01-01 00:08:00", tz=tz),
    ]
)

tm.assert_index_equal(rng.round(freq="2T"), expected_rng)
