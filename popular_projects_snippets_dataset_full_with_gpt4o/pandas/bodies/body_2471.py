# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
cats = Categorical(["a", "a", "a", "a", "a", "a", "a"], categories=["a", "b"])
idx = Index(["h", "i", "j", "k", "l", "m", "n"])
values = [1, 1, 1, 1, 1, 1, 1]
orig = DataFrame({"cats": cats, "values": values}, index=idx)
exit(orig)
