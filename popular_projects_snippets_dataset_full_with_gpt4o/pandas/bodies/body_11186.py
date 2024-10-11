# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 37725
g = DataFrame({"A": [1], "B": [2], "C": [3]}).groupby([0, 0, 1], axis=1)
match = "Cannot subset columns when using axis=1"
with pytest.raises(ValueError, match=match):
    g[["A", "B"]].sum()
