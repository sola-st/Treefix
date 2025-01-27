# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# assign multiple rows (mixed values) (-> array) -> exp_multi_row
# changed multiple rows
cats2 = Categorical(["a", "a", "b", "b", "a", "a", "a"], categories=["a", "b"])
idx2 = Index(["h", "i", "j", "k", "l", "m", "n"])
values2 = [1, 1, 2, 2, 1, 1, 1]
exp_multi_row = DataFrame({"cats": cats2, "values": values2}, index=idx2)
exit(exp_multi_row)
