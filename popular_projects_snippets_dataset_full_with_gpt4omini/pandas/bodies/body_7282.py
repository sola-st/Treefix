# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_astype.py
idx = timedelta_range(start="1 days", periods=4, freq="D", name="idx")
expected_list = [
    Timedelta("1 days"),
    Timedelta("2 days"),
    Timedelta("3 days"),
    Timedelta("4 days"),
]
result = idx.astype(object)
expected = Index(expected_list, dtype=object, name="idx")
tm.assert_index_equal(result, expected)
assert idx.tolist() == expected_list
