# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# The expected values if we change a single row
cats1 = Categorical(["a", "a", "b", "a", "a", "a", "a"], categories=["a", "b"])
idx1 = Index(["h", "i", "j", "k", "l", "m", "n"])
values1 = [1, 1, 2, 1, 1, 1, 1]
exp_single_row = DataFrame({"cats": cats1, "values": values1}, index=idx1)
exit(exp_single_row)
