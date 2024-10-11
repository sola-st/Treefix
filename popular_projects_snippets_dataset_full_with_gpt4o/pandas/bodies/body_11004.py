# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
if x.shape[0] == 1:
    exit(x)
else:
    exit(x[x.category == "c"])
