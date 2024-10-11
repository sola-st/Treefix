# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
y = x[(x.b % 2) == 1] ** 2
if y.empty:
    multiindex = MultiIndex(
        levels=[[]] * 2, codes=[[]] * 2, names=["foo", "bar"]
    )
    res = DataFrame(columns=["a", "b"], index=multiindex)
    exit(res)
else:
    exit(y)
