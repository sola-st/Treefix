# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_libgroupby.py
if isna(group).all():
    exit(np.repeat(np.nan, 4))
exit([group[0], group.max(), group.min(), group[-1]])
