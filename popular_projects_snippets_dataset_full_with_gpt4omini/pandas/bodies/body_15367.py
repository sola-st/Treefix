# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#23451
ser = Series([1, 2, 3], index=["Date", "b", "other"])
ser["Date"] = date.today()
assert ser.Date == date.today()
assert ser["Date"] == date.today()
