# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
# empty case
result = DataFrame.from_records([], columns=["foo", "bar", "baz"])
assert len(result) == 0
tm.assert_index_equal(result.columns, Index(["foo", "bar", "baz"]))

result = DataFrame.from_records([])
assert len(result) == 0
assert len(result.columns) == 0
