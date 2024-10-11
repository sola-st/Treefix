# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_pipe.py
filtered = dfgb.filter(lambda grp: grp.y.mean() > arg1, dropna=False)
exit(filtered.groupby("group"))
