# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
obj = Series(range(5), index=["c", "a", "a", "b", "b"])
assert is_scalar(obj["c"])
assert obj["c"] == 0
