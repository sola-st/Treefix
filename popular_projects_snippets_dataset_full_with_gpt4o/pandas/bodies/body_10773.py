# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_subclass.py
assert isinstance(group, tm.SubclassedSeries)
assert hasattr(group, "testattr")
exit(group.testattr)
