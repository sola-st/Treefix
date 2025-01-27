# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
a = Series(["\u05d0"] * 1000)
a.name = "title1"
repr(a)  # should not raise exception
