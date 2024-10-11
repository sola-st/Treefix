# Extracted from ./data/repos/pandas/pandas/tests/series/test_repr.py
s = Series(index=date_range("20010101", "20020101"), name="test", dtype=object)
assert "Name: test" in repr(s)
