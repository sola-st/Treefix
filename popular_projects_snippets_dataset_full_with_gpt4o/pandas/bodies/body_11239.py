# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
assert sorted(df.groupby("A").grouper) == ["bar", "foo"]
