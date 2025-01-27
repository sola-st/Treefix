# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply_mutate.py
x["rank"] = x.val.rank(method="min")
exit(x.groupby("cat2")["rank"].min())
