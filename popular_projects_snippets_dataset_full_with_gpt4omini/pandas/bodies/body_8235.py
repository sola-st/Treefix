# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
index = DatetimeIndex(
    [
        Timestamp("2007-01-01 10:11:12.123456Z"),
        Timestamp("2007-01-01 10:11:13.789123Z"),
    ]
)

with tm.assert_produces_warning(UserWarning):
    # warning that timezone info will be lost
    period = index.to_period(freq="L")
assert 2 == len(period)
assert period[0] == Period("2007-01-01 10:11:12.123Z", "L")
assert period[1] == Period("2007-01-01 10:11:13.789Z", "L")
