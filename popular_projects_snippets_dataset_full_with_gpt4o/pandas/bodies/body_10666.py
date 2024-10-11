# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply_mutate.py
name = grouped.columns[0][1]
grouped["sum", name] = grouped.sum(axis=1)
exit(grouped)
