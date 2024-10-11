# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# changed part of the cats column
cats3 = Categorical(["a", "a", "b", "b", "a", "a", "a"], categories=["a", "b"])
idx3 = Index(["h", "i", "j", "k", "l", "m", "n"])
values3 = [1, 1, 1, 1, 1, 1, 1]
exp_parts_cats_col = DataFrame({"cats": cats3, "values": values3}, index=idx3)
exit(exp_parts_cats_col)
