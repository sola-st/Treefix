# Extracted from ./data/repos/pandas/pandas/tests/extension/base/groupby.py
df = pd.DataFrame({"A": [1, 1, 2, 2, 3, 3, 1, 4], "B": data_for_grouping})
df.groupby("B", group_keys=False).apply(groupby_apply_op)
df.groupby("B", group_keys=False).A.apply(groupby_apply_op)
df.groupby("A", group_keys=False).apply(groupby_apply_op)
df.groupby("A", group_keys=False).B.apply(groupby_apply_op)
