# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
rs = dtc.convert(["2012-1-1"], None, None)[0]
xp = dates.date2num(datetime(2012, 1, 1))
assert rs == xp

rs = dtc.convert("2012-1-1", None, None)
assert rs == xp

rs = dtc.convert(date(2012, 1, 1), None, None)
assert rs == xp

rs = dtc.convert("2012-1-1", None, None)
assert rs == xp

rs = dtc.convert(Timestamp("2012-1-1"), None, None)
assert rs == xp

# also testing datetime64 dtype (GH8614)
rs = dtc.convert("2012-01-01", None, None)
assert rs == xp

rs = dtc.convert("2012-01-01 00:00:00+0000", None, None)
assert rs == xp

rs = dtc.convert(
    np.array(["2012-01-01 00:00:00+0000", "2012-01-02 00:00:00+0000"]),
    None,
    None,
)
assert rs[0] == xp

# we have a tz-aware date (constructed to that when we turn to utc it
# is the same as our sample)
ts = Timestamp("2012-01-01").tz_localize("UTC").tz_convert("US/Eastern")
rs = dtc.convert(ts, None, None)
assert rs == xp

rs = dtc.convert(ts.to_pydatetime(), None, None)
assert rs == xp

rs = dtc.convert(Index([ts - Day(1), ts]), None, None)
assert rs[1] == xp

rs = dtc.convert(Index([ts - Day(1), ts]).to_pydatetime(), None, None)
assert rs[1] == xp
