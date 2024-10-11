# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
exit(group.groupby("B")["C"].sum().sort_values().iloc[:2])
