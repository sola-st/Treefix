# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 25978

vals = [
    "nan",
    Timestamp("1990-01-01"),
    "2015-03-14T16:15:14.123-08:00",
    "2019-03-04T21:56:32.620-07:00",
    None,
    "today",
    "now",
]
ser = Series(vals)
assert all(ser[i] is vals[i] for i in range(len(vals)))  # GH#40111

now = Timestamp("now")
today = Timestamp("today")
mixed = to_datetime(ser)
expected = Series(
    [
        "NaT",
        Timestamp("1990-01-01"),
        Timestamp("2015-03-14T16:15:14.123-08:00").to_pydatetime(),
        Timestamp("2019-03-04T21:56:32.620-07:00").to_pydatetime(),
        None,
    ],
    dtype=object,
)
tm.assert_series_equal(mixed[:-2], expected)
# we'll check mixed[-1] and mixed[-2] match now and today to within
# call-timing tolerances
assert (now - mixed.iloc[-1]).total_seconds() <= 0.1
assert (today - mixed.iloc[-2]).total_seconds() <= 0.1

with pytest.raises(ValueError, match="Tz-aware datetime.datetime"):
    to_datetime(mixed)
