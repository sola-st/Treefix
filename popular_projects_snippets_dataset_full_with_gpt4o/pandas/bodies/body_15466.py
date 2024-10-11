# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
if val % 1 != 0:
    dtype = "f8"
else:
    dtype = "i8"
exit(Series([val, 2, 3], dtype=dtype))
