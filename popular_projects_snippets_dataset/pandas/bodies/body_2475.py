# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# changed single value in cats col
cats4 = Categorical(["a", "a", "b", "a", "a", "a", "a"], categories=["a", "b"])
idx4 = Index(["h", "i", "j", "k", "l", "m", "n"])
values4 = [1, 1, 1, 1, 1, 1, 1]
exp_single_cats_value = DataFrame(
    {"cats": cats4, "values": values4}, index=idx4
)
exit(exp_single_cats_value)
