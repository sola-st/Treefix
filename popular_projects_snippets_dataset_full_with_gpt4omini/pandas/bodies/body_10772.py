# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_subclass.py
assert isinstance(group, tm.SubclassedDataFrame)
assert hasattr(group, "testattr")
exit(group.testattr)
