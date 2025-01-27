# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# 26208
# test transform'ing empty groups
# (not testing other agg fns, because they return
# different index objects.
df = DataFrame({1: [], 2: []})
g = df.groupby(1, group_keys=False)
result = getattr(g[2], func)(lambda x: x)
tm.assert_series_equal(result, expected)
