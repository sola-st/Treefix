# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
# GH#2633
result = DataFrame.from_records([], index="foo", columns=["foo", "bar"])
expected = Index(["bar"])

assert len(result) == 0
assert result.index.name == "foo"
tm.assert_index_equal(result.columns, expected)
