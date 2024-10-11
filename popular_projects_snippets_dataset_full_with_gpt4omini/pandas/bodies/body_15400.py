# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#22717 inserting a Timedelta should _not_ cast to int64
expected = Series(["x", td], index=[0, "td"], dtype=object)

ser = Series(["x"])
ser["td"] = td
tm.assert_series_equal(ser, expected)
assert isinstance(ser["td"], Timedelta)

ser = Series(["x"])
ser.loc["td"] = Timedelta("9 days")
tm.assert_series_equal(ser, expected)
assert isinstance(ser["td"], Timedelta)
