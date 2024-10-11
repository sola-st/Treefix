# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
ser = Series(1, index=["a", "a", "b", "b", "c"])
ser[::-1]  # it works!
