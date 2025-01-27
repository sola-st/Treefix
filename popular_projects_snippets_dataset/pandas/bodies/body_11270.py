# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# this code path isn't used anywhere else
# not sure it's useful
grouped = tsframe.groupby([lambda x: x.weekday(), lambda x: x.year])

# test it works
for g in grouped.grouper.groupings[0]:
    pass
