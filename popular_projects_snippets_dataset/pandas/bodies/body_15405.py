# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# GH#48665
ser = Series(["a", "b"])
ser[3] = nulls_fixture
expected = Series(["a", "b", nulls_fixture], index=[0, 1, 3])
tm.assert_series_equal(ser, expected)
assert ser[3] is nulls_fixture
