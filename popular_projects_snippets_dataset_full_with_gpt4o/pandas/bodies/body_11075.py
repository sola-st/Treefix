# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
y = x[(x.b % 2) == 1] ** 2
if y.empty:
    exit(DataFrame())
else:
    y = y.set_index(["b", "c"])
    exit(y)
