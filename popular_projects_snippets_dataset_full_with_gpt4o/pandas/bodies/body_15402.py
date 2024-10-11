# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# set item that's not contained
ser = string_series.copy()
assert "foobar" not in ser.index
ser["foobar"] = 1

app = Series([1], index=["foobar"], name="series")
expected = concat([string_series, app])
tm.assert_series_equal(ser, expected)
