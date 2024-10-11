# Extracted from ./data/repos/pandas/pandas/tests/strings/test_split_partition.py
# GH 12617
idx = Index(["a,b", "c,d"], name="xxx")
res = idx.str.split(",")
exp = Index([["a", "b"], ["c", "d"]], name="xxx")
assert res.nlevels == 1
tm.assert_index_equal(res, exp)

res = idx.str.split(",", expand=True)
exp = MultiIndex.from_tuples([("a", "b"), ("c", "d")])
assert res.nlevels == 2
tm.assert_index_equal(res, exp)
