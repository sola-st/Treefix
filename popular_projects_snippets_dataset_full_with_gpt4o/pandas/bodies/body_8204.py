# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# see gh-18031
tz = "Europe/Brussels"
freq = "15min"

start = Timestamp("201710290100", tz=tz)
end = Timestamp("201710290300", tz=tz)
index = date_range(start=start, end=end, freq=freq)

expected = DatetimeIndex(
    [
        "201710290115",
        "201710290130",
        "201710290145",
        "201710290200",
        "201710290215",
        "201710290230",
        "201710290245",
        "201710290200",
        "201710290215",
        "201710290230",
        "201710290245",
        "201710290300",
    ],
    tz=tz,
    freq=freq,
    ambiguous=[
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
    ],
)
result = index.drop(index[0])
tm.assert_index_equal(result, expected)
