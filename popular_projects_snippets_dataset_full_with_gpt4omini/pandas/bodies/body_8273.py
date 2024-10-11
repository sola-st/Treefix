# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
idx = date_range(start="2013-01-01", periods=4, freq="M", name="idx", tz=tz)
expected_list = [
    Timestamp("2013-01-31", tz=tz),
    Timestamp("2013-02-28", tz=tz),
    Timestamp("2013-03-31", tz=tz),
    Timestamp("2013-04-30", tz=tz),
]
expected = Index(expected_list, dtype=object, name="idx")
result = idx.astype(object)
tm.assert_index_equal(result, expected)
assert idx.tolist() == expected_list
