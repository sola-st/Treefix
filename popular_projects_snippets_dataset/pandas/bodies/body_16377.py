# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
values = [188.5, 328.25]
tzinfo = tzoffset(None, 7200)
index = [
    datetime(2012, 5, 11, 11, tzinfo=tzinfo),
    datetime(2012, 5, 11, 12, tzinfo=tzinfo),
]
series = Series(data=values, index=index)

assert series.index.tz == tzinfo

# it works! GH#2443
repr(series.index[0])
