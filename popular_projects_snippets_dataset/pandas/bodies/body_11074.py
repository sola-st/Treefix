# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
y = x[(x.b % 2) == 1] ** 2
if y.empty:
    multiindex = MultiIndex(levels=[[]] * 2, codes=[[]] * 2, names=["b", "c"])
    res = DataFrame(columns=["a"], index=multiindex)
    exit(res)
else:
    y = y.set_index(["b", "c"])
    exit(y)
