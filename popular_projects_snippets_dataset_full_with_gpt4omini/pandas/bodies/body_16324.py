# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#40111
vals = [
    "nan",
    Timestamp("1990-01-01"),
    "2015-03-14T16:15:14.123-08:00",
    "2019-03-04T21:56:32.620-07:00",
    None,
]
ser = Series(vals)
assert all(ser[i] is vals[i] for i in range(len(vals)))
