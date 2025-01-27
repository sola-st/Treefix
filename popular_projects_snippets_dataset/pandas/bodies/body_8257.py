# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_insert.py
# see GH#7299
# pre-2.0 with mismatched tzs we would cast to object
idx = date_range("1/1/2000", periods=3, freq="D", tz="Asia/Tokyo", name="idx")

# mismatched tz -> cast to object (could reasonably cast to same tz or UTC)
item = Timestamp("2000-01-04", tz="US/Eastern")
result = idx.insert(3, item)
expected = Index(
    list(idx[:3]) + [item.tz_convert(idx.tz)] + list(idx[3:]),
    name="idx",
)
assert expected.dtype == idx.dtype
tm.assert_index_equal(result, expected)

item = datetime(2000, 1, 4, tzinfo=pytz.timezone("US/Eastern"))
result = idx.insert(3, item)
expected = Index(
    list(idx[:3]) + [item.astimezone(idx.tzinfo)] + list(idx[3:]),
    name="idx",
)
assert expected.dtype == idx.dtype
tm.assert_index_equal(result, expected)
