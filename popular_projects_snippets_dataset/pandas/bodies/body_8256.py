# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
# see GH#7299
idx = date_range("1/1/2000", periods=3, freq="D", tz="Asia/Tokyo", name="idx")

# mismatched tz-awareness
item = Timestamp("2000-01-04")
result = idx.insert(3, item)
expected = Index(
    list(idx[:3]) + [item] + list(idx[3:]), dtype=object, name="idx"
)
tm.assert_index_equal(result, expected)

# mismatched tz-awareness
item = datetime(2000, 1, 4)
result = idx.insert(3, item)
expected = Index(
    list(idx[:3]) + [item] + list(idx[3:]), dtype=object, name="idx"
)
tm.assert_index_equal(result, expected)
