# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# see GH#13509

# unique Index
ser = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.1, 0.2], name="foo")
result = ser[0.0]
assert result == (1, 1)

# non-unique Index
expected = Series([(1, 1), (2, 2)], index=[0.0, 0.0], name="foo")
ser = Series([(1, 1), (2, 2), (3, 3)], index=[0.0, 0.0, 0.2], name="foo")

result = ser[0.0]
tm.assert_series_equal(result, expected)
