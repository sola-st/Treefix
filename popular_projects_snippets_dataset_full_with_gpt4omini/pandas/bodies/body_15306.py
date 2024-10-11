# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#17286
ser = Series([1] * 4, index=Index(["a", "b", "c", 1.0]))
assert ser["a"] == 1
assert ser[1.0] == 1
