# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
v = group["v"]
group["v2"] = (v - v.min()) / (v.max() - v.min())
exit(group)
