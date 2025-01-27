# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH 21697
fmt = "%Y-%m-%d %H:%M:%S %z"
arg = Index(["2010-01-01 12:00:00 Z"], name="foo")
result = to_datetime(arg, format=fmt)
expected = DatetimeIndex(["2010-01-01 12:00:00"], tz="UTC", name="foo")
tm.assert_index_equal(result, expected)
