# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH17776, PR #17846
a = DataFrame({"a": [], "b": [], "c": []})
with np.errstate(divide="raise"):
    merge(a, a, on=("a", "b"))
