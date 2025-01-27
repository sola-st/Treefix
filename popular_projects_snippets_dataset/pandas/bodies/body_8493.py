# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# GH4226
st = Timestamp("2013-07-01 00:00:00", tz="America/Los_Angeles")
et = Timestamp("2013-07-02 00:00:00", tz="America/Los_Angeles")
dr = date_range(st, et, freq="H", name="timebucket")
assert dr[1:].name == dr.name
