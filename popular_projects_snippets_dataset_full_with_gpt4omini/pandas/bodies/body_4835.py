# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# https://github.com/pandas-dev/pandas/issues/23677

idx = Index(["nosplit", "alsonosplit", np.nan])
result = idx.str.split("_", expand=True)
exp = idx
tm.assert_index_equal(result, exp)
assert result.nlevels == 1
