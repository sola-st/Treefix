# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
idx = Index(["a,b", "c,d"], name="xxx")
# should preserve name
result = idx.str.partition(",", expand=False)
expected = Index(np.array([("a", ",", "b"), ("c", ",", "d")]), name="xxx")
assert result.nlevels == 1
tm.assert_index_equal(result, expected)
