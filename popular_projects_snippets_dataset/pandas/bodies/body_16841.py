# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
found = [
    c for c in group.columns if c in columns or c.replace(suffix, "") in columns
]

# filter
group = group.loc[:, found]

# get rid of suffixes, if any
group = group.rename(columns=lambda x: x.replace(suffix, ""))

# put in the right order...
group = group.loc[:, columns]

exit(group)
