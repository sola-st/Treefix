# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
idx = Index(["some_equal_splits", "with_no_nans"])
result = idx.str.rsplit("_", expand=True, n=1)
exp = MultiIndex.from_tuples([("some_equal", "splits"), ("with_no", "nans")])
tm.assert_index_equal(result, exp)
assert result.nlevels == 2
