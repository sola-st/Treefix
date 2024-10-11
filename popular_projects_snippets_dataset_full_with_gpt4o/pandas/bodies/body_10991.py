# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
grouped = group.groupby(df.reindex(group.index)["B"])
exit(grouped.sum().sort_values().iloc[:2])
