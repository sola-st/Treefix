# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
idx = Index(["nosplit", "alsonosplit"])
result = idx.str.rsplit("_", expand=True)
exp = idx
tm.assert_index_equal(result, exp)
assert result.nlevels == 1
