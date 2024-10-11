# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#14865
ser = Series(["a", "b", "c"], index=Index([1, 2, 3], dtype="category"))
assert ser.get(3) == "c"
assert ser[3] == "c"
