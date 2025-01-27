# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
base_str = "2014-07-01 09:00"
base_dt = datetime(2014, 7, 1, 9)
base_expected = 1_404_205_200_000_000_000

# confirm base representation is correct
assert calendar.timegm(base_dt.timetuple()) * 1_000_000_000 == base_expected

tests = [
    (base_str, base_dt, base_expected),
    (
        "2014-07-01 10:00",
        datetime(2014, 7, 1, 10),
        base_expected + 3600 * 1_000_000_000,
    ),
    (
        "2014-07-01 09:00:00.000008000",
        datetime(2014, 7, 1, 9, 0, 0, 8),
        base_expected + 8000,
    ),
    (
        "2014-07-01 09:00:00.000000005",
        Timestamp("2014-07-01 09:00:00.000000005"),
        base_expected + 5,
    ),
]

timezones = [
    (None, 0),
    ("UTC", 0),
    (pytz.utc, 0),
    ("Asia/Tokyo", 9),
    ("US/Eastern", -4),
    ("dateutil/US/Pacific", -7),
    (pytz.FixedOffset(-180), -3),
    (dateutil.tz.tzoffset(None, 18000), 5),
]

for date_str, date_obj, expected in tests:
    for result in [Timestamp(date_str), Timestamp(date_obj)]:
        result = result.as_unit("ns")  # test originally written before non-nano
        # only with timestring
        assert result.as_unit("ns").value == expected

        # re-creation shouldn't affect to internal value
        result = Timestamp(result)
        assert result.as_unit("ns").value == expected

    # with timezone
    for tz, offset in timezones:
        for result in [Timestamp(date_str, tz=tz), Timestamp(date_obj, tz=tz)]:
            result = result.as_unit(
                "ns"
            )  # test originally written before non-nano
            expected_tz = expected - offset * 3600 * 1_000_000_000
            assert result.as_unit("ns").value == expected_tz

            # should preserve tz
            result = Timestamp(result)
            assert result.as_unit("ns").value == expected_tz

            # should convert to UTC
            if tz is not None:
                result = Timestamp(result).tz_convert("UTC")
            else:
                result = Timestamp(result, tz="UTC")
            expected_utc = expected - offset * 3600 * 1_000_000_000
            assert result.as_unit("ns").value == expected_utc
