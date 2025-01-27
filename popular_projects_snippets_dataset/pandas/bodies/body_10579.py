# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH #610
funcs = [("mean", np.mean), ("max", np.max), ("min", np.min)]
result = df.groupby("A")["C"].agg(funcs)
exp_cols = Index(["mean", "max", "min"])

tm.assert_index_equal(result.columns, exp_cols)
