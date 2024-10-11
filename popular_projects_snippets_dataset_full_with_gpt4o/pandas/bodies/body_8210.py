# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#1345

# dates around a dst transition
rng = date_range("2/13/2010", "5/6/2010", tz=tzstr)

objs = rng.astype(object)
for i, x in enumerate(objs):
    exval = rng[i]
    assert x == exval
    assert x.tzinfo == exval.tzinfo

objs = rng.astype(object)
for i, x in enumerate(objs):
    exval = rng[i]
    assert x == exval
    assert x.tzinfo == exval.tzinfo
